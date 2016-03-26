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
f = u'不再'
s = u'一个'
y = u'两个'
z = u'三个'
tieba_name = raw_input(u'请输入贴吧名称：\n').decode('utf-8')
xuanze_zhuti = raw_input(u'请选择主题：\n').decode('utf-8')
xuanze_tuce = raw_input(u'请选择图册：\n').decode('utf-8')
def path(f,s,y):
	dir_name=os.path.join(f,s)
	if not os.path.exists(dir_name):
		os.makedirs(dir_name)
	else:
		pass
	dir_name2 = os.path.join(dir_name,y)
	if not os.path.exists(dir_name2):
		os.makedirs(dir_name2)
	else:
		pass

path(tieba_name,xuanze_zhuti,xuanze_tuce)
