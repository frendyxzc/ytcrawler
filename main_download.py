#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import urllib
reload(sys)
sys.setdefaultencoding('utf-8')

def read_from_file(file_name):
	file = "/Users/frendy/Desktop/github/ytcrawler/data/singerlist/" + file_name
	f = open(file, 'r')
	return f

def save_img(img_url,file_name, file_path='images'):
    #保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
    try:
        if not os.path.exists(file_path):
            print '文件夹',file_path,'不存在，重新建立'
            #os.mkdir(file_path)
            os.makedirs(file_path)
        #获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        #拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
       #下载图片，并保存到文件夹中
        urllib.urlretrieve(img_url,filename=filename)
    except IOError as e:
        print '文件操作失败',e
    except Exception as e:
        print '错误 ：',e

if __name__ == '__main__':
    FILE = "singer_icon.txt"
    content = read_from_file(FILE)

    for line in content.readlines():
        info = line.split(",")
        #print info[1].replace('\r\n', '')
        print info[0]
        save_img(info[1].replace('\r\n', ''), info[0])