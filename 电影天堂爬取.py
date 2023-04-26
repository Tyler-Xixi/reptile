import requests
import re
import json
from lxml import etree

def main(url):
    get_url(url)



def get_url(url):
    resp = requests.get(url)
    resp.encoding = 'gb2312'
    obj = re.compile(r'<div class="title_all"><p><strong>迅雷电影资源</strong><em><a href="/html/gndy/index.html">更多>></a></em></p></div>.*?<tr>(?P<url>.*?)<td width="15%" class="inddline"><font color=#FF0000>2021-07-30</font></td>', re.S)
    obj1 = re.compile(r"<a href='(?P<herf>.*?)'>", re.S)
    obj2 = re.compile(r'◎译　　名(?P<herf_1>.*?)<br />◎导　　演', re.S)
    result1 = obj.finditer(resp.text)
    datas = []
    for data in result1:
        ul = data.group('url')

        result2 = obj1.finditer(ul)

        for data1 in result2:
            child_herf = url.strip("/") + data1.group('herf')
            datas.append(child_herf)

        for herf in datas:
            herf_resp = requests.get(herf)
            herf_resp.encoding = 'gb2312'
            divs = herf_resp.text
            result3 = obj2.search(divs)
            print(result3.group('herf_1'))



def down_url(url):
    pass


if __name__ == '__main__':
    url = 'https://www.dytt8.net/'
    main(url)
