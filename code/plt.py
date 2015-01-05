#/usr/bin/python
#coding=utf-8
import re
# Works without $DISPLAY
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
#
#****data format****
# title
# feature
# len\n
# [date array]\n
# [price array]\n
f=open('tmp.dat','r')

title=f.readline().strip()
feature=f.readline().strip()
length=eval(f.readline().strip())

date=f.readline().strip()
date=re.sub(r'\[','',date)
date=re.sub(r'\]','',date)
date=re.sub(r' +','',date)
date=re.sub(r'\'','',date)
date=date.split(',')

content=f.readline().strip()
content=re.sub(r'\[','',content)
content=re.sub(r'\]','',content)
content=re.sub(r' +','',content)
content=map(float,content.split(','))
content=[i/1000000 for i in content]
f.close()

xticks=range(0,length)
xtick_labels=date

fig=plt.figure()
ax=fig.add_subplot(111)

ax.set_label('Date')
ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels,rotation=90,fontsize=8)
 
plt.xlabel('Date', multialignment='center')
plt.ylabel('0.01 \'Yi Yuan\'')
plt.title(title)
#print(content)
ax.plot(content)
pic_name=('%s-%s.jpg' % (feature,title))
pic_name=re.sub('Stock ','',pic_name)
fig.savefig(pic_name)
#plt.show()

