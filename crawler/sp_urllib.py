# -*- coding: utf-8 -*-

"""
通过urllib爬取

Author: ainoob.cn
Email: 535334234@qq.com
"""

from urllib.error import URLError
from urllib.request import urlopen
import ssl
from lxml import etree


# 通过指定的字符集对页面进行解码(不是每个网站都将字符集设置为utf-8)
def decode_page(page_bytes, charsets=('utf-8',)):
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
            # logging.error('Decode:', error)
    return page_html


# 获取页面的HTML代码(通过递归实现指定次数的重试操作)
def get_page_html(seed_url, *, retry_times=3, charsets=('utf-8',)):
    print('--', seed_url)
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(), charsets)
    except URLError:
        # logging.error('URL:', error)
        if retry_times > 0:
            return get_page_html(seed_url, retry_times=retry_times - 1,
                                 charsets=charsets)
    return page_html


# 从页面中提取需要的部分
def get_matched_parts(page_html, xpath_str):
    links = etree.HTML(page_html).xpath(xpath_str)
    return links


# 开始执行爬虫程序
def start_crawl(seed_url, match_pattern, *, max_depth=-1):
    url_list = [seed_url]
    visited_url_list = {seed_url: 0}
    while url_list:
        current_url = url_list.pop(0)
        depth = visited_url_list[current_url]
        if depth != max_depth:
            page_html = get_page_html(current_url, charsets=('utf-8', 'gbk', 'gb2312'))
            links_list = get_matched_parts(page_html, match_pattern)
            for link in links_list:
                link = 'https:'+link
                if link not in visited_url_list:
                    visited_url_list[link] = depth + 1
                    page_html = get_page_html(link, charsets=('utf-8', 'gbk', 'gb2312'))
                    headings = get_matched_parts(page_html, '//div[@class="text-title"]/h1/text()')
                    if headings:
                        heading = headings[0].replace(' ','').replace('\n','')
                        print(heading, link)


def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl('https://sports.sohu.com/s/nba',
                '//ul[@class="news-list first"]/li/a/@href',
                max_depth=2)


if __name__ == '__main__':
    main()
