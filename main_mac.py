#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def read_from_file(file_name):
	file = "/Users/frendy/Desktop/github/ytcrawler/data/singerlist/" + file_name
	content = open(file).read()
	return content

FILE_LIST = "singers".split(",")

for file in FILE_LIST:
	FILE = file + ".txt"
	DEFAULT = read_from_file(FILE)

	ARTIST_LIST = DEFAULT.split(",")

	for artist in ARTIST_LIST:
		os.system("./../phantomjs-2.1.1/bin/phantomjs /src/js/search_image.js " + artist)