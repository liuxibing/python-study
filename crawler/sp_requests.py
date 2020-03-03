# -*- coding: utf-8 -*-

"""
通过requests爬取网页

Author: ainoob.cn
Email: 535334234@qq.com
"""

from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import re


def main():
    # 通过requests第三方库的get方法获取页面
    headers = {'user-agent': 'Baiduspider'}
    proxies = {
        'http': 'http://122.114.31.177:808'
    }
    base_url = 'https://www.zhihu.com/'
    seed_url = urljoin(base_url, 'explore')
    resp = requests.get(seed_url,
                        headers=headers,
                        proxies=proxies)
    # 对响应的字节串(bytes)进行解码操作(搜狐的部分页面使用了GBK编码)
    # html = resp.content.decode('gbk')
    html = resp.content
    # 创建BeautifulSoup对象来解析页面(相当于JavaScript的DOM)
    bs = BeautifulSoup(html, 'lxml')
    soup = BeautifulSoup(resp.text, 'lxml')
    href_regex = re.compile(r'^/question')
    link_set = set()
    # 通过CSS选择器语法查找元素并通过循环进行处理
    for a_tag in soup.find_all('a', {'href': href_regex}):
        if 'href' in a_tag.attrs:
            # 通过attrs属性(字典)获取元素的属性值
            href = a_tag.attrs['href']
            full_url = urljoin(base_url, href)
            link_set.add(full_url)
            print(full_url)
    print('Total %d question pages found.' % len(link_set))



if __name__ == '__main__':
    main()
