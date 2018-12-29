#!/usr/bin/env python3

import argparse
import logging
import urllib
import requests
from bs4 import BeautifulSoup
import random


log = logging.getLogger(__name__)

proxies = {}


class ProgressBar(object):
    
    def __init__(self):
        pass


def pick_proxy():
    content = request.urlopen(
        "http://www.proxynova.com/proxy-server-list/country-cn/").read()
    soup = BeautifulSoup(content, 'lxml')
    all_proxies = []
    for row in soup.find_all('tr')[1:]:
        try:
            ip = row.find_all('span')[0].text.strip() + row.find_all('span')[1].text.strip()
            port = row.find_all('a')[0].text.strip()
            if not port in ['80', '3128', '8080']:
                continue
            cur_proxy = "{}:{}".format(ip, port)
            all_proxies.append(cur_proxy)
        except:
            pass

    if not len(all_proxies):
        raise AssertionError('No chinese proxy is valid，Please use -x or -s option instead!')
    return random.choice(all_proxies)


def download_images():
    pass

def get_html():
    pass

def main(starturl: str):
    urlparsed = urllib.parse.urlparse(starturl)

    

if __name__ == "__main__":
    main(starturl="http://f.91p08.space/forumdisplay.php?fid=19")
