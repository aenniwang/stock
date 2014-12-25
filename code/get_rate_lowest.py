import  ystockquote

fstock=open('shanghai_stock.txt','r')
str=fstock.read()
fstock.close();
stocks=str.split('.ss')
stock_num=len(stocks)-1
stock_num = 10

price=[]
for i in range (0,stock_num):
	str_stock="%s.ss" % (stocks[i])
	price.append(eval(ystockquote.get_last_trade_price(str_stock)))
	print(price[i])

sorted(price)
print(price)
