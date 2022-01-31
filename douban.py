"Special Thanks To Douban"

import requests
from bs4 import BeautifulSoup

print("Great Films On Top 250 In Douban -- By lanlan2_")

nameli = []
rateli = []
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like GeCKO) Chrome/45.0.2454.85 Safari/537.36 115Broswer/6.0.3',
    'Referer':'https://movie.douban.com/',
    'Connection':'keep-alive'}
count = 1
pagenum = 0

print("Loading", end="")
for i in range(10):
    resp = requests.get("https://movie.douban.com/top250?start="+str(pagenum), headers=headers)
    resp.encoding = "utf-8"
    res = resp.text
    soup = BeautifulSoup(res, "html.parser")
    ol = soup.find("ol")
    #divs = ol.find_all("div", attrs={"class":"star"})
    #for div in divs:
        #rate_get = div.find_all("span")[1].string
        #rateli.append(rate_get)
    lists = ol.find_all("li")
    for li in lists:
        ass = li.find_all("a")[1]
        sps = ass.find_all("span")[0]
        for sp in sps:
            #nameli.append(str(count)+":"+sp+"\n\t评分："+rateli[count-1])
            nameli.append(str(count)+":"+sp)
            count += 1
    pagenum += 25
    print(".", end="")

print("")
for name in nameli:
    print(name)
