import  ystockquote

for i in range (0,1000):
    stock_number=i
    str_number= "6%05d.ss" % (stock_number)
    print(str_number)
    print(ystockquote.get_last_trade_price(str_number))
