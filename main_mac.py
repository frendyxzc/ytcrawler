#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

DEFAULT = "BEYONCÉ"

######

ARTIST_LIST = DEFAULT.split(",")

for artist in ARTIST_LIST:
    os.system("./../phantomjs-2.1.1/bin/phantomjs /src/js/search_more.js " + artist)