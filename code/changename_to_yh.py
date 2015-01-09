#!/usr/bin/python3
import re
f=open('sina_code.txt','r')
fo=open('yh_code.txt','w')
msg=f.readline()
fo.write(msg)
msg=f.readline().strip()
msgfind=re.findall('sh\d{6}',msg)
for i in msgfind:
    i=re.sub('sh','',i)
    i+='.ss'
    fo.write('%s,'%i)
fo.write('\n')
msg=f.readline()
fo.write(msg)
msg=f.readline().strip()
msgfind=re.findall('sz\d{6}',msg)
for i in msgfind:
    i=re.sub('sz','',i)
    i+='.sz'
    fo.write('%s,'%i)
fo.write('\n')
msg=f.readline()
fo.write(msg)
msg=f.readline().strip()
msgfind=re.findall('sz\d{6}',msg)
for i in msgfind:
    i=re.sub('sz','',i)
    i+='.sz'
    fo.write('%s,'%i)
fo.write('\n')
f.close()
fo.close()
