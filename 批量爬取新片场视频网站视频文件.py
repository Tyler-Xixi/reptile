import requests
import re
from lxml import etree
import time

def down(name):
    global data_name

    url_2 = f"https://www.xinpianchang.com/a{name}?from=ArticleList"

    obj = re.compile(r'var vid = "(?P<Url>.*?)";', re.S)
    resq_2 = requests.get(url_2)

    ret = obj.findall(resq_2.text)[0]

    url = f"https://mod-api.xinpianchang.com/mod/api/v2/media/{ret}?appKey=61a2f329348b3bf77&extend=userInfo%2CuserStatus"

    resq = requests.get(url)

    json_1 = resq.json()
    
    # 0.高清 1.标清 2.清晰 3.流畅
    a = 3
    url_1 = json_1['data']["resource"]["progressive"][a]["url"]

    resq_1 = requests.get(url_1)

    with open("视频%d.mp4" % data_name, mode="wb") as f:
        f.write(resq_1.content)


def data_articleid(name):
    global data_name
    url_3 = f"https://www.xinpianchang.com/channel/index/type-/sort-like/duration_type-0/resolution_type-/page-{name}"

    resq_3 = requests.get(url_3)
    html = etree.HTML(resq_3.text)

    datas = html.xpath("/html/body/div[8]/div[2]/ul/li")
    data_list = []

    for data in datas:
        data_list.append(data.get("data-articleid"))

    for i in data_list[:3]:
        print("第 %d 次爬取开始！" % data_name)
        down(i)
        print("第 %d 次爬取 over!" % data_name)
        data_name += 1
        time.sleep(1)


data_name = 1
for i in range(1,26):
    data_articleid(str(i))

