#!/usr/bin/python3
#coding=utf-8
import urllib.request
import os
from operator import itemgetter
import re

def get_price(code):
    prices=[]
    #symbol NAME Change Price
    url = 'http://hq.sinajs.cn/?list=%s' % code
#    print(url)
    req = urllib.request.Request(url)
    #HERE Saved a copy of shanghai stock names
 #   req.set_proxy('proxy.XXX.com:911', 'http')
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
    for i in range(0,len(info)):
        symbol=symbol_regex.findall(sn[i])
        symbol=symbol[0]
        data = info[i].split(',')
#        print(data)
        name = "%-6s" % data[0]
        price_current = "%-6s" % float(data[3])
        change_percent = ( float(data[3]) - float(data[2]) )*100 / float(data[2])
        change_percent = "%-6s" % round (change_percent, 2)
        stock_price = [symbol, name,eval(change_percent),eval(price_current)]
        prices.append(stock_price)
#        print(stock_price)
#    print(prices)
    return prices

f=open('sina_code_sh.txt','r')
stock_names=f.read();
f.close()

# Create Symbol - Name -Price
#
#ff=open('shanghai_name_symbol.txt','w+')
#shanghai_prices=get_price(stock_names)
#for pp in shanghai_prices:
#    ff.write("%s \n" % (' '.join(map(str,pp))))
#ff.close()

for time in range(0,1000):
    os.system('clear')
    shanghai_prices=get_price(stock_names)
    sorted_price =sorted(shanghai_prices,key=itemgetter(2))
    for p in sorted_price[0:20:1]:
        print(p)
    os.system('sleep 2')
