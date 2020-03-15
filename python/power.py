# n=int(input())
# list=[]
# for i in range(0,n):
# 	ele=int(input())
# 	list.append(ele)
# 	list.sort()


# print(' '.join(map(str,list)))
# c=int(input())
# print(list[c])
# print(list,sorted(list),[-2])
f=int(input())
a=int(input())
b=int(input())
c1=2
c2=3
list=[]
for i in range(f):
	if i%2==0:
		list.append(a);
		list.append(b);
		print(a,b,end=' ')
		a=a*c1
		b=b*c2

n=int(input())
		# print(list)

	

print("nth term",list[n+1])

	# else:
	# 	print(b,a)
	# 	a=a*c1
	# 	b=b*c2
	# i=i+1


