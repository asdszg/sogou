#coding=utf-8 
import re
import urllib2
import re
import cPickle
import os
from bs4 import BeautifulSoup
import sys
reload(sys) 
sys.setdefaultencoding('utf-8') 
# def work():

# 	url = urllib2.urlopen('http://xh.5156edu.com/bs.html')
# 	r = url.read()
# 	r = r.decode('GB18030-2000')
# 	soup = BeautifulSoup(r)
# 	#print soup.text
# 	dict1={}  
# 	x=1
# 	ftp = open('bushou.txt','a+')
# 	for el in soup.find_all("a", class_="fontbox"):
# 		print el.text
# 		dict1[el.text]=el['href'][5:]
# 		ftp.write(str(x))
# 		ftp.write(el.text+' ')
# 		ftp.write("http://xh.5156edu.com/html/")
# 		ftp.write(dict1[el.text])
# 		ftp.write("\n")
# 		x+=1
# 	ftp.close()

# 	print '一共有'+str(len(dict1))+'个部首'

# 	ftp = open('zi.txt','a+')
# 	html_base="http://xh.5156edu.com/html/"
# 	dict2={}
# 	pinyin={}
# 	i=1
# 	y=0
# 	for han in dict1.keys():
# 		url=html_base+dict1[han]
# 		print url+' '+str(i)
# 		req = urllib2.urlopen(url) 
# 		r = req.read().decode('GB18030-2000')
# 		soup = BeautifulSoup(r)
# 		i+=1	
# 		for el in soup.find_all("a", class_="fontbox"):
# 			try:		
# 				y+=1
# 				#print el.text
# 				dict2[el.text[:1]]=el['href'][7:]
# 				pinyin[el.text[:1]]=el.text[1:]
# 				ftp.write(str(y)+'-')
# 				ftp.write(el.text[:1]+'-')
# 				ftp.write(el.text[1:]+'-')
# 				ftp.write("http://xh.5156edu.com/html3/")
# 				ftp.write(dict2[el.text])
# 				ftp.write("\n")
# 			except:
# 				y+=100000
# 				continue
# 	ftp.close()
# 	return dict2,pinyin

# def getInfo(src_str):

# 	bihuashu=re.search('笔画数：\d*',src_str).group()
# 	bushou=re.search('部首：.{3}',src_str).group()
# 	bishunbianhao=re.search('笔顺编号：\d*',src_str).group()[15:]

def main():
	url_base="http://www.wandoujia.com/apps/"
	fin = open("C:\Users\Administrator\Desktop\\apklist.txt","r")
	fout = open("out.txt","w")
	for line in fin.readlines():
		url=url_base+line
		html = urllib2.urlopen(url)
		print url
		r = html.read()
        	# r = r.decode('GBK')
		soup = BeautifulSoup(r)
		# for el in soup.find_all("span", itemprop="name"):
		# 	print el.text
		# for el in soup.find_all("span", itemprop="title"):
		# 	print el.text
		# for el in soup.find_all("span", "item"):
		# 	anzhungnum = el.i
		for el in soup.find_all("span", "item love"):
			likenum = el.i.text
		for el in soup.find_all("a", title="查看评论"):
			pinglunnum = el.i.text
		for el in soup.find_all("div", "num-list"):
			pinglunnum1 = el.i.text
			print pinglunnum1
		for el in soup.find_all("a", itemprop="SoftwareApplicationCategory"):
			name = el.text
			print name
		for el in soup.find_all("a", {"class":"dev-sites"}):
			name1 = el.text
			print name1
		fout.write(pinglunnum1+"_"+likenum+"_"+pinglunnum+"_"+name.strip()+"_"+name1+"\n")
	fout.close()
	fin.close()

		
		
		




	# for han1 in dict2.keys():

	# 	x+=1 
	# 	if x<8095:
	# 		continue
	# 	else:

	# 		url1=html_base1+dict2[han1]
	# 		print url1+' '+str(x)
	# 		try :
	# 			req = urllib2.urlopen(url1)
	# 			r = req.read().decode('GB18030-2000','ignore').encode("utf-8")

	# 		except:
	# 			ftp = open('login.txt','w+')
	# 			ftp.write(str(x)+' ')
	# 			ftp.write(url1)
	# 			ftp.write("\n")
	# 			ftp.close
	# 			pass 
	# 		ftp = open('111.txt','a')
	# 		match = re.search("<hr class=hr1>\s*\S* <br>.*\s<br><br>",r)
	# 		if not match:
	# 			print "没有匹配"
	# 			ftp = open('log.txt','a+')
	# 			ftp.write(str(x)+' ')
	# 			ftp.write(url1)
	# 			ftp.write("\n")
	# 			ftp.close
	# 			continue
	# 		info = match.group()
	# 		soup = BeautifulSoup(info)
	# 		soup = soup.text.encode("utf-8")

	# 		bihuashu=re.search('笔画数：\d*',soup).group()
	# 		bushou=re.search('部首：.{3}',soup).group()
	# 		bishunbianhao=re.search('笔顺编号：\d*',soup).group()[15:]


		
	# 		ftp.write(str(x)+'	')
	# 		ftp.write(soup.strip()[:4]+'	')
	# 		ftp.write(bihuashu.strip()+'	')
	# 		ftp.write(bushou.strip()+'	')
	# 		ftp.write(bishunbianhao.strip())
	# 		ftp.write("\n")
	# 	ftp.close()


if __name__=="__main__":
        main()
