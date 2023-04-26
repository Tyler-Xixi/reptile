import time
import asyncio
import aiohttp
import requests
import aiofiles
from lxml import etree
from selenium.webdriver import Chrome
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.chrome.options import Options



def no_heard():
    opt = Options()
    opt.add_argument("--headless")
    opt.add_argument("--disbale-gpu")

    return Chrome(options=opt)

def down_href(web, url):
    # 打开网页
    web.get(url)
    time.sleep(2)
    # 对页面进行翻页, 加载更多视频
    for i in range(300):
        # 下拉
        web.execute_script('window.scrollBy(0,250)')
        if i % 10 == 0:
            time.sleep(0.5)

    time.sleep(0.5)
    # 找出每一个视频的超链接地址
    html = etree.HTML(web.page_source)
    data = "\n".join(html.xpath('//*[@id="rooot"]/section/main/section/main/div/div/a/@href'))

    # 将我们拿到的每个视频的超链接地址进行保存
    with open("down_href.text", mode="w") as f:
        f.write(data)
    web.close()


def get_video_href(url, tasks):
    web = no_heard()
    web.get(url)

    html = etree.HTML(web.page_source)
    web.close()
    src = html.xpath('//*[@id="mse"]/video/@src')

    tasks.append(src[0])


def down_video_href():
    tasks = []
    with ThreadPoolExecutor(10) as t:
        with open("down_href.text", mode='r') as f:
            for line in f:
                line = line.strip()
                t.submit(get_video_href, url=line, tasks=tasks)

    with open("down_video_src.text", mode='w') as f:
        print("开始写入！")
        f.write("\n".join(tasks))
    print("保存完毕！")


async def down_file(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{name}.mp4", mode="wb") as f:
            await f.write(await resp.content.read())

    print(f"{name}完成")


async def down_video_file():
    tasks = []

    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("down_video_src.text", mode="r") as f:
            async for line in f:
                line = line.strip()
                name = line[35:50].replace("/", '_')

                task = asyncio.create_task(down_file(line, name, session))
                tasks.append(task)

            await asyncio.wait(tasks)


def main(url):
    web = Chrome()

    # 下载每个视频的超链接
    down_href(web, url)

    # 拿到每个视频的下载地址
    down_video_href()

    # 采用异步协程进行每个文件的下载
    asyncio.run(down_video_file())


if __name__ == '__main__':
    name = "小姐姐"
    url = f"https://haokan.baidu.com/web/search/page?query={name}"
    main(url)

