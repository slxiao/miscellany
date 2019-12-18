#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import re

import requests
import json
from bs4 import BeautifulSoup as bs

def get_html():
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    headers = {'User-Agent' : user_agent}
    resp = requests.Session().get("https://world.taobao.com/", headers=headers)
    return bs(resp.content, "lxml")

def print_items(html):
    for i in html.find("script", "J_ContextData").children:
        for category in json.loads(i)["category"]:
            print("\n\n##%s" % (category["title"]))
            for child in filter(re.compile(r"child\d+").match, category.keys()):
                print("\n#%s" % category[child])
                for k in category[child.replace("child", "childList")]:
                    print(k["title"], end=" ")
    print("\n")

if __name__ == "__main__":
    print_items(get_html())