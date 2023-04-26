import requests
from bs4 import BeautifulSoup
import time

def down(name, x, j):
    url = 'http://www.bizhi360.com/%s/list_%d.html' % (name, x)

    resq = requests.get(url)
    resq.encoding = "utf-8"

    page = BeautifulSoup(resq.text, "html.parser")
    ret = page.find_all("a", target="_blank")

    for i in ret:
        url_1 = "http://www.bizhi360.com" + i.get("href")

        ret_1 = requests.get(url_1)
        ret_1.encoding = "utf-8"

        page_1 = BeautifulSoup(ret_1.text, "html.parser")
        page_1 = page_1.find("figure").find("a")

        url_2 = page_1.get("href")
        ret_2 = requests.get(url_2)
        ret_2.encoding = "utf-8"

        with open("%d图片.jpg" % j, mode="wb") as f:
            f.write(ret_2.content)

        j += 1
        time.sleep(1/2)
    print(j)
    return j

j = 1
for i in range(2,5):
    j = down("dongman", i, j)
    print("%d  over!" % i)
