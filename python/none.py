def shop(tax,rate,quantity):
	total=(rate*quantity)+tax
	return total

tax=int(input())
rate=int(input())
quantity=int(input())
shop(tax,rate,quantity)
#print(total)


def shopb(a,b,c):
	tt1=(a*b)+c
	return tt1

a=int(input())
b=int(input())
c=int(input())
shopb(a,b,c)

total=shop(tax,rate,quantity)
tt1=shopb(a,b,c)

if total>=tt1:
	print("shop is good")
else:
	print("shopb is good")
