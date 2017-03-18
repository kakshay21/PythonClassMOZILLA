#!/bin/python
s=input()
n=input()
ds=[]
bonus=[]
for i in range(0,n):
	x=input()
	y=input()
	ds.append(x)
	bonus.append(y)
ds.sort()
for i in range(0,n):
	if ds[i]<s:
		print "YES"
		s=s+bonus[i]
	else:
		print "NO"