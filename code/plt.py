#/usr/bin/python
#coding=utf-8
import re
import matplotlib.pyplot as plt
#
#data format
#len\n
#[date array]\n
#[price array]\n
f=open('tmp.dat','r')

title=f.readline().strip()
print(title)

len=eval(f.readline().strip())
print(len)

date=f.readline().strip()
date=re.sub(r'\[','',date)
date=re.sub(r'\]','',date)
date=re.sub(r' +','',date)
date=re.sub(r'\'','',date)
date=date.split(',')
print (date)

content=f.readline().strip()
content=re.sub(r'\[','',content)
content=re.sub(r'\]','',content)
content=re.sub(r' +','',content)
content=map(int,content.split(','))
content=[i/1000000 for i in content]
f.close()

xticks=range(0,len)
xtick_labels=date

ax = plt.subplot(111)

ax.set_label('Date')
ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels,rotation=90,fontsize=8)
 
plt.xlabel('Date', multialignment='center')
plt.ylabel('0.01 \'Yi Yuan\'')
plt.title(title)
#print(content)
ax.plot(content)
plt.show()

