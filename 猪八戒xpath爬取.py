import requests
from lxml import etree



def get_url():

    url = "https://chongqing.zbj.com/search/f/?type=new&kw=logo"

    resp = requests.get(url)
    # print(resp.text)
    html = etree.HTML(resp.text)

    divs = html.xpath("/html/body/div[6]/div/div/div[3]/div[5]/div[1]/div")
    for div in divs:
        price = div.xpath("./div/div/a[1]/div[2]/div[1]/span/text()")
        title = "logo".join(div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()"))
        compny = div.xpath("./div/div/a[2]/div[1]/p/text()")
        adress = div.xpath("./div/div/a[2]/div[1]/div/span/text()")
        list_get = []
        list_get = price,title,compny,adress
        print(list_get)

