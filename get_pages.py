#!/usr/bin/env python

import requests
from lxml import html
import codecs


def helper_fields(html_text):
    tree = html.fromstring(html_text)
    ids = ['__VIEWSTATE', '__EVENTVALIDATION']
    result = {id: tree.xpath('//input[@id="'+id+'"]/@value')[0]
              for id in ids}
    result['__EVENTARGUMENT'] = ''
    return result

URL = 'http://www.cjccresourcelocator.net/ResourceLocator/List.aspx'
base = requests.get(URL)
params = helper_fields(base.text)
params['__EVENTTARGET'] = 'ctl00$ContentPlaceHolder1$lnk1'

x = requests.post(URL, params)
with codecs.open('test.html', 'w', 'utf-8') as f:
    f.write(x.text)
