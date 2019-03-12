l=[1,2,3,4]
try:
	s=len(l)
	if s >4: 
		raise TypeError
	print(l[1])


except TypeError:
	print("the length of the list should be less than 4")
except IndexError:
	print("index out of range")

else:
	for i in l:
		print(l)	

finally:
	print("execution completed")
