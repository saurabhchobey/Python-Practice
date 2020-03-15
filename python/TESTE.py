amount1=int(input())
amount2=int(input())
amount3=int(input())
rate1=int(input())
rate2=int(input())
rate3=int(input())
if 0<=amount1<=300000 and 0<=amount2<=300000 and 0<=amount3<=300000:
	total2 =amount2*rate1
	total1=amount1*rate1
	total3=amount3*rate1


	print(total1,total2,total3)
elif 600000>amount1>300000 or 600000>amount2>300000 or 600000>amount3>300000:

	total1=amount1*rate2
	total2=amount2*rate2
	total3=amount3*rate2
	print(total1,total2,total3)
elif 600000<amount1<900000 or 600000<amount3<900000 or 600000<amount2<900000:
	total1=amount1*rate2
	total2=amount2*rate2
	total3=amount3*rate2
	print(total1,total2,total3)

elif amount1>900000 or amoun2>900000 or amount3>900000:
	total1=amount1*rate2
	total2=amount2*rate2
	total3=amount3*rate3
	print(total1,total2,total3)


new=total1+total2+total3
print(new)


