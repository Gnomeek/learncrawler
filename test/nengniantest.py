# -*- coding:utf8 -*-
import requests
import json
s = requests.session()
Vote_url =  ''
h = s.get(Vote_url)
html = h.content.decode('unicode-escape')
print html
target = json.loads(html)
#print target['data']['pic_list'][0]['purl']
#http:www.zhihu.com/answer/45872347/voters_profile