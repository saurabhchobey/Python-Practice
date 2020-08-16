def bintodec(binary):
	binary1=binary
	decimal=0
	i=0
	dec=0
	while(binary1!=0):
		dec=binary1%10
		decimal=decimal+dec*pow(2,i)
		binary1=binary1//10
		i=i+1
	print(decimal)

bintodec(11)
