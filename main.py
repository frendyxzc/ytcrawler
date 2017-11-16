#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

DEFAULT = "陈奕迅,孙燕姿"

######

ARTIST_LIST = DEFAULT.split(",")

for artist in ARTIST_LIST:
    os.system("python crawler.py " + artist)