import chromedriver_binary

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import requests
from bs4 import BeautifulSoup

import pandas as pd

import time
import tqdm

def get_title_txt(driver):
    titles_elements = driver.find_elements(by=By.XPATH, value="//a/span[@class='img']/img")

    titles = []

    for e in titles_elements:
        time.sleep(400/1000)
        title = e.get_attribute("alt")
        titles.append(title)

    return titles

def main():
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument('--start-maximized')
    options.add_argument('--headless')

    driver = webdriver.Chrome(chrome_options=options)

    url = 'https://www.dmm.co.jp/digital/videoa/-/list/=/sort=ranking/'
    driver.get(url)

    time.sleep(5)

    element = driver.find_element(by=By.LINK_TEXT, value="はい").click()

    titles = []

    # 最大10ページまでとする
    for page in tqdm.tqdm(range(1, 51)):
        url = url +'page='+str(page)+'/'
        driver.get(url)
        time.sleep(1)
        titles.extend(get_title_txt(driver))

    df = pd.DataFrame({'titles':titles})
    df.to_csv('./titles.csv', index=False)

    driver.quit()


if __name__=='__main__':
    main()