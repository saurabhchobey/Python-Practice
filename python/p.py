#!/bin/python3

n=int(input())


if n%2!=0  :
    print("Weird")
elif n%2!=1 or 2<n<5:
   print("Not Weird")
elif n%2!=1 and 6<n>20:
    print("Weird")
elif n%2!=1 or n>20:
    print("Not Weird")


    
