# -*- coding: utf-8 -*-
from __future__ import print_function   # for compatibility with both python 2 and 3
import os 
import sys
import argparse
#import tkinter as tk
from subprocess import call 
from pytube import YouTube
import time
#from progressbar import *

class YTDownload():
	def __init__(self,url,location):
		#self.file_size=0
		self.url=url
		self.location=location

	def Downloader(self,url):
		# User input argument and pass to download
		location = self.Youtube_locate()
		self.Youtubedownload(url,location)
		print('Done!!!!')

	def Youtube_locate(self):
		location = os.getcwd()
		location=location+'/'
		#print(location)
		#location=input("Save Location :")
		return location

	def Youtubedownload(self,URL,location):
	# Download from Youtube
		global file_size
		YT = YouTube(URL, on_progress_callback=show_progress)
		#print('A:',file_size)
		#YT = YouTube(URL,on_progress_callback=self.show_progress)
		YTstream = YT.streams.filter(file_extension='mp4',only_audio=True).first()
		file_size = YTstream.filesize # Get video size
		#print('B:',file_size)
		#YTstream.download('/Users/useriii/Desktop')
		YTstream.download(location)

def show_progress(stream=None, chunk=None, file_handle=None, bytes_remaining=None):
	#print('C:',file_size)
	#print('D:',file_handle)
	ch='*'
	#chunk=0
	chunk_count=0
	#print('E:',bytes_remaining)
	#chunks=str(chunk,encoding="utf-8")
	#print('F:',chunks)
	file_receive=file_size-bytes_remaining
	#print('G:',file_receive)
	#print('G:',chunk_count)
	percent = int((100*(file_receive))/file_size) # Display 當前以下載進度
	#print('G:',percent)
	#chunk_count = int(round(int(round(percent))/5))
	chunk_count = percent // 5
	#print('A:',chunk_count)
	bar = ch*chunk_count+' '*(20-chunk_count)
	text = '|{bar}| {percent} %\r'.format(bar=bar,percent=percent)
	time.sleep(0.01) # 等待時間不能太常，會造成buffer太久而形成connectionreseterror
	sys.stdout.write(text)
	sys.stdout.flush()

'''
def get_terminal_size():
	rows,columns=os.popen('stty size', 'r').read().split()
	return int(rows),int(columns)
'''
'''
def show_progress(stream=None, chunk=None, file_handle=None, bytes_remaining=None):
	ch='*'
	scale=0.55
	rows,columns=get_terminal_size()
	max_width=int(columns*rows)
	bytes_received=file_size-bytes_remaining
	filled=int(round(max_width*bytes_received/file_size))
	remaining=max_width-filled
	bar=ch*filled+' '*remaining
	percent = (100*(file_size-bytes_remaining))/file_size # Display 當前以下載進度
	text= '|{bar}| {percent}%\r'.format(bar=bar,percent=percent)
	#print(text, end='\r')
	time.sleep(1)
	sys.stdout.write(text)
	sys.stdout.flush()
'''	

if __name__ == '__main__':
	#file_size=0
	YTD=YTDownload(0,'C:')
	parser = argparse.ArgumentParser(description='Process an url')
	parser.add_argument('-u','--ur',action='store',dest='url',default=None,help='<Required> url link',required=True)
	args = parser.parse_args()#collect command line parameter
	url=args.url
	YTD.Downloader(url)

'''
Reference Site:
https://pypi.org/project/pytube/
https://python-pytube.readthedocs.io/en/latest/_modules/pytube/streams.html?highlight=Progress%20bar
https://www.cnblogs.com/yinxiangnan-charles/p/5645561.html
http://python-pytube.readthedocs.io/en/latest/user/quickstart.html#working-with-streams
https://docs.python.org.tw/3/howto/argparse.html
https://stackoverflow.com/questions/15170547/passing-a-url-as-argument
https://github.com/nficano/pytube/blob/master/pytube/cli.py
https://www.saltycrane.com/blog/2007/12/how-to-pass-command-line-arguments-to/
https://www.unixmen.com/how-to-download-youtube-videos-pytube/
http://kuanghy.github.io/2016/06/30/python-argparse
https://yagisanatode.com/2018/03/11/how-to-create-a-simple-youtube-download-program-with-a-progress-in-python-3-with-pytube/
https://faultinmycode.com/python-youtube-downloader/
https://extenshu.com/2017/09/24/python%E5%88%9D%E5%AD%B8%E9%87%8D%E9%BB%9E-05-global%E8%AE%8A%E6%95%B8/
http://www.cnblogs.com/huangjacky/archive/2012/04/19/2457842.html
https://docs.python.org/3/library/exceptions.html#ConnectionError
'''

'''
爬蟲
https://medium.com/@chenchoulo/python-requests%E7%88%AC%E8%9F%B2%E5%85%A5%E9%96%80-yahoo%E9%9B%BB%E5%BD%B1%E6%8E%92%E8%A1%8C%E5%AF%A6%E6%88%B0-python-requests-crawler-tutorial-yahoo-movie-ranking-example-4f291257d61c
https://hk.saowen.com/a/f15b6108ccb148b8cecd817f21092ee44e6a6eee156025e392974ca8f22a8e97
'''
'''
os.getcwd() 取得當前工作位置
http://www.runoob.com/python/os-getcwd.html
'''

'''
python video

https://www.youtube.com/watch?v=00agGNMNmTk
https://www.youtube.com/user/wuchaiyen/playlists
https://kknews.cc/zh-tw/tech/nx23grq.html
https://www.google.com.tw/search?ei=Gv_9W-C4BM2moAScoZy4BA&q=euclidean+distance+python&oq=euclidean+distance&gs_l=psy-ab.1.2.0i71l7.0.0..3104...0.0..0.0.0.......0......gws-wiz.wUMAD4ivUd4
https://speakerdeck.com/mosky/practicing-python-3
https://facebook.github.io/prophet/docs/quick_start.html
https://www.inside.com.tw/article/8635-facebook-prophet-forecasting-at-scale
http://wsfdl.com/python/2013/08/14/%E7%90%86%E8%A7%A3Python%E7%9A%84mutable%E5%92%8Cimmutable.html
'''