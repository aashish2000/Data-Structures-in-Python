class Node:
	def __init__(self,val):
		self.data=val
		self.left=None
		self.right=None

def morris(head):
	while(head is not None):
		if(head.left is None):
			print(head.data,end=" ")
			head=head.right
		else:
			ptr=head.left
			while(ptr.right is not None and ptr.right!=head):
				ptr=ptr.right
			if(ptr.right is None):
				ptr.right=head
				head=head.left
			else: 
				ptr.right = None
				print(head.data,end=" ") 
				head = head.right 

head=Node(4)
head.left=Node(2)
head.right=Node(6)
head.left.left=Node(1)
head.left.right=Node(3)
head.right.right=Node(7)
head.right.left=Node(5)
morris(head)
