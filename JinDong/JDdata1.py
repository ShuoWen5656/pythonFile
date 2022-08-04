import requests
import re
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt,html):
    try:
        dianpumingcheng = re.findall(r'p-commit')
        dianpuleixing =re.findall()
        tlt =re.findall()
        plt = re.findall()
        for s in range(len(tlt)):
            ilt.append([dianpumingcheng,dianpuleixing,tlt,plt])
    except:
        print('')
            
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format('序号','店铺名称','店铺类型','商品名称','价格'))
    count = 0
    for k in ilt:
        count = count + 1
        print(tplt.format(count,k[0],k[1],k[2],k[3]))

def main():
    goods = '成人纸尿裤'
    depth = 100
    start_url ='https://search.jd.com/Search?keyword=' + goods
    infoList = []
    number0 = [1, 56, 116, 177, 236, 296, 356, 416, 476, 536, 601]
    for n in range(1,90):
        number = number0[10] + 60 * int(n)
        numbers = number0.append(number)
    for i in range(depth):
        try:
            url = start_url + '&qrst=1&stock=1&page=' + str(2*(i+1)-1) + '&s=' + str(numbers[i]) +'&click=0'
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)

main()


