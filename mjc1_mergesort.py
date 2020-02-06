import random
import time
import matplotlib.pyplot as plt
import numpy as np

a = [random.randint(0,10) for iter in range(10)]
b = [random.randint(0,100) for iter in range(100)]
c = [random.randint(0,1000) for iter in range(1000)]
d = [random.randint(0,5000) for iter in range(5000)]

def a_mergeSort(a):

	start = time.time()
	print("Splitting ",a)
	if len(a)>1:
		mid = len(a)//2
		lefthalf = a[:mid]
		righthalf = a[mid:]

		a_mergeSort(lefthalf)
		print('\n')
		print('lefthalf:',lefthalf)
		print('righthalf:',righthalf)
		print('\n')
		a_mergeSort(righthalf)
		i=j=k=0       
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				a[k]=lefthalf[i]
				i=i+1
			else:
				a[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			a[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			a[k]=righthalf[j]
			j=j+1
			k=k+1
		print("Merging ",a)

def b_mergeSort(b):

	start = time.time()
	print("Splitting ",b)
	if len(b)>1:
		mid = len(b)//2
		lefthalf = b[:mid]
		righthalf = b[mid:]

		b_mergeSort(lefthalf)
		print('\n')
		print('lefthalf:',lefthalf)
		print('righthalf:',righthalf)
		print('\n')
		b_mergeSort(righthalf)
		i=j=k=0       
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				b[k]=lefthalf[i]
				i=i+1
			else:
				b[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			b[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			b[k]=righthalf[j]
			j=j+1
			k=k+1
		print("Merging ",b)

def c_mergeSort(c):

	start = time.time()
	print("Splitting ",c)
	if len(c)>1:
		mid = len(c)//2
		lefthalf = c[:mid]
		righthalf = c[mid:]

		c_mergeSort(lefthalf)
		print('\n')
		print('lefthalf:',lefthalf)
		print('righthalf:',righthalf)
		print('\n')
		c_mergeSort(righthalf)
		i=j=k=0       
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				c[k]=lefthalf[i]
				i=i+1
			else:
				c[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			c[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			c[k]=righthalf[j]
			j=j+1
			k=k+1
		print("Merging ",c)

def d_mergeSort(d):

	start = time.time()
	print("Splitting ",d)
	if len(d)>1:
		mid = len(d)//2
		lefthalf = d[:mid]
		righthalf = d[mid:]

		d_mergeSort(lefthalf)
		print('\n')
		print('lefthalf:',lefthalf)
		print('righthalf:',righthalf)
		print('\n')
		d_mergeSort(righthalf)
		i=j=k=0       
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				d[k]=lefthalf[i]
				i=i+1
			else:
				d[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			d[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			d[k]=righthalf[j]
			j=j+1
			k=k+1
		print("Merging ",d)

def timer():
	tL = []
	#rangeL = [10]
	n = input("\nChoose range to sort or [Q] to quit:"
		"\na = range 10"
		"\nb = range 100"
		"\nc = range 1000"
		"\nd = range 5000"
		"\n== ")
	while n != 'Q':
		if n == 'a':
			start = time.time()
			a_mergeSort(a)
			stop = time.time()
			runtime_a = stop - start
			tL.append(runtime_a)
			print(a)
			print("runtime:",runtime_a)
			n = input("\nChoose range to sort or [Q] to quit:"
		"\na = range 10"
		"\nb = range 100"
		"\nc = range 1000"
		"\nd = range 5000"
		"\n== ")

		if n == 'b':
			start = time.time()
			b_mergeSort(b)
			stop = time.time()
			runtime_b = stop - start
			tL.append(runtime_b)
			print(b)
			print("runtime:",runtime_b	)
			n = input("\nChoose range to sort or [Q] to quit:"
		"\na = range 10"
		"\nb = range 100"
		"\nc = range 1000"
		"\nd = range 5000"
		"\n== ")

		if n == 'c':
			start = time.time()
			c_mergeSort(c)
			stop = time.time()
			runtime_c = stop - start
			tL.append(runtime_c)
			print(c)
			print("runtime:",runtime_c)
			n = input("\nChoose range to sort or [Q] to quit:"
		"\na = range 10"
		"\nb = range 100"
		"\nc = range 1000"
		"\nd = range 5000"
		"\n== ")

		if n == 'd':
			start = time.time()
			d_mergeSort(d)
			stop = time.time()
			runtime_d = stop - start
			tL.append(runtime_d)
			print(d)
			print("runtime:",runtime_d)
			n = input("\nChoose range to sort or [Q] to quit:"
		"\na = range 10"
		"\nb = range 100"
		"\nc = range 1000"
		"\nd = range 5000"
		"\n== ")

		elif n == 'Q':
			print(tL)
			x = [1,2,3,4]
			y = tL
			plt.plot(x,y, label = 'linear')
			plt.legend()
			plt.show()
			'''plt.rcParams["figure.figsize"] = (8, 8)	
			fig, ax = plt.subplots()

			ax.plot(40,tL)
			plt.legend()
			plt.show()'''
		else:
			print('invalid input')
			n = input("\nChoose range to sort or [Q] to quit:"
		"\na = range 10"
		"\nb = range 100"
		"\nc = range 1000"
		"\nd = range 5000"
		"\n== ")
		
timer()