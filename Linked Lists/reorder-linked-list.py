class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

def reverse(head):
	prev=None
	curr=head

	while(curr is not None):
		temp=curr.next
		curr.next=prev
		prev=curr
		curr=temp
	return(prev)


def reorder(head):
	hare=head
	tortoise=head

	while(hare.next is not None and hare.next.next is not None):
		tortoise=tortoise.next
		hare=hare.next.next

	head2=tortoise.next
	tortoise.next=None
	head2=reverse(head2)

	'''print("part1:",end=" ")
	printNode(head)
	print("part2:",end=" ")
	printNode(head2)'''
	
	#print("e: ",head.data,head2.data)
	list1=head
	list2=head2
	while(head is not None and head2 is not None):
		
		temp=head.next
		temp1=head2.next
		head.next=head2
		head2.next=temp
		head=temp
		head2=temp1

	if(head2 is not None):
		head.next=head2

	return(list1)

def printNode(head):
	temp=head

	while(temp):
		print(temp.data,end=" ")
		temp=temp.next
	print("")

root=Node(1)
root.next=Node(2)
root.next.next=Node(3)
root.next.next.next=Node(4)
root.next.next.next.next=Node(5)

printNode(reorder(root))



