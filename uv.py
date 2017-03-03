#-*-coding:utf-8 -*-

import re
import os
from prettytable import PrettyTable

#uv_dic = {}
x = PrettyTable(["Date", "UniqueVisitors"])  
x.align["Date"] = "l"
x.padding_width = 1

filenames=os.popen('ls access_qq*.html').read()

sum = 0.0
i = 0
for filename in filenames.split("\n"):
	if filename:
		
		date=re.search('\d+',str(filename)).group()
		#print (date)
		
		f = open(filename,"r+")
		p = re.compile("Unique Visitors</div><h3 class='label trunc'>(\d+,\d+)(.*) Unique Files")
		s=p.search(f.read())
		x.add_row([date,s.groups()[0]])
		#uv_dic[date]=s.groups()[0]
		#print (s.groups()[0])
		l=s.groups()[0].split(',')
		k = ''
		for j in range(len(l)):
			k += l[j]
		#print (k)
		sum += int(k) 
		i += 1	
		f.close()
        
	else:
		continue

#print (uv_dic)
x.add_row(['-'*10,'-'*16])
x.add_row(['Total_UV',sum])
x.add_row(['Average_UV',sum/i])
print (x)
