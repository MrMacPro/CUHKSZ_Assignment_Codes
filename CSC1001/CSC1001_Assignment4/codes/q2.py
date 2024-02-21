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
        #The same as q1
        new_node = Node(data, None)
        if self.size==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.pointer=new_node
            self.tail=new_node
        self.size+=1
        # End writing your code.


    ## Here you can write some other functions inside the class if needed, or you can igore this block.
    # Start writing your code.
    
    # End writing your code.
    

def quick_sort(node):
    # Start writing your code.
    def sort(lst):
        if lst.size==1:
            return lst
        elif lst.size==2:
            if lst.head.element>lst.tail.element:
                temp=lst.head.element
                lst.head.element=lst.tail.element
                lst.tail.element=temp
            return lst
        else:    #Only sort if node is not None
            smaller=SinglyLinkedList()  #Init a linked list storing elements smaller than original list
            larger=SinglyLinkedList()   #Init a linked list storing elements larger than original list
            current=lst.head.pointer    #Start traverse throughout the linked list
            pivot=lst.head.element  #Define pivot to be the first element
            while current:
                if current.element<pivot:    #If current element is smaller than pivot,
                    smaller.insert(current.element) #add this element to smaller linked list
                else:                        #If current element is larger than pivot,
                    larger.insert(current.element)  #add this element to larger linked list
                current=current.pointer #Go to next element

            #Get sorted sub linked lists
            output=SinglyLinkedList()
            if smaller.size==0:
                if larger.size==0:
                    output.insert(pivot)    #If smaller and larger are all empty, output pivot only.
                    return output
                else:
                    smaller.insert(pivot)   #If smaller is empty only, plug pivot into smaller.
            else:
                if larger.size==0:
                    larger.insert(pivot)    #If larger is empty only, plug pivot into larger.
                else:
                    smaller.insert(pivot)   #If none is empty, plug pivot into smaller.
            sorted_smaller=sort(smaller)    #Sort smaller
            sorted_larger=sort(larger)      #Sort larger

            #Combine smaller and larger
            sorted_smaller.tail.pointer=sorted_larger.head
            output.head=sorted_smaller.head
            output.tail=sorted_larger.tail
            output.size=sorted_smaller.size+sorted_larger.size
            
            return output

    lst=SinglyLinkedList()
    current=node
    while current:
        lst.insert(current.element)
        current=current.pointer
    return sort(lst).head
    # End writing your code.


# We will write code as follows to check your answer. You can remain or delete the following code in the submission. Because the following code will be rewritten when checking your answer.
if __name__ == '__main__':
    test_list = SinglyLinkedList()
    nums = [12,52,34,35,93,56,12,90]  # An example. We will change it during testing.
    for num in nums:
        test_list.insert(num)
    first_node = test_list.head  # Get the first node of the linked list.
    p = quick_sort(first_node)
    while p.pointer != None:
        print(p.element)
        p = p.pointer
    print(p.element)