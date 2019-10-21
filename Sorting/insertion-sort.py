def insertionSort(arr):
	n=len(arr)
	for i in range(1,n):
		for j in range(i,0,-1):
			if (arr[j]<arr[j-1]):
				arr[j],arr[j-1]=arr[j-1],arr[j]
	return(arr)

arr=[9,8,7,6,5,4,3]
print(insertionSort(arr))


