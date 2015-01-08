import  ystockquote

f=open('sz_stock_name_for_sina.txt','a')
j=0
if 1:
    for i in range (0,3000):
        stock_number=i
        str_number= "sz%d%05d," % (j,stock_number)
        print(str_number)
        price = eval(ystockquote.get_last_trade_price(str_number))
        if price < 0.5:
    	    print "PRICE too small: %d" % price
        else:
    	    f.write(str_number)
    	    print("%s : %d" % (str_number, price))
f.close()
print("Finished")
