n=int(input())
list=[]

for i in range(0,n-1):
	temp=int(input())



	list.append(temp)
	temp=temp+1
	print(list)
print(sorted(list)[-2])






string = input("Enter the tring:")
if(string == string[::-1]):
	print("The string is a palindrome")
else:
	print("The string is not a palindrome")