def countingSort(arr,exp):
	arr=arr[::-1]
	digarr=[]
	bucket=[0]*10

	for i in range(len(arr)):
		try:
			dig=int(str(arr[i])[-exp])
		except:
			dig=0
		#print("dig: ",dig)
		digarr.append(dig)
		bucket[dig]+=1

	for i in range(1,10):
		bucket[i]+=bucket[i-1]

	#print(digarr,bucket)
	sortedarr=[0]*len(arr)

	for i in range(len(arr)):
		sortedarr[bucket[digarr[i]]-1]=arr[i]
		bucket[digarr[i]]-=1

	return(sortedarr)

def radixSort(arr):
	val=len(str(max(arr)))
	for i in range(val):
		arr=countingSort(arr,(i+1))
	return(arr)

print(radixSort([1000,170,45,75,90,802,24,2,66]))



	

