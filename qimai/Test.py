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
# from xlutils.copy import copy
import random
from threading import Thread,Lock,Semaphore
from bs4 import BeautifulSoup
from qimai import GlobalPost

semaphore = Semaphore(1)

availableIP = ""

testProxyUrl = "http://httpbin.org/ip"
testProxyUrlHTTPS = "https://httpbin.org/ip"

proxies = {
    "http": "60.170.204.30:8060",
    "https": "103.23.20.68:80"
}



# 获取一个可用的ip地址
def getOneAvailableProxyIP():
    for i in  range(1, 8):
        try:
            req = requests.get("http://www.ip3366.net/free/?stype=1&page=" + str(i), timeout=5)
            html = req.text
            req.encoding = "utf-8"
            soup = BeautifulSoup(html, features="html.parser")
            iplist = soup.select('#list tbody tr')
            for tag in iplist:
                try:
                    if availableIP != "":
                        return
                    ipport = tag.findAll('td')[0].text+":"+tag.findAll('td')[1].text
                    print(ipport)
                    proxies["https"] = ipport
                    rsp = requests.get(testProxyUrlHTTPS, proxies=proxies, timeout=5)
                    print("wa!!!!!!!,找到一个！:",json.loads(rsp.text))
                    # print(tag.findAll('td')[1].text)
                    GlobalPost.append(ipport)
                    print("#####当前ip可用列表：############3")
                    GlobalPost.printList()
                    print("###############################3")
                except:
                    print("不可用ip：", ipport + "   " , end="")
                    continue
        except:
            continue
        finally:
            if i == 8:
                i = 1

# get89VIP
def get89Vip():
    global availableIP
    for i in  range(1, 7):
        try:
            req = requests.get("https://www.89ip.cn/index_"+ str(i) +".html", timeout=5)
            html = req.text
            req.encoding = "utf-8"
            soup = BeautifulSoup(html, features="html.parser")
            iplist = soup.select('.layui-table tbody tr')
            for tag in iplist:
                try:
                    if availableIP != "":
                        return
                    ipport = tag.findAll('td')[0].text.replace("\t", "").replace("\n", "")+":"+tag.findAll('td')[1].text.replace("\t", "").replace("\n", "")
                    print(ipport)
                    proxies["https"] = ipport
                    rsp = requests.get(testProxyUrlHTTPS, proxies=proxies, timeout=5)
                    print("wa!!!!!!!,找到一个！:",json.loads(rsp.text))
                    # print(tag.findAll('td')[1].text)
                    GlobalPost.append(ipport)
                    print("#####当前ip可用列表：############3")
                    GlobalPost.printList()
                    print("###############################3")
                except:
                    print("不可用ip：", ipport + "   ", end="")
                    continue
        except:
            continue
        finally:
            if  i == 7:
                i = 1

def getKuaidaili():
    for i in  range(1, 4705):
        try:
            req = requests.get("https://free.kuaidaili.com/free/inha/"+ str(i) +"/", timeout=5)
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
                        GlobalPost.append(ipport)
                        print("#####当前ip可用列表：############3")
                        GlobalPost.printList()
                        print("###############################3")
                    # print(tag.findAll('td')[1].text)
                except:
                    print("不可用ip：", ipport + "   ", end="")
                    continue
        except:
            continue
        finally:
            if  i == 20:
                i = 1

def getkxdaili():
    global availableIP
    for i in range(1, 4705):
        try:
            req = requests.get("http://www.kxdaili.com/dailiip/1/"+str(i)+".html", timeout=5)
            html = req.text
            req.encoding = "utf-8"
            soup = BeautifulSoup(html, features="html.parser")
            iplist = soup.select('.hot-product-content tbody tr')
            for tag in iplist:
                try:
                    if availableIP != "":
                        return
                    ipport = tag.findAll('td')[0].text + ":" + tag.findAll('td')[1].text
                    print(ipport)
                    proxies["https"] = ipport
                    rsp = requests.get(testProxyUrlHTTPS, proxies=proxies, timeout=5)
                    print("wa!!!!!!!,找到一个！:", json.loads(rsp.text))
                    GlobalPost.append(ipport)
                    print("#####当前ip可用列表：############3")
                    GlobalPost.printList()
                    print("###############################3")
                    # print(tag.findAll('td')[1].text)
                except:
                    print("不可用ip：", ipport + "   ", end="")
                    continue
        except:
            continue
        finally:
            if  i == 20:
                i = 1

def getAvailableIP():
    # global availableIP
    # 每次获取之前清空
    # availableIP = ""
    t4 = Thread(target=getKuaidaili)
    t3 = Thread(target=get89Vip)
    t1 = Thread(target=getkxdaili)
    t2 = Thread(target=getOneAvailableProxyIP)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # while availableIP == "":
    #     None
    # availableIP = getOneAvailableProxyIP()
    return availableIP



def testip():
    rsp = requests.get(testProxyUrl, proxies=proxies, timeout=5)
    print(json.loads(rsp.text))


if __name__ == '__main__':
    a = getAvailableIP()
    print(a)

    # t4 = Thread(target=getKuaidaili)
    # t3 = Thread(target=get89Vip)
    # t1 = Thread(target=getkxdaili)
    # t2 = Thread(target=getOneAvailableProxyIP)
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # get89Vip()
    # getOneAvailableProxyIP()
    # getkxdaili()




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




