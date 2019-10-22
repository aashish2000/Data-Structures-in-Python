class Node:
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data


def insert(head,temp,val):
	if(temp is None):
		head=Node(val)
		return(head)
	else:
		if(val>temp.data and temp.right is not None):
			return(insert(head,temp.right,val))

		elif(val>temp.data and temp.right is None):
			temp.right=Node(val)
			return(head)

		if(val<temp.data and temp.left is not None):
			return(insert(head,temp.left,val))

		elif(val<temp.data and temp.left is None):
			temp.left=Node(val)
			return(head)

def minNode(head):
	if(head.left is None and head.right is None):
		return(head.val)
	else:
		return(minNode(head.left))

def search(head,val):
	if(head is None or head.data==val):
		return(head)
	elif(head.data>val):
		return(search(head.left,val))
	else:
		return(search(head.right,val))

def delete(head,val):
	if(head is None):
		return(head)
	elif(val<head.data):
		head.left=delete(head.left,val)
	elif(val>head.data):
		head.right=delete(head.right,val)
	else:
		if(head.right is None and head.left is None):
			head=None
		elif(head.right is None):
			head=head.left
		elif(head.left is None):
			head=head.right
		else:
			head.data=minNode(head.right)
			head.right=delete(head.right,head.data)

	return(head)

def inorder(head): 
    if head: 
        inorder(head.left) 
        print(head.data) 
        inorder(head.right) 


head=None

for i in range(5):
	head=insert(head,head,i+1)

inorder(head)

if(search(head,3)!=None):
	print("Found")
else:
	print("Not Found")


if(delete(head,3)!=None):
	print("Deleted")
else:
	print("Null")

inorder(head)
