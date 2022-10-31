from telnetlib import EC

from selenium import webdriver
import time
from openpyxl import load_workbook, Workbook
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

# options = webdriver.FirefoxOptions()
# options.set_headless(True)
# options.add_argument("--headless")  # 设置火狐为headless无界面模式
# options.add_argument("--disable-gpu")
# d = webdriver.Firefox(options=options)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# d = webdriver.Firefox()
d = webdriver.Chrome()


# d.implicitly_wait(5)


def rw():
    time.sleep(1)


def dl(d):
    # d.window_handles()
    d.get('https://jiaobenwang.com/')
    # WebDriverWait(d, time).until(EC.visibility_of_element_located((By.CLASS_NAME, 'visible_long_after_loading_only')))

    d.find_element_by_xpath('/html/body/div[11]/div/div[1]/button').click()

    # d.switch_to(d.window_handles[1])
    # for handle in d.window_handles:  # 方法二，始终获得当前最后的窗口，所以多要多次使用
    #     d.switch_to_window(handle)

    # input()
    rw()

    d.find_element_by_xpath('//*[@id="navHeight"]/div/div/div[4]/div[1]').click()

    rw()
    d.find_element_by_xpath('//*[@id="login"]/div/form/div[1]/input').send_keys('sch1532694569c@163.com')

    rw()
    d.find_element_by_xpath(
        '//*[@id="login"]/div/form/div[2]/input').send_keys('123456789c')
    rw()
    d.find_element_by_xpath(
        '//*[@id="login"]/div/form/button').click()

    time.sleep(5)

    d.find_element_by_xpath(
        '/html/body/div[3]/ul/li[1]/a/span').click()

    time.sleep(3)
    ax = d.find_element_by_xpath('//*[@id="swal2-title"]').text
    print(ax)
    return ax

    # 鼠标悬停
    # # 1、先定位到需要悬停的元素
    # mte = d.find_element(By.CSS_SELECTOR, '.swal2-confirm')
    #
    # # 2、实现鼠标悬停 导入 from selenium.webdriver import ActionChains
    # # ActionChains(浏览器).move_to_element(需要悬停的元素).perform()
    # ActionChains(d).move_to_element(mte).perform()
    #
    # time.sleep(3)  # 悬停之后，最好等待1s中，悬停过程中，放下鼠标键盘
    #
    # # 3、点击悬停后 出现的元素
    # d.find_element(By.LINK_TEXT, '.swal2-confirm').click()


ax = dl(d)
while ax != '今日已签到，请明日再来':
    d.quit()
    d = webdriver.Chrome
    ax = dl(d)
