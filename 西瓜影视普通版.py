import requests
import asyncio
import aiohttp
import aiofiles
import os


def main(url):
    datas = get_url(url)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(down_video(datas))

    merge_ts_file(len(datas))


def get_url(url):
    resp = requests.get(url)
    resp.encode = "utf-8"

    list_1 = resp.text.split("\n")
    datas = []
    for data in list_1:
        if data == '':
            continue
        else:
            if data[0] == "#":
                continue
        datas.append(data)

    return datas


async def down_video(datas):
    tasks = []
    i = 1
    async with aiohttp.ClientSession() as session:
        for url in datas:
            da = asyncio.create_task(down_file(url, session, i))
            tasks.append(da)
            i += 1
        await asyncio.wait(tasks)


async def down_file(url, session, name):
    print(f"{name} 开始下载!")
    async with session.get(url) as resp:
        async with aiofiles.open(f"mp4/{name}.ts", mode="wb") as f:
            await f.write(await resp.content.read())
    print(f"{name} 下载完成！")


def merge_ts_file(n):
    print("开始合并")
    list_1 = []
    for i in range(1, n + 1):
        list_1.append(f"mp4\\{i}.ts")

    ts_file = "+".join(list_1)
    shell_str = 'copy /b ' + ts_file + ' mp4\\tyler.mp4'
    os.system(shell_str)


if __name__ == '__main__':
    # url = 'https://v3.szjal.cn/20200118/HTdRSdMP/hls/index.m3u8'
    # 越狱url
    url = 'https://vod.bunediy.com/20210715/PrYG1Aqa/index.m3u8'
    main(url)
