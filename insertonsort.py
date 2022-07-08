INSERTION SORT

def insertionSort(arr):
for i in range(1, len(arr)):
  key = arr[i]
 j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])

  SELECTION SORT
 
import sys
A = [64, 25, 12, 22, 11]
for i in range(len(A)):
	
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
			
	A[i], A[min_idx] = A[min_idx], A[i]

print ("Sorted array")
for i in range(len(A)):
	print("%d" %A[i],end=" ")

MERGE SORT
def mergeSort(arr):
	if len(arr) > 1:

		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		mergeSort(L)
		mergeSort(R)

		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1Ṃ
def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is", end="\n")
	printList(arr)
	mergeSort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)

  QUICK SORT
def partition(array, low, high):
pivot = array[high]
i = low - 1
for j in range(low, high):
	if array[j] <= pivot:
	i = i + 1
	(array[i], array[j]) = (array[j], array[i])
(array[i + 1], array[high]) = (array[high], array[i + 1])
return i + 1

def quick_sort(array, low, high):
if low < high:
	pi = partition(array, low, high)
	quick_sort(array, low, pi - 1)
	quick_sort(array, pi + 1, high)

array = [ 10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)

print(f'Sorted array: {array}')
	
COUNTING SORT
def countSort(arr):
	output = [0 for i in range(len(arr))]
	count = [0 for i in range(256)]

	ans = ["" for _ in arr]

	for i in arr:
		count[ord(i)] += 1
	for i in range(256):
		count[i] += count[i-1]

	for i in range(len(arr)):
		output[count[ord(arr[i])]-1] = arr[i]
		count[ord(arr[i])] -= 1

	for i in range(len(arr)):
		ans[i] = output[i]
	return ans
arr = "geeksforgeeks"
ans = countSort(arr)
print("Sorted character array is % s" %("".join(ans)))

HEAP SORT
def heapify(arr, n, i):
	largest = i 
	l = 2 * i + 1
	r = 2 * i + 2	 
	if l < n and arr[largest] < arr[l]:
		largest = 1
	if r < n and arr[largest] < arr[r]:
		largest = r
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] 
		heapify(arr, n, largest)
def heapSort(arr):
	n = len(arr)
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
	print("%d" % arr[i],end=" ")



