#!/usr/bin/python3
#coding=

import re

f_data=open(r'../docs/shanghai_name_symbol.txt','r')
for line in f_data:
    line.strip('\n')
    data=re.sub('\s+',' ',line)
    data=re.sub('\s+$','',data)
    data=data.split(' ')
    if
f_data.close()


