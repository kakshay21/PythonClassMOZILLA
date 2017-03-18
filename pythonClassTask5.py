#!/usr/bin/python

class Consumer:
	def __init__(self):
		self.customer=[]
		self.customerid=[]

	def addConsumer(self,cust,id):
		self.customer.append(cust)
		self.customerid.append(id)


class Product:
	def __init__(self):
		self.product=[]
		self.price=[]

	def addProduct(self,name,price):
		self.product.append(name)
		self.product.append(price)

class Employee(Consumer,Product):
	def __init__(self):
		self.empname=[]
		self.emppass=[]

	def addEmployee(self,emplname,emplpass):
		self.ampname.append(emplname)
		self.amppass.append(emplpass)

	def DelProduct(self,proname):
		if proname in self.product:
			for i in range(size(self.product)):
				if self.product[i] is proname:
					self.product.pop(i)

	def DelConsumer(self,consname):
		if consname in self.customer:
			for i in range(size(self.customer)):
				if self.customer[i] is consname:
					self.customer.pop(i)

class Admin(Employee):
	def __init__(self):
		self.admname=[]
		self.admpass=[]
	def addAdmin(self,admname,admpass):
		self.admname.append(admname)
		self.admpass.append(admpass)

	def DelEmployee(self,emplname):
		if emplname in self.empname:
			for i in range(size(self.empname)):
				if self.empname[i] is emplname:
					self.empname.pop(i)
					self.emppass.pop(i)


if __name__=='__main__':
	newcon=Consumer()
	adcon=open("consumer.txt","r")
	while True :
		line = adcon.readline()
		newcon.addConsumer(line)
		if ("" == line):
			break
	newpro=Product()
	adpro=open("product.txt","r")
	while True :
		line = adpro.readline()
		price=adpro.readline()            # Assumed that in the text file
		newcon.addProduct(line)           # The format will be like 
		newcon.addproduct(price)          # pencil
		if ("" == line):                  # Rs 5
			break
	newemp=Employee()
	ademp=open("employee.txt","r")
	while True :
		line = ademp.readline()
		newemp.addConsumer(line)
		if ("" == line):
			break
	newadm=Admin()
	adadm=open("admin.txt","r")
	while True :
		line = adadm.readline()
		newemp.addAdmin(line)
		if ("" == line):
			break
	