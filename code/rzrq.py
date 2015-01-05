#!/usr/bin/python3
#coding=utf-8

import urllib.request
import re
import os
#import matplotlib.pyplot as plt

PLOT=1
SAVE_TO_FILE = 0
DEBUG_USING_STATIC_DATA = 0

def get_rzrq_from_web(code):
    url = 'http://data.eastmoney.com/rzrq/detail/%s.html' % code
    # a Better URL
    #url = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=FD&sty=MTE&mkt=1&code=%s' % code
    req = urllib.request.Request(url)
    content = urllib.request.urlopen(req).read()
    str = content.decode('gbk')
    str= re.search('defjson:.*\]\},',str)
    if str:
        str=str.group()
        str=re.sub('defjson:\{pages.*data:\[','',str)
        str=re.sub('\]\},','',str)
        #print(str)
    else:
        print("NONE!!")
    #save to file
    if SAVE_TO_FILE:
        f_name='rzrq_%s.html' % code
        f=open(f_name, 'w')
        f.write(str)
        f.close()
    return str

def get_rzrq_from_file(code):
    f_name='rzrq_%s.html' % code
    f=open(f_name, 'r')
    content=f.read()
    f.close()
    str= re.search('defjson:.*\]\},',content)
    if str:
        str=str.group()
        str=re.sub('defjson:\{pages.*data:\[','',str)
        str=re.sub('\]\},','',str)
        #print(str)
    else:
        print("NONE!!")
    return str

stock_code='600183'
# Using debug message
if DEBUG_USING_STATIC_DATA:
    html_txt=get_rzrq_from_file(stock_code)
else:
    html_txt=get_rzrq_from_web(stock_code)
# Get everyday data
rzrq_arrays=html_txt.split('"')
rzrq_arrays=rzrq_arrays[1:len(rzrq_arrays):2]
rzrq_arrays.reverse()
# Get 
rzrq_result=[]
rzrq_date=[]
for everyday in rzrq_arrays:
    item=everyday.split(',')
    rzrq_date.append(item[4])
    rzrq_result.append(eval(item[3]))
    #print('%s - %s' %  (item[4],item[3]))

if PLOT:
    x=len(rzrq_result)
    f=open('tmp.dat','w')
    f.write('Stock %s' % stock_code)
    f.write('\n')
    f.write(str(x))
    f.write('\n')
    f.write(str(rzrq_date))
    f.write('\n')
    f.write(str(rzrq_result))
    f.write('\n')
    f.close()
    os.system('python plt.py')
#Draw a map


