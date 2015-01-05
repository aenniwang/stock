#!/usr/bin/python3

import re

def get_stock_symble(str_file_database, str_file_name, str_file_sym):
    try:
       f_file=open(str_file_name,'r')
       f_data=open(str_file_database,'r')
       f_sym=open(str_file_sym,'w+')
       for l_name in f_file:
           l_name.strip('\n')
           l_name=re.sub('\s+','',l_name)
           for l_data in f_data:
               l_data.strip('\n')
               data=re.sub('\s+',' ',l_data)
               data=re.sub('\s+$','',data)
               data=data.split(' ')
               if (data[0] == l_name) or (data[1] == l_name):
                   f_sym.write('%s %s' % (data[0],data[1]))
                   print("Found %s:%s" % (data[0],data[1]))
                   break;
    except IOError:
        print("get_stock_symble file error.")
    finally:
        f_file.close()
        f_data.close()
        f_sym.close()

get_stock_symble('../docs/shanghai_name_symbol.txt','name.txt','sym.txt')
