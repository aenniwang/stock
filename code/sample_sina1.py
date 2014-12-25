#!/usr/bin/python3
#coding=utf-8
import urllib.request
from operator import itemgetter

def get_price(code):
    #symbol NAME Change Price
    url = 'http://hq.sinajs.cn/?list=%s' % code
#    print(url)
    req = urllib.request.Request(url)
 #   req.set_proxy('proxy.XXX.com:911', 'http')
    content = urllib.request.urlopen(req).read()
    str = content.decode('gbk')
#    print(str)
    data = str.split('"')[1].split(',')
    name = "%-6s" % data[0]
    price_current = "%-6s" % float(data[3])
    change_percent = ( float(data[3]) - float(data[2]) )*100 / float(data[2])
    change_percent = "%-6s" % round (change_percent, 2)
    stock_price = [code, name,eval(change_percent),eval(price_current)]
    return stock_price


def get_all_price(code_list):
    prices=[]
    price=[0,0,0,0]
    for code in code_list:
        price = get_price(code)
        prices.append(price)
    return prices

f=open('shanghai_stock.txt','r')
stock_names=f.read();
f.close()
stocks=stock_names.split('.ss')
del stocks[len(stocks)-1] # del "\n"
for i in range(0,len(stocks)):
    stocks[i]='sh%s' % stocks[i]

#code_list = ['sz300036', 'sz000977', 'sh600718', 'sh600452', 'sh600489']
#print(stocks[1])
shanghai_prices=get_all_price(stocks)
new = sorted(shanghai_prices, key=itemgetter(3))
print (new)
