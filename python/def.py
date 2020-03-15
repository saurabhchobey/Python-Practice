def banka(p,t,tax):
	amount1=p+(p*t)/100+(tax*p)/100
	return amount1
	print("total amount","=",amount1)

p=int(input("principle:"))
t=int(input("tenur:"))
tax=int(input("tax:"))
banka(p,t,tax)
def bankb(p1,t2,tax2):
	amount=p1+(p1*t2)/100+(tax2*p1)/100
	return amount
	print("total amount","=",amount)
    
p1=int(input("principle:"))
t2=int(input("tenure:"))
tax2=int(input("tax:"))
bankb(p1,t2,tax2)

bankaa=banka(p,t,tax)
bankbb=bankb(p1,t2,tax2)
if bankaa>bankbb:
	print("bank a is baest")
else:
	print("bankb is beat")
		


