def selectionSort(arr):
	n=len(arr)
	for i in range(n-1):
		minind=i
		for j in range(i+1,n):
			if(arr[minind]>arr[j]):
				minind=j
		arr[i],arr[minind]=arr[minind],arr[i]
	return(arr)

arr=[4,7,5,8,6,3,19]

print(selectionSort(arr))