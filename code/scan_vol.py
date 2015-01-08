#!/usr/bin/python3
#coding=utf-8
import urllib.request
import os
from operator import itemgetter
#from numpy import *
import re
#
# output array
# [name][symbol][time][vol][change][price]
def get_vol(code,num,name,symbol,vol,change,price):
    #symbol NAME Change Price
    url = 'http://hq.sinajs.cn/?list=%s' % code
#    print(url)
    req = urllib.request.Request(url)
    #HERE Saved a copy of shanghai stock names
    content = urllib.request.urlopen(req).read()
    #str = content.decode('gb2312')
    str = content.decode('gbk')
# Store to file
#    file=open('sina_stock_return_msg.txt','w+')
#    file.write(str)
#    file.close()
    info=str.split('"')
    sn=info[0:len(info):2]
    info=info[1:len(info):2]
#    print(info)
    symbol_regex=re.compile(r's[hz]\d{6}')
    mini=min(len(info),num)
    for i in range(0,mini):
        ssymbol=symbol_regex.findall(sn[i])
        ssymbol=ssymbol[0]
        data = info[i].split(',')
        #print(data)
        sname = "%-6s" % data[0]
        price_current = "%-6s" % float(data[3])
        change_percent = ( float(data[3]) - float(data[2]) )*100 / float(data[2])
        change_percent = "%-6s" % round (change_percent, 2)
        stime=data[31]
        t=stime.split(':')
        n_time=(int(t[0]))*3600+(int(t[1]))*60+int(t[2])
        n_vol=eval(data[8])
        name[i]=sname
        symbol[i]=ssymbol
        time=n_time
        vol[i]=n_vol
        price[i]=float(price_current)
        change[i]=float(change_percent)
    return time


#[5sec_vol][10sec_vol][15sec_vol][30sec_vol][1min_vol][5min_vol][10min_vol]

# store 1200 seconds data
COUNT_TIME_SEC=600
list_vol=[]
list_time=[]
ci=0
def process(vols,time,data_vols,data_times):
    global ci
    global list_vol
    global list_time
    global COUNT_TIME_SEC
    global time_start
    if ci >= COUNT_TIME_SEC:
        list_vol.pop(COUNT_TIME_SEC-1)
        list_time.pop(COUNT_TIME_SEC-1)
    list_vol.insert(0,vols)
    list_time.insert(0,time)
    #list_vol[0] is the data_vols for every second
    #list_vol[EVERY_SECOND][EVERY_STOCK]
    if time_start==0:
        time_start=time
        print("Start at %02d-%02d-%02d"%(int(time_start/3600),int((time_start%3600)/60),int(time_start%60)))
        return
    for j in range(0,len(list_vol[0])):
        data_times[5]=time-list_time[min(ci,599)]
        data_times[4]=time-list_time[min(ci,299)]
        data_times[3]=time-list_time[min(ci,59)]
        data_times[2]=time-list_time[min(ci,29)]
        data_times[1]=time-list_time[min(ci,9)]
        data_times[0]=time-list_time[min(ci,4)]
        if list_vol[0][j]==0:
            data_vols[5][j]=data_vols[4][j]=data_vols[2][j]=data_vols[3][j]=data_vols[1][j]=data_vols[0][j]=1;
        else:
            data_vols[5][j]=(100*(list_vol[0][j]-list_vol[min(ci,599)][j])*data_times[5])/list_vol[0][j]
            data_vols[4][j]=(100*(list_vol[0][j]-list_vol[min(ci,299)][j])*data_times[4])/list_vol[0][j]
            data_vols[3][j]=(100*(list_vol[0][j]-list_vol[min(ci,59)][j])*data_times[3])/list_vol[0][j]
            data_vols[2][j]=(100*(list_vol[0][j]-list_vol[min(ci,29)][j])*data_times[2])/list_vol[0][j]
            data_vols[1][j]=(100*(list_vol[0][j]-list_vol[min(ci,9)][j])*data_times[1])/list_vol[0][j]
            data_vols[0][j]=(100*(list_vol[0][j]-list_vol[min(ci,4)][j])*data_times[0])/list_vol[0][j]
        data_vols[6][j]=vols[j];
    ci=ci+1
    

f=open('sina_code_sh.txt','r')
stock_num=eval(f.readline().strip())
stock_names=f.read();
f.close()

   
# Create Symbol - Name -Price
#
#ff=open('shanghai_name_symbol.txt','w+')
#shanghai_prices=get_price(stock_names)
#for pp in shanghai_prices:
#    ff.write("%s \n" % (' '.join(map(str,pp))))
#ff.close()
#get_vol('sh600138')
vol_data=[]
vol_data.append([0 for i in range(0,stock_num)])
vol_data.append([0 for i in range(0,stock_num)])
vol_data.append([0 for i in range(0,stock_num)])
vol_data.append([0 for i in range(0,stock_num)])
vol_data.append([0 for i in range(0,stock_num)])
vol_data.append([0 for i in range(0,stock_num)])
vol_data.append([0 for i in range(0,stock_num)])
vol_time=[0 for i in range(0,6)]

time_start=0
time_current=0

name=['' for i in range(0,stock_num)]
symbol=['' for i in range(0,stock_num)]
vol=[0 for i in range(0,stock_num)]
change=[float(0) for i in range(0,stock_num)]
price=[float(0) for i in range(0,stock_num)]

stock_static=[]
for t in range(0,1000):
    time_current=get_vol(stock_names,stock_num,name,symbol,vol,change,price)
    process(vol,time_current,vol_data,vol_time)
    for i in range(0,stock_num):
        vol_dat=[symbol[i],name[i],vol_data[5][i],vol_data[4][i],vol_data[3][i],
                vol_data[2][i],vol_data[1][i],vol_data[0][i],vol_data[6][i] ]
        if len(stock_static)!=stock_num:
            stock_static.append(vol_dat)
        else:
            stock_static[i]=vol_dat
    #Sort by absolute volume
    sorted_volume=sorted(stock_static,key=itemgetter(8),reverse=True)

    os.system('clear')
    for p in sorted_volume[0:40:1]:
        print(p)
    os.system('sleep 2')
