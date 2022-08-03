# coding=utf-8
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

# ##########################请求相关###################
# 防止被反爬虫,各种headers
def get_headers():
    useragent_list = [
        'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.9.2.1000 Chrome/39.0.2146.0 Safari/537.36',
        'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/532.3',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
    ]
    useragent = random.choice(useragent_list)
    header = {'User-Agent': useragent}
    return header



proxyArr = ["222.92.207.98:40080", "194.169.167.5:8080"]
# 代理
proxies = {
    "http": "",
    "https": ""
}
# 获取代理
def getProxy():
    index = int(random.random() * len(proxyArr))
    while proxyArr[index] == proxies["https"]:
        index = int(random.random() * len(proxyArr))
    proxies["https"] = proxyArr[index]
    proxies["http"] = proxyArr[index]




# 测试代理ip是否生效
testProxyUrl = "https://httpbin.org/ip"

# 查询appInfourl
appInfoUrl = "https://api.qimai.cn/andapp/info?{}"
appInfoContext = "/andapp/info"
# 查询appid的
bundleId2id = "https://api.qimai.cn/search/checkHasBundleId?{}"
bundleId2idContext = "/search/checkHasBundleId"

# market: 6 华为 8 vivo 3 vivo
# 请求入参， 查询bundle对应的appid
paramsForId = {
    "market": 8,
    "search": "com.xa.heard"
}
paramsForStatus = {
    "appid": 7522305,
    "market": 8
}




def getAppInfoFromAppIdAndMarket(appId, market):
    paramsForStatus["appid"] = appId
    paramsForStatus["market"] = market
    a = getAnalysis(paramsForStatus, appInfoContext)
    if a == None or a == "":
        return ""
    url = appInfoUrl.format(parse.urlencode(paramsForStatus)) + "&analysis=" + a
    print(url)
    getProxy()
    rsp = requests.get(testProxyUrl, proxies=proxies, timeout=5)
    print("当前代理ip:", json.loads(rsp.text))
    res = requests.get(url, headers=get_headers(), proxies = proxies)
    rsp = json.loads(res.text)
    if rsp["appInfo"] == None or rsp["appInfo"] == "":
        return ""
    return rsp["appInfo"]["is_online"]

def getAppIdFromBundle(bundleId, market):
    paramsForId["market"] = market
    paramsForId["search"] = bundleId
    a = getAnalysis(paramsForId, bundleId2idContext)
    if a == None or a == "":
        return ""
    url = bundleId2id.format(parse.urlencode(paramsForId)) + "&analysis=" + a
    # url = "https://www.qimai.cn/"
    print(url)
    getProxy()
    # 检验
    rsp = requests.get(testProxyUrl, proxies=proxies, timeout=5)
    print("当前代理ip:", json.loads(rsp.text))
    res = requests.get(url, headers=get_headers(), proxies = proxies)
    rsp = json.loads(res.text)
    return rsp["app_id"]

def getStatusByBundleAndMarket(bundleId, market):
    time.sleep(10 + 10 * random.random())
    appId = getAppIdFromBundle(bundleId, market)
    time.sleep(10 + 10 * random.random())
    if appId == "" or appId == None:
        return 0
    time.sleep(10 + 10 * random.random())
    status = getAppInfoFromAppIdAndMarket(appId, market)
    time.sleep(10 + 10 * random.random())
    return status

# 0000000c735d856

# OZ,加密算法，n可以是两种值
def encrypt(a: str, n="0000000c735d856"):
    s, n = list(a), list(n)
    sl = len(s)
    nl = len(n)
    for i in range(0, sl):
        s[i] = chr(ord(s[i]) ^ ord(n[(i + 10) % nl]))
    return html.unescape("".join(s))



# 获取反爬虫加密信息
def getAnalysis(params, context):
    # 计算时间差
    o = str(int((time.time() * 1000 - 1515125653845)))
    # 参数作为数组进行排序，之后转str，注意不能有analysis
    s = "".join(sorted([str(v) for v in params.values()]))
    # 将参数进行base64加密
    # s = base64.b64encode(bytes(s, encoding="ascii"))
    s = base64.b64encode(bytes(s, encoding="ascii"))
    # s += "@#".join([s.decode(), "/search/checkHasBundleId", t, "1"])
    s = s.decode() + "@#" + context
    s = s + "@#" + o
    s = s + "@#" + str(1)
    a = parse.quote(base64.b64encode(bytes(encrypt(s), encoding="ascii")))
    return a
    # s = base64.b64encode(bytes(encrypt(s), encoding="ascii"))
    # ewl2Q1RjBQZRZ0hcL1p1Qgd5CAtwEx9DVVFCAF8cVgxdVl14UUNyRV5UD1J6USQbBAIEAgkEAAkBUwYLdUcJ
    # ewl2Q1RjBQZRZ0hcL1p1Qgd5CAtwEx9DVVFCAF8cVgxdVl14UUNyRV5UD1J6USQbBAIEAgkJBgUAUQ8EdUcJ
    # ex5tTHtafUd%2BZFcNIxQcVApcVEZAH1leVl9wQAYHAVcJAAUIAggIAnATUg%3D%3D
    # paramsForStatus["analysis"] = a


def main():
    s = "{'code': 10000, 'msg': '成功', 'is_logout': 0, 'app_id': '6070976'}"
    data = json.loads(s)
    appid = data["app_id"]
if __name__ == '__main__':
    workbookr = xlrd.open_workbook(r'..\resource\resourceData.xls')
    sheet = workbookr.sheet_by_index(1)
    workbookw = xlwt.Workbook(encoding="utf-8")
    sheetw = workbookw.add_sheet("result", cell_overwrite_ok=True)
    # sheetw.write(0,0,"123")

    print(sheet.nrows)

    for i in  range(1, sheet.nrows):
        try:

            print("查询"+sheet.row_values(i)[0])
            bundleId = sheet.row_values(i)[0]
            appName =  sheet.row_values(i)[1]
            sheetw.write(i, 0, bundleId)
            sheetw.write(i, 1, appName)
            # 三种market查询
            statusXunfei = 0
            statusHuawei = getStatusByBundleAndMarket(bundleId, 6)
            print("statusHuawei:" + str(statusHuawei))
            if statusHuawei == 1:
                statusXunfei = 1
                sheetw.write(i, 2, statusHuawei)
                sheetw.write(i, 5, statusXunfei)
                continue

            statusVivo = getStatusByBundleAndMarket(bundleId, 8)
            print("statusVivo:" + str(statusVivo))
            if statusVivo == 1:
                statusXunfei = 1
                sheetw.write(i, 2, statusVivo)
                sheetw.write(i, 5, statusXunfei)
                continue

            statusYinyongBao = getStatusByBundleAndMarket(bundleId, 3)
            print("statusYinyongBao:" + str(statusYinyongBao))
            if statusYinyongBao == 1:
                statusXunfei = 1
                sheetw.write(i, 2, statusVivo)
                sheetw.write(i, 5, statusXunfei)
                continue

            # 到这里说明都是0
            # 写入excel
            sheetw.write(i, 2, 0)
            sheetw.write(i, 3, 0)
            sheetw.write(i, 4, 0)
            sheetw.write(i, 5, 0)
            # # 随机休眠,3秒内
            # time.sleep(3 + 2 * random.random())
        except:
            sheetw.write(i, 0, bundleId)
            sheetw.write(i, 1, appName)
            sheetw.write(i, 2, "error")
            sheetw.write(i, 3, "error")
            sheetw.write(i, 4, "error")
            sheetw.write(i, 5, "error")
            # 异常一定save一下
            workbookw.save(r'..\resource\resourceData1.xls')
            continue
    workbookw.save(r'..\resource\resourceData1.xls')

    # print(chr(14))
    # getAppInfoFromAppIdAndMarket(7522305, 8)
