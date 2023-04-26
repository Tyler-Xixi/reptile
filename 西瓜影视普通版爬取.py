# import requests
# import asyncio
# import aiohttp
# import aiofiles
# import json
#
# def get_url(url):
#     resp = requests.get(url)
#     resp.encode = "utf-8"
#
#     list_1 = resp.text.split("\n")
#     datas = []
#     for data in list_1:
#         if data == '':
#             continue
#         else:
#             if data[0] == "#":
#                 continue
#         datas.append('https://v3.szjal.cn/20200118/HTdRSdMP/hls/' + data)
#
#     return datas
#
#
# async def down_file(url, session, name):
#     print(f"{name} 开始下载!")
#     async with session.get(url) as resp:
#         async with aiofiles.open(f"video\\{name}.ts", mode="wb") as f:
#             await f.write(await resp.content.read())
#     print(f"{name} 下载完成！")
#
#
# async def down_video(datas):
#     tasks = []
#     async with aiohttp.ClientSession() as session:
#         i = 1
#         async for url in datas:
#             da = asyncio.create_task(down_file(url, session, i))
#             tasks.append(da)
#             i += 1
#
#         await asyncio.wait(tasks)
#
#
# def main(url):
#     datas = get_url(url)[:200]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(down_video(datas))
#
#
# if __name__ == '__main__':
#     url = 'https://v3.szjal.cn/20200118/HTdRSdMP/hls/index.m3u8'
#     main(url)
#
#
#

















import requests
import asyncio
import aiohttp
import aiofiles

def main(url):
    datas = get_url(url)[0:10]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(down_video(datas))


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
        datas.append('https://v3.szjal.cn/20200118/HTdRSdMP/hls/' + data)

    return datas



async def down_video(datas):
    tasks = []
    i = 1
    async with aiohttp.ClientSession() as session:
        async for url in datas:
            da = asyncio.create_task(down_file(url, session, i))
            tasks.append(da)
            i += 1
        await asyncio.wait(tasks)




async def down_file(url, session, name):
    print(f"{name} 开始下载!")
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{name}.ts", mode="wb") as f:
            await f.write(await resp.content.read())
    print(f"{name} 下载完成！")



if __name__ == '__main__':
    url = 'https://v3.szjal.cn/20200118/HTdRSdMP/hls/index.m3u8'
    main(url)

