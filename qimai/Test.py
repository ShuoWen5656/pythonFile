# 测试用例

from qimai import qimaiPachong
import requests
from urllib import parse
import json
import base64
import xlwt
import xlrd
import random
import string
import time
import html
from xlutils.copy import copy
import random
from bs4 import BeautifulSoup


testProxyUrl = "http://httpbin.org/ip"
testProxyUrlHTTPS = "https://httpbin.org/ip"

proxies = {
    "http": "60.170.204.30:8060",
    "https": "103.23.20.68:80"
}



# 获取一个可用的ip地址
def getOneAvailableProxyIP():

    for i in  range(1, 8):
        req = requests.get("http://www.ip3366.net/free/?stype=1&page=" + str(i))
        html = req.text
        req.encoding = "utf-8"
        soup = BeautifulSoup(html, features="html.parser")
        iplist = soup.select('#list tbody tr')
        for tag in iplist:
            try:
                ipport = tag.findAll('td')[0].text+":"+tag.findAll('td')[1].text
                print(ipport)
                proxies["https"] = ipport
                rsp = requests.get(testProxyUrlHTTPS, proxies=proxies, timeout=5)
                print("wa!!!!!!!,找到一个！:",json.loads(rsp.text))
                # print(tag.findAll('td')[1].text)
            except:
                print("不可用ip：", ipport)
                continue

# get89VIP
def get89Vip():
    for i in  range(1, 7):
        req = requests.get("https://www.89ip.cn/index_"+ str(i) +".html")
        html = req.text
        req.encoding = "utf-8"
        soup = BeautifulSoup(html, features="html.parser")
        iplist = soup.select('.layui-table tbody tr')
        for tag in iplist:
            try:
                ipport = tag.findAll('td')[0].text.replace("\t", "").replace("\n", "")+":"+tag.findAll('td')[1].text.replace("\t", "").replace("\n", "")
                print(ipport)
                proxies["https"] = ipport
                rsp = requests.get(testProxyUrlHTTPS, proxies=proxies, timeout=5)
                print("wa!!!!!!!,找到一个！:",json.loads(rsp.text))
                # print(tag.findAll('td')[1].text)
            except:
                print("不可用ip：", ipport)
                continue


def getKuaidaili():
    for i in  range(1, 4705):
        req = requests.get("https://free.kuaidaili.com/free/inha/"+ str(i) +"/")
        html = req.text
        req.encoding = "utf-8"
        soup = BeautifulSoup(html, features="html.parser")
        iplist = soup.select('#list tbody tr')
        for tag in iplist:
            try:
                if  tag.findAll('td')[2].text == "HTTPS":
                    ipport = tag.findAll('td')[0].text+":"+tag.findAll('td')[1]
                    print(ipport)
                    proxies["https"] = ipport
                    rsp = requests.get(testProxyUrlHTTPS, proxies=proxies, timeout=5)
                    print("wa!!!!!!!,找到一个！:", json.loads(rsp.text))
                # print(tag.findAll('td')[1].text)
            except:
                print("不可用ip：", ipport)
                continue


def getkxdaili():
    for i in range(1, 4705):
        req = requests.get("http://www.kxdaili.com/dailiip/1/"+str(i)+".html")
        html = req.text
        req.encoding = "utf-8"
        soup = BeautifulSoup(html, features="html.parser")
        iplist = soup.select('.hot-product-content tbody tr')
        for tag in iplist:
            try:
                ipport = tag.findAll('td')[0].text + ":" + tag.findAll('td')[1].text
                print(ipport)
                proxies["https"] = ipport
                rsp = requests.get(testProxyUrlHTTPS, proxies=proxies, timeout=5)
                print("wa!!!!!!!,找到一个！:", json.loads(rsp.text))
                # print(tag.findAll('td')[1].text)
            except:
                print("不可用ip：", ipport)
                continue

def testip():
    rsp = requests.get(testProxyUrl, proxies=proxies, timeout=5)
    print(json.loads(rsp.text))


if __name__ == '__main__':
    # get89Vip()
    # getOneAvailableProxyIP()
    getkxdaili()
    # testip()
    # req = requests.get("http://www.ip3366.net/free/?stype=1&page=2")
    # html = req.text
    # req.encoding = "utf-8"
    # soup = BeautifulSoup(html, features="html.parser")
    # iplist = soup.select('#list tbody tr')
    # for tag in iplist:
    #     print(tag.findAll('td')[0].text)
    #     print(tag.findAll('td')[1].text)



    # print("hello")
    # rsp = requests.get("https://www.89ip.cn/", proxies = proxies)
    # rsp = requests.get("https://www.proxy-list.download/api/v2/get?l=en&t=https")
    # json = json.loads(rsp.text)
    # total = int(json['TOTAL'])
    # for i in range(0, total-1):
    #     try:
    #
    #         ip = json['LISTA'][i]['IP']
    #         port = json['LISTA'][i]['PORT']
    #         proxies["http"] = ip + ":" + port
    #         proxies["https"] = ip + ":" + port
    #         rsp = requests.get(testProxyUrl, proxies=proxies, timeout = 5)
    #         print(json.load(rsp.text))
    #     except:
    #         print("ip不可用" + ip)
    #         continue
    #
    # print("ok")
    # print(json['origin'])




