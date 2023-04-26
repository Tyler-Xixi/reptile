import requests
import re


def donw_load(name, url):
    reps = requests.get(url)
    with open(f"C:\\Users\\Administrator\\Desktop\image\\{name}.jpg", mode="wb") as f:
        f.write(reps.content)


def url_load(name,i):
    url = f"http://www.bizhi360.com/{name}/list_{id}.html"
    reps = requests.get(url)
    reps.encoding = "utf-8"
    obj = re.compile(r'target="_blank" title="(?P<name>.*?)"><img src="(?P<url>.*?)"', re.S)
    datas = obj.finditer(reps.text)
    for data in datas:
        donw_load(data.group("name"), data.group("url"))

url_list= [
"weimei","qiche","3d","dongman"
    ]

i = 1
for li in url_list:
    i = url_load(li,i)
