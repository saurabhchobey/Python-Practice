n=int(input())
list=[]



for i in range(n-1):
	a=int(input())
	list.append(a)

print(' '.join(map(str,list)))
list.sort()
j=0
while(j<=(n-2)):
	
	if list[j]==list[j+1]:
		list.pop(j)
	j=j+1
	print(list.pop(j)) 