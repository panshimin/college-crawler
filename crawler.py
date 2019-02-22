# -*- coding: utf-8 -*-
import os
import requests
import logging
from lxml import html
from requests import urllib3

headers = {
    'Host': 'www.zhihu.com',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'Connection': 'keep-alive',
    # 'accept-encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}


def save(text, filename='temp', path='download'):
    fpath = os.path.join(path, filename)
    with open(fpath, 'wb') as f:
        print('output:', fpath)
        f.write(text)


def save_image(image_url):
    print('image_url :', image_url)
    urllib3.disable_warnings()
    resp = requests.get(image_url, verify=False)
    page = resp.content
    filename = image_url.split('zhimg.com/')[-1]
    save(page, filename)


def crawl(url):
    urllib3.disable_warnings()
    resp = requests.get(url, headers=headers, verify=False)
    page = resp.content
    root = html.fromstring(page)
    image_urls = root.xpath('//img[@src]/@src')
    for image_url in image_urls:
        if image_url.startswith('http') or image_url.startswith('https'):
            save_image(image_url)


if __name__ == '__main__':
    url = 'https://www.zhihu.com/question/27364360'
    crawl(url)
