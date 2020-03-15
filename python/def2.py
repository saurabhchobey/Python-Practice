def square(num,x):
	kkr=num*x
	return kkr
	print(kkr)

num=int(input("enter"))
x=int(input("enter"))	
square(num,x)	

y=square(num,x)
if y>1:
	print(y)
	x=x+1
else:
	print("erreor")