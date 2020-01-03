from __future__ import print_function

import re

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_browser(webdriver_path):
    browser_options = Options()
    browser_options.add_argument("--headless")
    browser_options.add_argument('--no-sandbox')
    return webdriver.Chrome(webdriver_path, chrome_options=browser_options)

def print_items():
    browser = create_browser('/usr/bin/chromedriver')
    browser.get("https://world.taobao.com/")
    html = bs(browser.page_source, "lxml")

    for cat in html.find_all("div", re.compile("cat cat-\d+")):
        for items in cat.find_all("div", re.compile("cat-con-child cat-child-\d+")):
            for item in items.find_all("a"):
                print(item.text, end=" ")

if __name__ == "__main__":
    print_items()