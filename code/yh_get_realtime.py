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
    return msg

#Support list
#c c1 c3 c6 c8
#
#NOT support list
#sz
#j1:marker_cap

#ss
#j1:marker_cap
function='snl1vos7rr2k3hg'
func_des='symbol,name,last-trade-price,volume,'
data=''
while 1:
    data=get_realtime_data('BRCM+CAVM+BABA',function)
    os.system('clear')
    print(data)
    os.system('sleep 1')
if 0:
    f=open('yh_code.txt','r')
    for msg in f:
        msg=msg.strip()
        code_len=10
        if re.findall('\d{6}.s[s|z]',msg)==[]:
         #   print("Msg is %s"%msg)
            continue
        while msg:
            code=msg[0:code_len*200-1]
            msg=msg[code_len*200:]
            data=get_realtime_data('BRCM+CAVM+BABA',function)
            print(data)
            #data+=get_realtime_data(code,function)
    SAVE=0
    if SAVE:
        f=open('yh_respond.txt','w')
        f.write('%s\n'%func_des)
        f.write(data)
        f.close()
        
