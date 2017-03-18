#!bin/python
n=input()
groups=[]
count=0
m1=0
m2=0
m3=0
for i in range(0,n):
	x=input()
	groups.append(x)
groups.sort()
for i in groups:
	if i==4:
		count=count+1
	elif i==3:
		m3=m3+1
	elif i==2:
		m2=m2+1
	elif i==1:
		m1=m1+1
if m3>m1:
	m3=m3-min(m3,m1)
	count=count+m3
else:
	m1=m1-min(m3,m1)
	count=count+m1/4
if m2%2==0:
	count=count+m2/2
else:
	count=count+m2/2+1
count=count+min(m3,m1)
print count