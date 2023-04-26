import requests
import os
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES


def get_key(url):
    resp = requests.get(url)
    return resp.text


def get_url(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    list_1 = resp.text.split("\n")

    # 创建列表，然后把迭代后的数据放进列表
    key_url = None
    datas = []
    for data in list_1:
        if data[:11] == "#EXT-X-KEY:":
            key_url = data.split("=")[2]
        if data == '':
            continue
        else:
            if data[0] == "#":
                continue
            datas.append(data)
    datas.append(key_url)

    return datas, key_url


async def down_file(url, session, i, key):
    print(f"开始下载{i}个")
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{i}.ts", mode='wb') as f:
            await f.write(await resp.content.read())
    print(f"第{i}下载完成")

    print(f'第{i}开始解密')
    aes = AES.new(key=key, IV=b"0000000000000000", mode=AES.MODE_CBC)
    async with aiofiles.open(f"video/{i}.ts", mode='rb') as f1, \
            aiofiles.open(f"video/temp_{i}.ts", mode="wb") as f2:
        bs = await f1.read()
        await f2.write(aes.decrypt(bs))

    print(f"第{i}解密完毕")


async def resp_url(datas, key):
    tasks = []
    i = 1
    async with aiohttp.ClientSession() as session:
        for url in datas:
            da = asyncio.create_task(down_file(url, session, i, bytes(key, encoding="utf-8")))
            tasks.append(da)
            i += 1
        await asyncio.wait(tasks)


def merge_ts_file(n):
    list_1 = []
    for i in range(1, n + 1):
        list_1.append(f"video\\temp_{i}.ts")

    win = "+".join(list_1)
    shell_str = 'copy /b ' + win + ' video\\奥利给.mp4'
    os.system(shell_str)


def main(url):
    # 得到每个m3u8以及key的下载地址
    data, key_url = get_url(url)
    # 设置下载数量
    data = data[:5]
    key_url = key_url[1:-1]

    # 拿取密钥
    key = get_key(key_url)

    # 运行异步协程下载每个视频并对其进行解密
    loop = asyncio.get_event_loop()
    loop.run_until_complete(resp_url(data, key))

    # 合并文件
    merge_ts_file(len(data))


if __name__ == '__main__':
    url = 'https://video.buycar5.cn/20200825/A7q2wVRI/1000kb/hls/index.m3u8'
    main(url)
