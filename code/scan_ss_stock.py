import  ystockquote

f=open('shanghai_stock_name_for_sina.txt','a')
for i in range (0,10):
    stock_number=i
    str_number= "sh6%05d," % (stock_number)
    price = eval(ystockquote.get_last_trade_price(str_number))
    if price < 0.5:
	print "PRICE too small: %d" % price
    else:
	f.write(str_number)
	print("%s : %d" % (str_number, price))
f.close()
print("Finished")
