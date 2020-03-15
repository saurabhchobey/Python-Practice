a=int(input())
rev=0
n=a

while(a!=0):
	rem=a%10
	rev=rev*10+rem
	a=int(a/10)



if(n==rev):
	print("palindrome")
else:
	print("not")

b=int(input())
fact=1
for i in range(1,b+1):
	fact=fact*i
	i=i+1
print(fact)


c=int(input())
d=int(input())
gcd=0
i=1
while(i<=c and i<=d):
	if c%i==0 and d%i==0:
		gcd=1
		i=i+1
print(gcd)
