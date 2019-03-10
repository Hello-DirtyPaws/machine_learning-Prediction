from random import* 

f = open("x.csv", "w")


for i in range(100):
	x = randint(1, 100)
	f.write(str(x))
	f.write('\n')
