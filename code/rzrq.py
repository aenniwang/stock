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
    try:
        str='NONE'
        url = 'http://data.eastmoney.com/rzrq/detail/%s.html' % code
        # a Better URL
        #url = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=FD&sty=MTE&mkt=1&code=%s' % code
        req = urllib.request.Request(url)
        content = urllib.request.urlopen(req).read()
        str = content.decode('gb2312')
        str= re.search('defjson:.*\]\},',str)
        if str:
            str=str.group()
            str=re.sub('defjson:\{pages.*data:\[','',str)
            str=re.sub('\]\},','',str)
            if re.search('stats:false',str):
                str='NONE'
                return str
        else:
            print("NONE!!")
            str='NONE'
            return str
        #save to file
        if SAVE_TO_FILE:
            f_name='rzrq_%s.html' % code
            f=open(f_name, 'w')
            f.write(str)
            f.close()
    except:
        str='NONE'
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
# MIN,MAX,START,END

# increase
# (END-START)/END > 50%

# decrease
# (START-END)/END > 50%

# RAPID
# (MAX-MIN)/MIN > 2倍

RZRQ_FEATURE_NONE=0
RZRQ_FEATURE_INCREASE=1
RZRQ_FEATURE_DECREASE=2
RZRQ_FEATURE_RAPID=4

#sum[0] is the oldest date
def get_rzrq_feature(sum):
    ret=RZRQ_FEATURE_NONE;
    MAX=max(sum)
    MIN=min(sum)
    START=sum[0]
    END=sum[len(sum)-1]
    #print('MAX=%d,MIN=%d,START=%d,END=%d' % (MAX,MIN,START,END))
    if((END>START) and (END-START)>0.5*END):
        ret += RZRQ_FEATURE_INCREASE
    if((START>END) and (START-END)>0.5*END):
        ret += RZRQ_FEATURE_DECREASE
    if((MAX-MIN)/MIN>2):
        ret += RZRQ_FEATURE_RAPID
    return ret

def rzrq(stock_code):
# Using debug message
    if DEBUG_USING_STATIC_DATA:
        html_txt=get_rzrq_from_file(stock_code)
    else:
        html_txt=get_rzrq_from_web(stock_code)
    # Get everyday data

    if html_txt and html_txt=='NONE':
        print('stock %s no rzrq' % stock_code)
        return 

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
    
    feature=get_rzrq_feature(rzrq_result)
    
    if PLOT:
        x=len(rzrq_result)
        f=open('tmp.dat','w')
        f.write('Stock %s' % stock_code)
        f.write('\n')
        f.write(str(feature))
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

rzrq('600004')
f=open('../docs/shanghai_name_symbol.txt','r')
for s in f:
    s.strip('\n')
    data=re.sub('\s+',' ',s)
    data=re.sub('\s+$','',data)
    data=re.sub('sh','',data)
    data=data.split(' ')
    code=data[0]
    print('For Stock %s ' % code)
    rzrq(code)
f.close()
