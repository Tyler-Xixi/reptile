import requests
import re
import time
from concurrent.futures import ThreadPoolExecutor


def url_down(data):
    with open(f'data.csv', mode='w', encoding='utf-8') as f:
        f.write(data)


def url_get(i, list_2):
    url = "http://www.xinfadi.com.cn/getPriceData.html"
    data = {
        "limit": "20",
        "current": str(i),
        "pubDateStartTime": '',
        "pubDateEndTime": '',
        "prodPcatid": '',
        "prodCatid": '',
        "prodName":  ''
    }

    resp = requests.post(url, data=data)
    data = (resp.json()["list"])

    list_1 = "" #将列表为空
    for datas in data:
        list_1 += "%s,%s,%s,%s,%s\n" % (datas["prodCat"], datas["prodName"], datas["place"],datas["highPrice"],datas["pubDate"])
    #将里面的元素进行定位
    list_2.append(list_1)
    #拼接字符串


if __name__ == '__main__':
    list_2 = []
    t1 = time.time()
    with ThreadPoolExecutor(5000) as t: #线程池
        for i in range(1, 100):        #迭代页数
            t.submit(url_get, i, list_2)

    print("导入完毕！")
    t2 = time.time()
    print("用时：",t2-t1,'秒')


    url_down("\n".join(list_2))

