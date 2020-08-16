def dectobin(val):
	if val>1:
		dectobin(val//2)
	print(val% 2, end = '')


	



dectobin(24)