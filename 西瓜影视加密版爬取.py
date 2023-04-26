import requests

#导入异步协程模块
import asyncio
import aiohttp
import aiofiles

#导入解密模块
from

#统一资源管理函数
def main(url):


    # #将url给datas
    datas = get_url(url)

    #运行异步协程
    loop = asyncio.get_event_loop()
    loop.run_until_complete(resp_url(datas))

    #拿取密钥
    key_url = 'https://ts1.yuyuangewh.com:9999/20200825/A7q2wVRI/1000kb/hls/key.key'
    key = get_key(key_url)


    asyncio.run(aio_key(key))

    #进行解密


#请求key的url获取到解密密码
def get_key(url):
    resp =requests.get(url)
    return resp.text


#将m3u8文件进行异步传入解密函数
async def aio_key(key):
    tasks = []

    async with aiofiles.open("urls/m3u8.txt", mode='r', encoding='utf-8') as f:
        line = f
        task = asyncio.create_task(aio_ts(line, key))
        tasks.append(task)

    await asyncio.wait(tasks)


#开始解密文件
async def aio_ts(name, key):
    aes = AES.new(key=key, IV=b"0000000000000000", mode=AES.MODE_CBC)
    async with aiofiles.open(f"video/{name}", mode='rb') as f1,\
        aiofiles.open(f"video/temp_{name}", mode="wb") as f2:

        bs = await f1.read()
        await f2.write(aes.decrypt(bs))
    print(f"{name}解密完毕")


#将url中的m3u8定位提取出并存为列表为请求准备
def get_url(url):

    resp = requests.get(url)
    resp.encoding = 'utf-8'
    list_1 = resp.text.split("\n")

    # 创建列表，然后把迭代后的数据放进列表
    datas = []
    for data in list_1:
        if data == '':
            continue
        else:
            if data[0] == "#":
                continue
            datas.append(data)
    return datas


#将url中的m3u8提取出来 为解密操作
# def down_url(url):
#
#     resp = requests.get(url)
#     list_1 = (resp.text.rsplit("\n"))
#
#     dic = {}
#
#     with open('urls/m3u8.txt', mode='w', encoding='utf-8') as f:
#         for data in list_1:
#             if data == '':
#                 continue
#             else:
#                 if data[0] == "#":
#                     continue
#                 else:
#                     dic = data.rsplit('/')[-1]
#                     f.write(dic)


#导入异步请求，并迭代列表中的么m3u8
async def resp_url(data):
    tasks = []
    i = 1
    async with aiohttp.ClientSession() as session:
        for url in data:
            da = asyncio.create_task(down_file(url, session, i))
            tasks.append(da)
            i += 1
        await asyncio.wait(tasks)


#请求url并下载文件
async def down_file(url,session,i):
    print(f"开始下载{i}个")
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{i}.ts", mode='wb' ) as f:
            await f.write(await resp.content.read())
    print(f"第{i}下载完成")


if __name__ == '__main__':    #入口
    url = 'https://video.buycar5.cn/20200825/A7q2wVRI/1000kb/hls/index.m3u8'
    # down_url(url)
    main(url)