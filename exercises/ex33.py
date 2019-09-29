
def looper(loopCounter, loopIncrementer):
	i = 1
	numbers = []

	while i <= loopCounter:
		print "At the top i is %d" % i
		numbers.append(i)
			
		i = i + loopIncrementer
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		

	print "The numbers: "
	for num in numbers: 
		print num	
		
		
looper(15,2)