
import random
import time

def insertionSort():
	a = ''
	a = input('Input range to sort or (Q)')
	while a != 'Q':
		start = time.time()
		n = [random.randint(0,10) for iter in range(10)]
		for i in range(1,len(n)):
			current_value = n[i]
			pos = i
			while pos>0 and n[pos-1]>current_value:
				n[pos]=n[pos-1]
				pos = pos-1

			n[pos]=current_value
		stop = time.time()
		runtime = stop - start
		print(n)
		print("runtime:",runtime)
	
	record = []
	record.append(runtime)
	print(record)


insertionSort()




