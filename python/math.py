def banka(p,r,t):
	emi=p+t+r
	return emi
	print(emi)
	

p=float(input("enter:"))
r=float(input("enterr:"))
t=float(input("entert:"))	

banka(p,r,t)

def bankb(p1,r2,t3):
	emi2=p1+r2+t3
	return emi2
	print(emi2)
	

p1=float(input("enterp1:"))
r2=float(input("enterr2:"))
t3=float(input("entert3:"))

bankb(p1,r2,t3)


banka=banka(p,r,t)
bankb=bankb(p1,r2,t3)

if banka>bankb:
	print("ais batter")
else:
	print("b is better")