#!/usr/bin/python
class Member:
	memberId=0
	def __init__(self,name,age):
		self.name=name
		self.age=age
		Member.memberId+=1
	def display(self):
		print "Name: ",self.name, "Age: ",self.age


class Student(Member):
	def __init__(self,grade,count):
		self.grade=grade
		self.count=count
		self.subject=[]
		for i in range(count):
			k=raw_input("Enter the Subject: ")
			self.subject.append(k)

	def stu(self,name,age):
		self.name=name
		self.age=age
		Member.memberId+=1



class Teacher(Student):
	def displayall(self):
		self.display()
		print "The subjects taken by the student are ",self.subject
		

if __name__=='__main__':
	# ak=Member('akshay',19)
	# ra=Member('rakesh',19)
	# print "Mebmer ID:",Member.memberId
	# ak.display()
	# ra.display()
	# aks=Student('A',2)
	# aks.age=20
	# aks.name='AKSHAY'
	# print "Grade of the candidate %s is %s"%(aks.name,aks.grade)
	akshay=Teacher('A',2)
	akshay.stu("AKS",19)
	akshay.displayall()
	print "Mebmer ID:",Member.memberId
