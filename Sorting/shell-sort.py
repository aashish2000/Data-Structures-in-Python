def shellSort(arr):
	n=len(arr)
	gap=n//2

	while gap>0:
		for i in range(gap,n):
			temp=arr[i]
			for j in range(i,gap-1,-gap):
				if(arr[j-gap]>temp):
					arr[j],arr[j-gap]=arr[j-gap],arr[j]

		gap//=2	
	return(arr)
arr=[8,1,2,3,0,5,9]

print(shellSort(arr))