import random
import time

start = time.time()
def mergeSort(n):

	start = time.time()
	print("Splitting ",n)
	if len(n)>1:
		mid = len(n)//2
		lefthalf = n[:mid]
		righthalf = n[mid:]

		mergeSort(lefthalf)
		print('\n')
		print('lefthalf:',lefthalf)
		print('righthalf:',righthalf)
		print('\n')
		mergeSort(righthalf)
		i=j=k=0       
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				n[k]=lefthalf[i]
				i=i+1
			else:
				n[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			n[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			n[k]=righthalf[j]
			j=j+1
			k=k+1
		print("Merging ",n)
n = [random.randint(0,100000)for i in range(100000)]

mergeSort(n)
stop = time.time()
runtime = stop - start
print(n)
print('runtime:',runtime)
