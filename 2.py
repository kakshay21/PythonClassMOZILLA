#!/bin/python
string=input()
a=string[0].isupper()
string1=[]
if a=='TRUE':
	if string[1:].isupper():
		string1.append(string[0])
		string1.append(string[1:].lower())
else:
	if string[1:].isupper():
		string1.append(string[0].upper())
		string1.append(string[1:].lower())
print ''.join(map(str,string1))