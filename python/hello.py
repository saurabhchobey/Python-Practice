a=float(input("enter a:"))
b=float(input("enter b:"))
c=float(input("enter c"))
if a>b and a>c:
	print("a is greatest")
elif b>a and b>c:
	print("b is greatest")
elif a==b and a==c:
	print("equql")
else:
	print("c is greatest")