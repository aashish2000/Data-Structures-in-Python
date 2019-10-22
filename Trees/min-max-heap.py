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

arr=[9,8,7,6,5,4,3,2,1]
build_min_heap(arr)
print(arr)

arr2=[1,2,3,4,5,6,7]
build_max_heap(arr2)
print(arr2)
