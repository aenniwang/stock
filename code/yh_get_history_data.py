#!/usr/bin/python3
#coding=utf-8

import re
import urllib.request
import os
from operator import itemgetter

#
# YAHOO Interface
#
# 查询浦发银行2010.09.25 – 2010.10.8之间日线数据
#http://ichart.yahoo.com/table.csv?s=600000.SS&a=08&b=25&c=2010&d=09&e=8&f=2010&g=d
#查看国内沪深股市的股票，规则是：沪股代码末尾加.ss，深股代码末尾加.sz。如浦发银行的代号是：600000.SS
#s — 股票名称
#a — 起始时间，月
#b — 起始时间，日
#c — 起始时间，年
#d — 结束时间，月
#e — 结束时间，日
#f — 结束时间，年
#g — 时间周期。

# year_start/end format "2014-01-01"
def get_history_data(code,year_start,year_end):
    global foldname
    ys=year_start.split('-')
    ys[1]=str(int(ys[1])-1)
    ye=year_end.split('-')
    ye[1]=str(int(ye[1])-1)
    url = 'http://ichart.yahoo.com/table.csv?s=%s&a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&g=d'%(code,ys[1],ys[2],ys[0],ye[1],ye[2],ye[0])
  #  os.system('sleep 10')
    req = urllib.request.Request(url)
    content = urllib.request.urlopen(req).read()
    msg = content.decode('gbk')

    file_name='%s/%s.csv'%(foldname,code)
    f=open(file_name,'w')
    f.write(msg)
    f.close()

start_date_latest='2014-12-10'
start_date='2013-12-25'
end_date='2015-01-08'
foldname='%s--%s'%(start_date,end_date)

os.system('mkdir %s'%foldname)

f=open('yh_code.txt','r')
for msg in f:
    msg.strip()
    code_list=re.findall('\d{6}.s[s|z]',msg)
    for code in code_list:
        print("Fetch history data for %s "%code)
        try:
            get_history_data(code,start_date,end_date)
        except:
            print("Error in get history data for %s"%code)
            try:
                get_history_data(code,start_date_latest,end_date)
            except:
                print("Still failed in get latest data")
f.close()
