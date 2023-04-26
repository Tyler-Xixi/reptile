#https://video.pearvideo.com/mp4/adshort/20210729/1627632031578-15732329_adpkg-ad_hd.mp4
#https://video.pearvideo.com/mp4/adshort/20210729/cont-1736782-15732329_adpkg-ad_hd.mp4
#https://video.pearvideo.com/mp4/adshort/20210729/cont_1736782-15732329_adpkg-ad_hd.mp4
#1.拿到cont-ID
#2.拿到videoStauts返回的 json -> srcURL
#3.将srcURL的内容进行修整
#4.将最后修整的url进行下载
import requests
url = "https://www.pearvideo.com/video_1736782"

cont_ID = url.split("_")[1]
# print(cont_ID)
videoStauts = "https://www.pearvideo.com/videoStatus.jsp?contId=1736782&mrd=0.49217956178595457"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    #防盗链:溯源 本次请求的上一级是谁
    "Referer": "https://www.pearvideo.com/video_1736782"
}

resp = requests.get(videoStauts,headers=headers)

dic = resp.json()
systemTime = dic["systemTime"]
serURL = dic["videoInfo"]["videos"]["srcUrl"]
serURL = serURL.replace(systemTime,f"cont-{cont_ID}")
with open('video.mp4', mode='wb') as f:
    f.write(requests.get(serURL).content)


