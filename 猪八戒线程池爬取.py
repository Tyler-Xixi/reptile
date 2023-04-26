import requests
import re
from concurrent.futures import ThreadPoolExecutor
import time


def down_img(url_1, x):
    resp = requests.get(url_1)

    with open(f"C:\\Users\\Administrator\\Desktop\\phto\\{x}.jpg", mode="wb") as f:
        f.write(resp.content)
    print(x,"over!")


def url_text(name, i):
    url = f"https://search.zbj.com/f/?kw={name}ype=new"


    obj = re.compile(r"class='service-case-img ' src='(?P<url>.*?)'/>", re.S)

    resp = requests.get(url)

    datas = obj.finditer(resp.text)

    with ThreadPoolExecutor(50) as t:
        # 假设有100个项目
        for data in datas:
            t.submit(down_img, url_1=data.group("url"), x=i)
            i+=1

    return i

i = 1
url_list = [
"vi设计","微信开发"
    ]

for li in url_list:
    i = url_text(li, i)




# import time
# from concurrent.futures import ThreadPoolExecutor,process


# def fun(name):
#     for i in range(1,500):
#         t1 = print(name,i)
#
#
# if __name__ == '__main__':
#     with ThreadPoolExecutor(50) as t:
#         for i in range(1,500):
#             t2 = t.submit(fun,name=f"线程{i}")
#     print(t2 - t1)
