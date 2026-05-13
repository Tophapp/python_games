number1 = int(input("First Number Goes Here "))
number2 = int(input("Second Number Goes Here "))
multi2 = []
multi1 = ["g1""3"]
g = 0
for i in range(1,3000):
	c = (number1 * i)
	i1 = str(i)
	c1 = str(c)
	c3 = c1
	#c3 = (f"{number1}*{i1} = " + c1)
	multi1.append(c3)
	#print(f"{multi1},{i}")
	#print(f"{number1 * i},{i}")
for x in range(1,3000):
	d = (number2 * x)
	x1 = str(x)
	d1 = str(d)
	#d3 = (f"{number2}*{x1} = " + d1)
	d3 = d1
	multi2.append(d3)
	#print(f"{multi2},{x}")
	#print(f"{number2 * x},{x}")
a = str(multi1)
b = str(multi2)
#print(a)
#print( )
#print(b)
for y in range(1, len(multi1)):
	g = (y * number2)
	g1 = str(g)
	yes = (g1 in multi1)
	yes1 = str(yes)
	if g1 in multi1:
		print(f"{g} is a common multiple of {number1} & {number2}")