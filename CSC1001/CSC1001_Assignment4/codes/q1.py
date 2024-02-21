"""
You are only permitted to write code between Start and End.
Don't change the template. Otherwise, you will get zero point.
"""


## Here you can write some extra code if needed, or you can igore this block.
# Start writing your code.

# End writing your code.


class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        # Start writing your code.
        new_node = Node(data, None) #Create a new node instance
        if self.size==0:    #If the linked list is empty
            self.head=new_node  #Assign head and tail to new node
            self.tail=new_node
        else:   #If it is not empty
            self.tail.pointer=new_node  #Assign the pointer of current tail to new node
            self.tail=new_node  #Assign tail to new node
        self.size+=1    #Update the size of linked list
        # End writing your code.
    
    
    ## Here you can write some other functions inside the class if needed, or you can igore this block.
    # Start writing your code.

    # End writing your code.


def count_node(node):
    # start writing your code.
    if node is None:    #Base case: No node
        return 0
    if node.pointer is None:    #Base case: Last node
        return 1
    else:   #Recursive case: Not last node
        return 1 + count_node(node.pointer)
    # end writing your code.


# We will write code as follows to check your answer. You can remain or delete the following code in the submission. Because the following code will be rewritten when checking your answer.
if __name__ == '__main__':
    test_list = SinglyLinkedList()
    nums = [4,2,3,1,0,-1]  # An example. We will change it during testing.
    for num in nums:
        test_list.insert(num)
    first_node = test_list.head  # Get the first node of the linked list.
    print('The number of nodes in test_list is:')
    print(count_node(first_node))

