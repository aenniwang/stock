#!/usr/bin/python3
import re
f=open('sh_stock_sina.txt','r')
names=f.read()
f.close()
regex=re.compile(r'\.ss')
code=(regex.sub(',sh',names))
f=open('sina_code_sh2.txt','a')
f.write('sh')
f.write(code)
f.close
