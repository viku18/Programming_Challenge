# Import Module
import string
import sys
from collections import defaultdict,deque
ALPHA = string.ascii_letters
# Folder Path
data=sys.argv[1]
dict1 = defaultdict(list)
with open(data,'r') as fh:
	for line in fh:
		if line.startswith(tuple(ALPHA)):
			pass
		else:
			tpl = line.split(",")
			x=tpl[4].strip()
			if x=='':
				pass
			else:
				val=list([int(tpl[0]),tpl[1],tpl[2],float(tpl[3]),int(float(x))])
				dict1[tpl[1]].append(val)
total_PNL=0
l1=[]
for k,v in dict1.items():
	b=deque()
	s=deque()
	for i in range(len(v)):
		if v[i][2]=='B':
			b.append(v[i])
		else:
			s.append(v[i])
	
	while b and s:
		b1=b.popleft()
		x=b1[-1]
		while x>0 and s:
			s1=s.popleft()
			y=s1[-1]
			q=min(x,y)
			pnl=round(q*(s1[3]-b1[3]),2)
			x=abs(x-q)
			y=abs(y-q)
			total_PNL+=pnl
			if y!=0:
				s.appendleft([s1[0],k,s1[2],s1[3],y])
			if b1[0]>s1[0]:
				l1.append([s1[0],b1[0],k,q,pnl,s1[2],b1[2],s1[3],b1[3]])
			else:
				l1.append([b1[0],s1[0],k,q,pnl,b1[2],s1[2],b1[3],s1[3]])
		if x!=0:
			b.appendleft([b1[0],k,b1[2],b1[3],x]) 

l1.sort(key=lambda l1: l1[1])
print('OPEN_TIME','CLOSE_TIME','SYMBOL','QUANTITY','PNL','OPEN_SIDE','CLOSE_SIDE','OPEN_PRICE','CLOSE_PRICE')
for ele in l1:
	print(*ele)
print(total_PNL)