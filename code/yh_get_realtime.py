#!/usr/bin/python3
#coding=utf-8

import re
import urllib.request
import os
from operator import itemgetter

def get_realtime_data(code,function):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (code,function)
    req = urllib.request.Request(url)
    content = urllib.request.urlopen(req).read()
    msg = content.decode('gbk')
    print(msg)


function='snd1l1yrl2l3'

f=open('yh_code.txt','r')
for msg in f:
    msg=msg.strip()
    msg.strip(',')
    if re.match('\d{6}.s[z|s]',msg):
        print("Fetch history data for %s "%msg)
        get_realtime_data(msg,function)
f.close()
