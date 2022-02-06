#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from urllib import request
import chardet


def decoding_method(url):
    return chardet.detect(request.urlopen(url).read())["encoding"]


if __name__ == "__main__":
    response = request.urlopen(
        "https://s.taobao.com/search?q=%E4%B8%80%E5%8A%A06%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180721&ie=utf8"
    )
    html = response.read()
    charset = chardet.detect(html)  # detect the encoding method of the website.
    html = html.decode(charset["encoding"])  # decode the html file.
    print(html)
