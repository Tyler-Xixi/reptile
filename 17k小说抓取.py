# import requests
#
# url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
#
# resp = requests.get(url,headers = {
#     "Cookie":"GUID=71011bd5-6154-471d-89fe-fbe680a3318c; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1627625560; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F09%252F09%252F18%252F78451809.jpg-88x88%253Fv%253D1627625638000%26id%3D78451809%26nickname%3DTylerXixi%26e%3D1643179133%26s%3D139a89752e8bbcca; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2278451809%22%2C%22%24device_id%22%3A%2217af60b18110-012b5a69f69b2b-f7f1939-2073600-17af60b18124f0%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2271011bd5-6154-471d-89fe-fbe680a3318c%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1627627558"
# })
# resp.encoding = 'utf-8'
# print(resp.text)


import requests
from lxml import etree
url = "https://www.17k.com/chapter/3328785/44207503.html"

resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)

html = etree.HTML(resp.text)

words = html.xpath("/html/body/div[4]/div[2]/div[2]/div[1]//p/text()")

print(words)