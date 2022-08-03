# coding=utf-8
import requests
from urllib import parse
import json
import base64
import xlwt
import random
import string
import time
# 防止被反爬虫
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


# 请求入参， search
params = {
    "market": 8,
    "search": "com.xa.heard"
}

# paramstem = {
#
# }

# 0000000c735d856

# OZ,加密算法，n可以是两种值
def encrypt(a:str, n="0000000c735d856"):
    s, n = list(a), list(n)
    sl = len(s)
    nl = len(n)
    for i in range(0, sl):
        s[i] = chr(ord(s[i]) ^ ord(n[(i+10)%nl]))
    return "".join(s)




def main():
    # 计算时间差
    o = str(int((time.time() * 1000 - 1515125653845)))
    # 参数作为数组进行排序，之后转str，注意不能有analysis
    s = "".join(sorted([str(v) for v in params.values()]))
    # 将参数进行base64加密
    # s = base64.b64encode(bytes(s, encoding="ascii"))
    s = base64.b64encode(bytes(s, encoding="ascii"))
    # s += "@#".join([s.decode(), "/search/checkHasBundleId", t, "1"])
    s = s.decode() + "@#" + "/search/checkHasBundleId"
    s = s + "@#" + o
    s = s + "@#" + str(1)
    a = parse.quote(base64.b64encode(bytes(encrypt(s), encoding="ascii")))
    # s = base64.b64encode(bytes(encrypt(s), encoding="ascii"))
    # ewl2Q1RjBQZRZ0hcL1p1Qgd5CAtwEx9DVVFCAF8cVgxdVl14UUNyRV5UD1J6USQbBAIEAgkEAAkBUwYLdUcJ
    # ewl2Q1RjBQZRZ0hcL1p1Qgd5CAtwEx9DVVFCAF8cVgxdVl14UUNyRV5UD1J6USQbBAIEAgkJBgUAUQ8EdUcJ
    params["analysis"] = a
    url = "https://api.qimai.cn/search/checkHasBundleId?{}".format(parse.urlencode(params))
    # url = "https://www.qimai.cn/"
    print(url)
    res = requests.get(url, headers = get_headers())
    rsp = json.loads(res.text)
    print(rsp)



if __name__ == '__main__':
    main()
