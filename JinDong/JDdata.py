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


# 创建表格
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("product")

# 行号,互斥
num = 0
mutex = Lock()


# 将product对象写到第row行
def write2excel(product, row):
    sheet.write(row, 0, product.productName)
    sheet.write(row, 1, product.shopName)
    sheet.write(row, 2, product.shopType)
    sheet.write(row, 3, product.price)
    sheet.write(row, 4, product.saleCount)

url = 'https://search.jd.com/Search?keyword=%E6%88%90%E4%BA%BA%E7%BA%B8%E5%B0%BF%E8%A3%A4&enc=utf-8&wq=%E6%88%90%E4%BA%BA%E7%BA%B8%E5%B0%BF%E8%A3%A4'
def requestData():
    # 声明chrome驱动
    options = webdriver.ChromeOptions()
    options.add_argument('user-agent='+get_headers())
    browser = webdriver.Chrome(options=options)
    while True :
        global num
        # 获取行号
        mutex.acquire()  # 上锁
        num += 1
        if num == 30:
            #  下滑
            js = "var q=document.getElementById('shortcut-2014').scrollTop=1000"
            browser.execute_script(js)
            time.sleep(random.randint(1, 3))
        if num == 60:
            # 点击下一页，num置0
            browser.find_element_by_class_name('pn-next').click()
            time.sleep(random.randint(1, 3))
            num = 0
        mutex.release()  # 释放锁



        # 请求
        browser.get(url)
        liElements = browser.find_element_by_class_name("gl-warp clearfix").find_element_by_tag_name('li')
        code = liElements[num].getAttribute('data-sku')
        browser.get("https://item.jd.com/" + code + ".html")
        productName = browser.find_element_by_class_name('sku-name').text
        product = Product()
        product.productName = browser.find_element_by_class_name('sku-name').getText()
        product.shopName = browser.find_element_by_class_name('J-hove-wrap EDropdown fr').find_element_by_tag_name('a').getText()
        if browser.find_element_by_class_name('u-jd') == None :
            product.shopType = '0'
        else:
            product.shopType = '1'
        product.price = browser.find_element_by_class_name('summary-price J-summary-price').find_element_by_class_name('p-price')[1].getText()
        product.saleCount = browser.find_element_by_id('comment-count').find_element_by_tag_name('a').getText()

        # 写入
        write2excel(product, num)
        # 写一行保存一行
        workbook.save('productInfo.xls')

if __name__ == "__main__":
    # 创建线程
    t1 = Thread(target=requestData)
    t2 = Thread(target=requestData)
    t3 = Thread(target=requestData)
    t4 = Thread(target=requestData)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    # 所有线程结束之后保存到productInfo.xls中
    t1.join()
    t2.join()
    t3.join()
    t4.join()
