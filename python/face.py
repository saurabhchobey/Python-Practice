
from random import random

def flip():
	r=random()
	if r>0.5:
		return "head"
	else:
		return "tail"

print(flip())