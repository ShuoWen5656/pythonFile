# coding=utf-8
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from threading import Thread,Lock
import xlwt
import random
import string
from selenium.webdriver.common.by import By
import time
from pandas import DataFrame
# encoding: utf-8
# from pandas import DataFrame




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


# 商品类
class Product():
    # 店铺名称
    shopName = ''
    # 商品名称
    productName = ''
    # 店铺类型
    shopType = ''
    # 商品价格
    price = ''
    # 商品销量
    saleCount = ''


shopName = []
productName = []
shopType = []
productPrice = []

if __name__ == "__main__":
    # 创建表格
    # workbook = xlwt.Workbook(encoding='utf-8')
    # sheet = workbook.add_sheet("product")
    # list = []
    # url = 'https://search.jd.com/Search?keyword=%E6%88%90%E4%BA%BA%E7%BA%B8%E5%B0%BF%E8%A3%A4&enc=utf-8&wq=%E6%88%90%E4%BA%BA%E7%BA%B8%E5%B0%BF%E8%A3%A4'
    # headers = {
    #     'User-Agent': get_headers().get('User-Agent')
    # }
    # result1 = requests.get(url,headers=headers).text
    # # print(result1)
    # soup1 = BeautifulSoup(result1, "html.parser")
    for i in range(1,20):
        list = []
        url = 'https://search.jd.com/Search?keyword=%E6%88%90%E4%BA%BA%E7%BA%B8%E5%B0%BF%E8%A3%A4&qrst=1&stock=1&page='+str(i)+'&s=1&click=0'
        headers = {
            'User-Agent': get_headers().get('User-Agent')
        }
        result1 = requests.get(url, headers=headers).text
        # print(result1)
        soup1 = BeautifulSoup(result1, "html.parser")
        for i in range(30):
            product = Product()
            if soup1.find(class_='gl-warp clearfix').find_all('li')[i].find(class_='skcolor_ljg') != None:
                product.productName = soup1.find(class_='gl-warp clearfix').find_all('li')[i].find(
                    class_='skcolor_ljg').parent.text
            else:
                product.productName = '未获取'
            # print(product.productName)
            product.shopName = soup1.find(class_='gl-warp clearfix').find_all('li')[i].find(class_='curr-shop hd-shopname').text
            # print(product.shopName)
            if soup1.find(class_='gl-warp clearfix').find_all('li')[i].find(class_='goods-icons J-picon-tips J-picon-fix') == None :
                product.shopType = '0'
                # print(soup1.find(class_='gl-warp clearfix').find_all('li')[i].find(class_='goods-icons J-picon-tips J-picon-fix').text)
            else:
                product.shopType = '1'
                # print(soup1.find(class_='gl-warp clearfix').find_all('li')[i].find(class_='goods-icons J-picon-tips J-picon-fix').text)
            product.price = soup1.find(class_='gl-warp clearfix').find_all('li')[i].find(class_='J_'+soup1.find(class_='gl-warp clearfix').find_all('li')[i].attrs['data-sku']).contents[2].text
            # product.saleCount = soup1.find(id='J_comment_'+soup1.find(class_='gl-warp clearfix').find_all('li')[i].attrs['data-sku']).parent
            # print(product.saleCount)
            # get请求获取销量等数据
            url = 'https://club.jd.com/comment/productCommentSummaries.action'
            headers = {
                'User-Agent': get_headers().get('User-Agent')
            }
            data = {
                'referenceIds': '940582',  # 商品编号
                'callback': 'jQuery4865013',  # 需要获取
                '_': '1606390141281'  # 需要获取
            }
            result1 = requests.get(url, headers=headers, params=data).text
            soup1 = BeautifulSoup(result1, "html.parser")
            # soup = 'jQuery4865013({"CommentsCount":[{"SkuId":940582,"ProductId":940582,"ShowCount":64135,"ShowCountStr":"6.4万+","CommentCountStr":"213万+","CommentCount":2136947,"AverageScore":5,"DefaultGoodCountStr":"155万+","DefaultGoodCount":1554916,"GoodCountStr":"117万+","GoodCount":1170490,"AfterCount":6634,"OneYear":0,"AfterCountStr":"6600+","VideoCount":2005,"VideoCountStr":"2000+","GoodRate":0.99,"GoodRateShow":99,"GoodRateStyle":148,"GeneralCountStr":"2700+","GeneralCount":2780,"GeneralRate":0.009,"GeneralRateShow":1,"GeneralRateStyle":2,"PoorCountStr":"1700+","PoorCount":1700,"SensitiveBook":0,"PoorRate":0.001,"PoorRateShow":0,"PoorRateStyle":0}]});'
            want = 'ShowCountStr'
            print(soup1)
            soup1 = str(soup1)
            print(soup1.index(want))
            # print(soup[34])
            print(soup1.index(':', soup1.index(want)))
            print(soup1.index(',', soup1.index(want)))
            print(soup1[soup1.index(':', soup1.index(want)) + 1: soup1.index(',', soup1.index(want))])
            # print(soup1)
            # print(type(soup1))
            # list.append(soup1.find(class_='gl-warp clearfix').find_all('li')[i].attrs['data-sku'])

        # for j in range(30):
        #     print(list[j])
        #     url1 = 'https://item.jd.com/'+list[j]+'.html'
            # print(url1)
            # result2 = requests.get(url1, headers=headers).text
            # soup2 = BeautifulSoup(result1, "lxml")
            # time.sleep(2)
            # print(result2)
            # product = Product()
            # product.productName = soup2.find_all('div',class_='sku-name')
            # print(product.productName)
            # product.shopName = soup2.find(class_='J-hove-wrap EDropdown fr').contents[0].contents[0].contents[0].attrs['title']
            # print(product.shopName)
            # if soup1.find_all(class_='u-jd') == None :
            #     product.shopType = '0'
            # else:
            #     product.shopType = '1'
            # product.price = soup2.find_all(class_='price J-p-'+list[j]).string
            # product.saleCount = soup2.find_all(class_='count J-comm-'+list[j]).string
            # print(soup1.find(class_='gl-warp clearfix').find_all('li')[0].attrs['data-sku'])
            shopName.append(product.shopName)
            productName.append(product.productName)
            shopType.append(product.shopType)
            productPrice.append(product.price)

        # sheet.write(i, 0, string(product.productName))
        # sheet.write(i, 1, string(product.shopName))
        # sheet.write(i, 2, string(product.shopType))
        # sheet.write(i, 3, string(product.price))
        # sheet.write(j, 4, product.saleCount)
    # workbook.save('productInfo.xls')


    data={
        'productName':productName,
        'shopName': shopName,
        'shopType': shopType,
        'productPrice': productPrice
    }
    df = DataFrame(data)
    df.to_excel("product.xlsx")
    # print(result1)
    # sheet.write(row, 0, product.productName)
    # sheet.write(row, 1, product.shopName)
    # sheet.write(row, 2, product.shopType)
    # sheet.write(row, 3, product.price)
    # sheet.write(row, 4, product.saleCount)

# 100003020756,940582,5919939,1055620391,5968356,15966569875,5481090,2567497,2567493,100006795751,1055620981,1417900835,1005130985,1005132412,10718636760,11062433548,1417911415,10783181556,61015697932,10513961884,100009345059,538727,10319308993,10095481600,24863034548