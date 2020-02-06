
import random
import time
import matplotlib.pyplot as plt
import numpy as np



a = [random.randint(0,10) for iter in range(10)]
b = [random.randint(0,100) for iter in range(100)]
c = [random.randint(0,1000) for iter in range(1000)]
d = [random.randint(0,10000) for iter in range(1000)]



def a_insertionSort(a):
	start = time.time()

	for i in range(1,len(a)):
		current_value = a[i]
		pos = i
		while pos>0 and a[pos-1]>current_value:
			a[pos]=a[pos-1]
			pos = pos-1

		a[pos]=current_value

def b_insertionSort(b):
	start = time.time()

	for i in range(1,len(b)):
		current_value = b[i]
		pos = i
		while pos>0 and b[pos-1]>current_value:
			b[pos]=b[pos-1]
			pos = pos-1

		b[pos]=current_value

def c_insertionSort(c):
	start = time.time()

	for i in range(1,len(c)):
		current_value = c[i]
		pos = i
		while pos>0 and c[pos-1]>current_value:
			c[pos]=c[pos-1]
			pos = pos-1

		c[pos]=current_value

def d_insertionSort(d):
	start = time.time()

	for i in range(1,len(d)):
		current_value = d[i]
		pos = i
		while pos>0 and d[pos-1]>current_value:
			d[pos]=d[pos-1]
			pos = pos-1

		d[pos]=current_value

def timer():
	tL = []
	rangeL = [1,2,3,4]
	n = input("\nChoose range to sort or [Q] to quit:"
		"\na = range 10"
		"\nb = range 100"
		"\nc = range 1000"
		"\nd = range 10000"
		"\n== ")

	while n != 'Q' or 'q':
		if n == 'a':
			start = time.time()
			a_insertionSort(a)
			stop = time.time()
			runtime_a = stop - start
			tL.append(runtime_a)	
			print(a)
			print("runtime:",runtime_a)
			n = input("\nChoose range to sort or [Q] to quit:"
		"\na = range 10"
		"\nb = range 100"
		"\nc = range 1000"
		"\nd = range 10000"
		"\n== ")

		elif n == 'b':
			start = time.time()
			b_insertionSort(b)
			stop = time.time()
			runtime_b = stop - start
			tL.append(runtime_b)
			print(b)
			print("runtime:",runtime_b)
			n = input("\nChoose range to sort or [Q] to quit:"
		"\na = range 10"
		"\nb = range 100"
		"\nc = range 1000"
		"\nd = range 10000"
		"\n== ")

		elif n == 'c':
			start = time.time()
			c_insertionSort(c)
			stop = time.time()
			runtime_c = stop - start
			tL.append(runtime_c)
			print(c)
			print("runtime:",runtime_c)
			n = input("\nChoose range to sort or [Q] to quit:"
		"\na = range 10"
		"\nb = range 100"
		"\nc = range 1000"
		"\nd = range 10000"
		"\n== ")

		elif n == 'd':
			start = time.time()
			d_insertionSort(d)
			stop = time.time()
			runtime_d = stop - start
			tL.append(runtime_d)
			print(d)
			print("runtime:",runtime_d)
			n = input("\nChoose range to sort or [Q] to quit:"
		"\na = range 10"
		"\nb = range 100"
		"\nc = range 1000"
		"\nd = range 10000"
		"\n== ")
			
		elif n == 'Q' or 'q':
			quit()

		else:
			print('invalid input')
			n = input("\nChoose range to sort or [Q] to quit:"
		"\na = range 10"
		"\nb = range 100"
		"\nc = range 1000"
		"\nd = range 10000"
		"\n== ")

	print(tL)
	plt.rcParams["figure.figsize"] = (8, 8)

	fig, ax = plt.subplots()


	ax.plot(rangeL,tL)
	plt.legend()
	plt.show()
		
timer()


	