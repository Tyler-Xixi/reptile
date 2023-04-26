#首页目录的url
#http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}
#目录章节内容的url
#http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}


import requests
import asyncio
import aiohttp
import aiofiles
import time
import json


async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for item in dic["data"]["novel"]["items"]:
        title = item["title"]
        cid = item["cid"]   #检索定位完首页的 标题和cid 然后进行异步操作

        tasks.append(aio_download(cid, title, book_id))
    await asyncio.wait(tasks)



async def aio_download(cid, title, book_id):
    data = {
        "book_id":book_id,
        "cid":f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)  #将data数据通过json变成字符串
    url = f'http://dushu.baidu.com/api/pc/getChapterContent?data={data}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()

            async with aiofiles.open(f"C:\\Users\\Administrator\\Desktop\\TylerXixi\\爬虫\\文件储存\\Text\\{title}.txt", mode='w', encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])



if __name__ == '__main__':
    book_id = "4306063500"
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + book_id + '"}'
    asyncio.run(getCatalog(url))