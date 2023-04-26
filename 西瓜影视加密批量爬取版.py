import requests
import os
import re
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES
from selenium.webdriver import Chrome
from lxml import etree
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor

list_data_1 = []


def no_hrad():
    opt = Options()
    opt.add_argument("--disable-blink-features=AutomationControlled")
    opt.add_argument("--headless")
    opt.add_argument("--disbale-gpu")

    web = Chrome(options=opt)

    return web


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


async def down_file(url, session, i, key, jj):
    print(f"开始下载第{jj}集{i}个")
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/第{jj}集{i}.ts", mode='wb') as f:
            await f.write(await resp.content.read())
    print(f"第{jj}集{i}下载完成")

    print(f'第{jj}集{i}开始解密')
    aes = AES.new(key=key, IV=b"0000000000000000", mode=AES.MODE_CBC)
    async with aiofiles.open(f"video/第{jj}集{i}.ts", mode='rb') as f1, \
            aiofiles.open(f"video/第{jj}集temp_{i}.ts", mode="wb") as f2:
        bs = await f1.read()
        await f2.write(aes.decrypt(bs))

    print(f"第{jj}集{i}解密完毕")


async def resp_url(datas, key, jj):
    tasks = []
    i = 1
    async with aiohttp.ClientSession() as session:
        for url in datas:
            da = asyncio.create_task(down_file(url, session, i, bytes(key, encoding="utf-8"), jj))
            tasks.append(da)
            i += 1
        await asyncio.wait(tasks)


def merge_ts_file(n):
    list_1 = []
    for i in range(1, n + 1):
        list_1.append(f"video\\第{i}级temp_{i}.ts")

    win = "+".join(list_1)
    shell_str = f'copy /b ' + win + ' 第{i}集.mp4'
    os.system(shell_str)


def down_mp4(url, i):
    print(f'第{i}集开始下载！')
    # 得到每个m3u8以及key的下载地址
    data, key_url = get_url(url)
    # 设置下载数量
    data = data
    key_url = key_url[1:-1]

    # 拿取密钥
    key = get_key(key_url)

    # 运行异步协程下载每个视频并对其进行解密
    loop = asyncio.get_event_loop()
    loop.run_until_complete(resp_url(data, key, i))

    # 合并文件
    merge_ts_file(len(data), i)


def get_mp4_url(url, url_1):
    resp = requests.get(url)
    obj = etree.HTML(resp.text)

    datas = obj.xpath('/html/body/div[6]/div/div[3]/ul[2]/li')
    list_1 = []
    for data in datas:
        list_1.append(url_1 + data.xpath('./a/@href')[0])

    return list_1


def get_m3u8_url(url):
    web = no_hrad()
    web.get(url)
    obj = re.compile(r'https://video.buycar5.cn/20200825/(?P<m3u8_url>.*?)/', re.S)
    data = obj.search(web.page_source)
    list_data_1.append("https://video.buycar5.cn/20200825/" + data.group("m3u8_url") + "/1000kb/hls/index.m3u8")


def get_m3u8_url_1(url):
    print('开始请求每个m3u8地址')
    href_data = get_mp4_url(url, url.rsplit("/", 2)[0])
    with ThreadPoolExecutor(7) as t:
        for href in href_data[:7]:
            t.submit(get_m3u8_url, url=href)

    with ThreadPoolExecutor(len(href_data) - 7) as t:
        for href in href_data[7:]:
            t.submit(get_m3u8_url, url=href)

    print("地址请求完毕")


def main(url):
    get_m3u8_url_1(url)
    i = 1

    # 这个运行不了就运行下面的
    # with ThreadPoolExecutor(len(list_data_1)) as t:
    #     for m3u8 in list_data_1:
    #         t.submit(down_mp4, url=m3u8, i=i)
    #         i += 1

    # 备用下载
    for m3u8 in list_data_1:
        down_mp4(m3u8, i)
        i += 1


if __name__ == '__main__':
    url = 'https://www.nmgtyjt.com/xigua110/37945.html'
    main(url)
