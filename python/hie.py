print("what operation you want")
operator=input("+,-,*,/:")
num1=int(input("enter the num1:"))
num2=int(input("enter th num2:"))
if operator=='+':
   print(num1,operator,num2,"=",num1+num2)
elif operator== '-':
   print(num1,operator,num2,"=",num1-num2)
elif operator=='*':
   print(num1,operator,num2,"=",num1*num2)
elif operator=='/':
   print(num1,operator,num2,"=",num1/num2)
else:

   print("error")