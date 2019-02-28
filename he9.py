import random
l = ["r","s","p"]
us = 0 
cs = 0
d = {'r':'rock','s':'scissor','p':'paper'}
while True:
	u = input("enter your choice,press n to discontinue")
	print("user chooses",u)
	if u in d:
		print(u,d[u])

	if u == "n":
		print("gameover")
		print("user score ",us)
		print("comp score ",cs)
		if us > cs:
			print("user wins")
		elif cs > us:
			print("comp wins")
		else:
			print("tie") 
		exit()

	c = random.choice(l)
	print("computer chooses",c)
	if c in d:
		print(c,d[c])

	if u == c:
		print("tie")
	elif u == "r" and c == "s":
		print("user wins")
		us=us+1
	elif u == "r" and c == "p":
		print("computer wins")
		cs=cs+1
	elif u == "p" and c == "r":
		print("user wins")
		us=us+1
	elif u == "s" and c == "r":
		print("computer wins")
		cs=cs+1
	elif u == "s" and c == "p":
		print("user wins")
		us=us+1
	elif u =="p" and c == "s":
		print("comp wins")
		cs=cs+1
	else:
		print("invalid")