class mydatabase:
	def __init__(self):
		self.username=[]
		self.password=[]
	
	def add(self,username,password):
		self.username.append(username)
		self.password.append(password)

	def printUser(self):
		print(self.username)

	def delete(self,username):
		if username in self.username:
			for i in range(0,len(self.username)):
				if username==self.username[i]:
					self.username.pop(i)
					self.password.pop(i)

if __name__=='__main__':
	app=mydatabase()
	app.add('aks','123')
	app.printUser()
	app.delete('aks')
	app.printUser()