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
import pandas as pd
# url = 'https://search.jd.com/Search?keyword=%E6%88%90%E4%BA%BA%E7%BA%B8%E5%B0%BF%E8%A3%A4&qrst=1&stock=1&page=1&s=1&click=0'

# url1 = 'https://www.baidu.com'
if __name__ == "__main__":
    data1={
        'productName': '1x',
        'shopName': '2y',
        'shopType': '3z',
        'productPrice': '4v'
    }
    data = ['fsaf','dafa','fasdfa','fadad']
    df1 = DataFrame(columns=('productName', 'shopName', 'shopType','productPrice'))
    # print(df1)
    df1.loc[0] = data
    print(df1)
    ds = pd.read_excel('product.xlsx')
    # print(ds)
    # ds.append(data,ignore_index=True)
    ds.append(df1)
    # print(ds)
    # ds.to_excel('product.xlsx')
    # browser = webdriver.Chrome('/Users/zhaoshuowen/Desktop/shuowen/others/chromedriver')
    # browser.get(url)
    # liElements = browser.find_element_by_tag_name('ul')
    # print(liElements.get(0))
    # browser.quit()
# headers = {
#     'User-Agent': get_headers()
# }
# result1 = requests.get(url,headers=headers).text
# soup1 = BeautifulSoup(result1, "html.parser")
# url2 = "https://item.jd.com/" + string(soup1.find_all('ul').children[num].attrs['data-sku']) + ".html"
# result2 = requests.get(url2, headers=headers).text
# soup2 = BeautifulSoup(result2, "html.parser")
# # 判断请求是否成功
# product.productName = soup2.find_all(class_ = 'sku-name').string
#
# product.shopName = soup2.find_all(class_='J-hove-wrap EDropdown fr').children.children.children.string
# if soup2.find_all(class_='u-jd') == None :
#     product.shopType = '0'
# else:
#     product.shopType = '1'
# product.price = soup2.find_all(class_='price J-p-5919939').string
# product.saleCount = soup2.find_all(class_='count J-comm-5919939').string



