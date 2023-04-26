import asyncio
import aiohttp
import time
#
#
# async def fun1():
#     print("陈独秀")
#     await asyncio.sleep(3)
#     print("陈独秀")
#
#
# async def fun2():
#     print("李大钊")
#     await asyncio.sleep(2)
#     print("李大钊")
#
#
# async def fun3():
#     print("周树人")
#     await asyncio.sleep(4)
#     print("周树人")
#
#
# async def main():
#     tasks = [
#         asyncio.create_task(fun1()),
#         asyncio.create_task(fun2()),
#         asyncio.create_task(fun3())
#     ]
#
#
#     await asyncio.wait(tasks)
#
#
# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(main())
#     t2 = time.time()
#     print(t2 - t1)






urls = [
        "http://img.netbian.com/file/2021/0731/d9f54a0eeb1693e3960973e19f5e9f60.jpg",
        "http://img.netbian.com/file/2021/0730/def5ad168856c9bccca9de9d4dd5d25f.jpg",
        "http://img.netbian.com/file/2021/0726/7ea8ed7c9b17216c10c7e9d1ce2b047a.jpg",
        "http://img.netbian.com/file/2021/0730/50923454a663a1e8994599409c07485e.jpg"
    ]



async   def  aiohttp_load(url):
    name = url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session:   # aiohttp 等价于 requests 模块
        async with session.get(url) as resp:            # 将aiohttp给 session 会话进行获取 最后 as 给resp请求
            with open(f"C:\\Users\\Administrator\\Desktop\\TylerXixi\\爬虫\\文件储存\\phto\\{name}.jpg",  mode='wb') as f:
                f.write(await resp.content.read())
    print(name, "ok！")




async def main():
    tasks = []

    for url in urls:
        tasks.append(aiohttp_load(url))

    await asyncio.wait(tasks)



if __name__ == '__main__':
    asyncio.run(main())


