#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import subprocess
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

YOUTUBE_ADDR = ""
YOUTUBE_FILE = "C:\\Users\\frend\\Desktop\\ccc\\yt.html"

def getDom(url):
    cmd = 'D:\\PycharmProjects\\phantomjs-2.1.1\\bin\\phantomjs \\js\\body.js "%s"' % url
    print "cmd:", cmd
    stdout, stderr = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    if stderr.strip() != '':
        print stderr
    return stdout


if __name__ == "__main__":

    print sys.argv[1]

    # content = getDom(YOUTUBE_ADDR + sys.argv[1])
    content = open(YOUTUBE_FILE).read()

    pattern_key = re.compile(
        r'<a is="yt-endpoint" id="view-all-endpoint" class="style-scope ytd-watch-card-video-list-renderer" href="https://www.youtube.com/playlist\?list=(.+?)">',
        re.S)
    keys = re.findall(pattern_key, content)

    f = file("./data/playlist_artist.txt", "a")
    for key in keys:
        tmp = key + ","
        f.writelines(tmp)
    f.close()
    print "** finish to print result **"