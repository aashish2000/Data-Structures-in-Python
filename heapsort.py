def max_heapify(arr,ind):
	left=2*ind+1
	right=2*ind+2
	maxval=ind

	if(left<len(arr) and arr[maxval]<arr[left]):
		maxval=left
	if(right<len(arr) and arr[maxval]<arr[right]):
		maxval=right
	if(maxval!=ind):
		arr[ind],arr[maxval]=arr[maxval],arr[ind]
		max_heapify(arr,maxval)

def build_max_heap(arr):
	for i in reversed(range(len(arr)//2)):
		max_heapify(arr,i)

def min_heapify(arr,ind):
	left=2*ind+1
	right=2*ind+2
	minval=ind

	if(left<len(arr) and arr[minval]>arr[left]):
		minval=left
	if(right<len(arr) and arr[minval]>arr[right]):
		minval=right
	if(minval!=ind):
		arr[ind],arr[minval]=arr[minval],arr[ind]
		min_heapify(arr,minval)

def build_min_heap(arr):
	for i in reversed(range(len(arr)//2)):
		min_heapify(arr,i)

def heapsortdesc(input_arr):
	arr=[x for x in input_arr]
	build_max_heap(arr)
	sortedarr=[]
	lenarr=len(arr)

	while(lenarr>0):
		sortedarr.append(arr[0])
		arr[0]=arr[-1]
		arr.pop()
		max_heapify(arr,0)
		lenarr-=1

	return(sortedarr)

def heapsort(input_arr):
	arr=[x for x in input_arr]
	build_min_heap(arr)
	sortedarr=[]
	lenarr=len(arr)

	while(lenarr>0):
		sortedarr.append(arr[0])
		arr[0]=arr[-1]
		arr.pop()
		min_heapify(arr,0)
		lenarr-=1

	return(sortedarr)



arr=[9,8,7,3,6,4,2,1]

print(heapsortdesc(arr))
print(heapsort(arr))