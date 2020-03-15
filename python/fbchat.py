class detail():
	active_users=0
	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age
		self.active_users +=1

	def fullname(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]} {self.last[0]}"

	def likes(self):
		return f"{self.first} likes icecream"

	def birthday(self):
		if self.age<=40:
			return f"happy {self.age}th birthday {self.first}"

	def logout(self):
		return f"{self.first} is logout"
print(detail.active_users)
user1=detail("joe" , "blanca" ,38)
user2=detail("prakshee","rajpurohit",21)
print(detail.active_users)
print(user2.fullname())
print(user2.likes())

print(user2.birthday())
