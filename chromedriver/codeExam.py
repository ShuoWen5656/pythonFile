
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def check(param):
    ps = param.split('#')
    if ps.__contains__('A'):
        return True


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('www.baidu.com')


    # 登录，等待某个元素出现
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.ID, "account"))
    driver.find_element(by=By.ID, value='account').send_keys("xxxx")
    driver.find_element(by=By.ID, value='password').send_keys("xxxx")

    # 点击按钮
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.CLASS_NAME, "btnxxx"))
    driver.find_element(by=By.CLASS_NAME, value='btnxxx').send_keys("xxxx")

    i = 0
    for i in range(10):
        # 取出元素文案
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.CLASS_NAME, "btnxxx"))
        text = driver.find_element(by=By.CLASS_NAME, value='btnxxx').text

        if text != None:
            continue
        elif text == 'xxx':
            continue
        else:
            continue

    sleep(200)
    driver.quit()


