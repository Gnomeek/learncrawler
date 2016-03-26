# -*- coding:utf-8 -*-
import requests, json
from bs4 import BeautifulSoup
import os
import os.path
import urllib2,urllib

global s
s = requests.session()
def get_soup(url):
	#soup一下
    h = s.get(url)
    html = h.content
    soup = BeautifulSoup(html,"html.parser")
    return soup

def path(f,z,y):
	dir_name=os.path.join(f,z)
	if not os.path.exists(dir_name):
		print u'---正在创建目录\"'+z+'\"---'
		os.makedirs(dir_name)
	else:
		pass
	dir_name2 = os.path.join(dir_name,y)
	if not os.path.exists(dir_name2):
		print u'---正在创建目录\"'+y+'\"---'
		os.makedirs(dir_name2)
	else:
		pass

def pic_download(pic_address,tieba_name,xuanze_zhuti,xuanze_tuce):
	i = 1
	for pic in pic_address:
		pic1 = pic[:30]
		pic2 = pic[-44:]
		new_pic = pic1+'pic/item/'+pic2   #获得高清图地址
		filename = str(i)+'.jpg'
		print 'Downloading '+filename + '......'
		urllib.urlretrieve(new_pic,'./'+tieba_name+'/'+xuanze_zhuti+'/'+xuanze_tuce+'/'+filename)
		i += 1

def get_zhuti_neirong(main_url):
	#得到1，主题名；2，主题url；3，某主题图册数
	zhuti_neirong = []
	soup =get_soup(main_url)
	zhuti_tag = soup.find_all('div',class_="grbh_left")
	for item in zhuti_tag:
		yige_zhutiming = item.a.text
		yige_zhutiurl = item.a['href']
		yige_tuceshu = item.span.text
		zhuti_neirong.append([yige_zhutiming,yige_zhutiurl,yige_tuceshu])
	return zhuti_neirong
	
def get_tuce_neirong(zhuti_url):
	#得到1，图册名；2，图册id；3，某图册中图片个数
	tuce_neirong = []
	soup = get_soup(zhuti_url)
	tuce_tag = soup.find_all('div',class_="grbm_ele_wrapper")
	for item in tuce_tag:
		yige_tuceming = item.div.a.text
		if yige_tuceming[-3:] == '...':
			yige_tuceming = yige_tuceming[:-3]
		yige_tuceid = item.a['href']
		yige_tupiangeshu = item.span.text
		tuce_neirong.append([yige_tuceming,yige_tuceid,yige_tupiangeshu])
	return tuce_neirong

def get_pic_address(json_url):
	pic_addres = []
	h = s.get(json_url)
	html = h.content.decode('unicode-escape')
	target = json.loads(html)
	for item in target['data']['pic_list']:
		pic_addres.append(item['purl'])
	return pic_addres

def main():

	tieba_name = raw_input(u'请输入贴吧名称：\n').decode('utf-8')
	main_url = 'http://tieba.baidu.com/photo/g?kw=' + tieba_name + '&ie=utf-8'
	zhuti = get_zhuti_neirong(main_url)
	#print zhuti
	for yigezhuti in zhuti:
		print yigezhuti[0] + '   ' + yigezhuti[2] + u'个图册'
	xuanze_zhuti = raw_input(u'请选择主题：\n').decode('utf-8')
	for yigezhuti in zhuti:
		#print yigezhuti
		if xuanze_zhuti == yigezhuti[0]:
			add_url = yigezhuti[1]
	#print add_url[10:]
	#else:
		#print u'主题输入错误，请重新输入：\n'
	zhuti_url = 'http://tieba.baidu.com/photo/g?kw=' + tieba_name + '&ie=utf-8&cat_id='+ str(add_url[10:])
	tuce = get_tuce_neirong(zhuti_url)
	#print tuce
	for yigetuce in tuce:
		print yigetuce[0] + '   ' + yigetuce[2] + u'图片'
	xuanze_tuce = raw_input(u'请选择图册：\n').decode('utf-8')
	for yigetuce in tuce:
		if xuanze_tuce == yigetuce[0]:
			tid = yigetuce[1]
			pe = yigetuce[2][:-1]
	#print tid，pe[:-1]
	json_url = 'http://tieba.baidu.com/photo/g/bw/picture/list?kw='+tieba_name+'&alt=jview&rn=200&tid='+str(tid[3:])+'&pn=1&ps=1&pe='+str(pe)+'&info=1'
	#print json_url
	pic_address = get_pic_address(json_url)
	#print  pic_address
	path(tieba_name,xuanze_zhuti,xuanze_tuce)
	pic_download(pic_address,tieba_name,xuanze_zhuti,xuanze_tuce)

if __name__=='__main__':
	main()
