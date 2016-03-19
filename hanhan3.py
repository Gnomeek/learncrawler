# -*- coding:utf-8 -*-
import urllib2
import time

links = ['']*7
n = 0
page = 0
while n < 7:
	links[n] = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_'+str(n+1)+'.html'
	n += 1
while page < 7:
	content = urllib2.urlopen(links[page]).read()
	url = ['']*100
	filename = ['']*100
	i = 0

	set_local = content.find(r'<a title')
	start = content.find(r'href',set_local)
	end = content.find(r'html',start)
#for_filename1 = content.find(r'>',end)
#for_filename2 = content.find(r'</a',end)


	while set_local != 0 and i < 100:
		url[i] = content[start+6:end+4]
	#for_filename1 = content.find(r'>',end)
	#for_filename2 = content.find('</a>',end)
	#filename[i] = content[end+4:for_filename2]
		set_local = content.find(r'<a title',end) 
		start = content.find(r'href',set_local)
		end = content.find(r'html',start)
	#for_filename1 = content.find(r'>',start)
	#filename2 = content.find(r'</a',end)
	#filename[i] = content[end+4:for_filename2]
		i += 1
	
	j = 0
	def mkdir(path):
    # 引入模块
		import os
 
    # 去除首位空格
		path=path.strip()
    # 去除尾部 \ 符号
		path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
		isExists=os.path.exists(path)
 
    # 判断结果
		if not isExists:
        # 如果不存在则创建目录
			print path+u' 创建成功'
        # 创建目录操作函数
			os.makedirs(path)
			return True
		else:
        # 如果目录存在则不创建，并提示目录已存在
			print path+u' 目录已存在'
			return False
 
# 定义要创建的目录
	mkpath="e:\\somegit\\learncrawler\\hanhan\\page"+str(page+1)
# 调用函数
	mkdir(mkpath)
	while url[j] != '' and j < 50:
	
		filename = url[j][url[j].find(r'blog_'):]
		con = urllib2.urlopen(url[j]).read()
		open (r'E:\somegit\learncrawler\hanhan\page'+str(page+1)+'\ '+filename,'w').write(con)
		print 'downloading',url[j]
		#time.sleep(1)
		j += 1
	else:
		print 'page'+str(page+1)+'ok'
	page += 1
else:
	print 'all finished!'