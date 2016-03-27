# -*- coding:utf8 -*-
import requests
import json
import urllib
from bs4 import BeautifulSoup
import os
import os.path
'''
s = u'http://imgsrc.baidu.com/forum/w%3D413/sign=7522310e79310a55c424dff584444387/f17c034e251f95ca53dc394bc9177f3e6609529c.jpg'

s1 = s[:30]
s2 = s[-44:]
new_s = s1+'pic/item/'+s2
print new_s
i = 1
'''

def check_xuanze_zhuti(xuanze_zhuti,zhuti):
	add_url = ''
	for yigezhuti in zhuti:
		#print yigezhuti
		if xuanze_zhuti == yigezhuti[0]:
			add_url = yigezhuti[1]
	if add_url == '':
		print u'该主题不存在，请重新输入。\n'
		xuanze_zhuti = raw_input(u'请选择主题：\n').decode('utf-8')
		check_xuanze_zhuti(xuanze_zhuti,zhuti)
	return add_url

