3 questions in assignment 4 is answered in q1.py, q2.py, and q3.py.
In q1.py,
    "insert" method is completed to insert a new node at the tail in the linked list.
    The function "count_node" work by traversing the linked list by continuously assigning the pointer to current cursor, and count once per step until reaches the end.

In q2.py,
    "insert" method is also completed to insert a new node at the head in the linked list.
    Then a quick sort is operated on a linked list. The detailed steps are as followed:
        -Choose the element at the head as the pivot.
        -Traverse the linked list, plug every element smaller than the pivot to "smaller" sub linked list, and plug every element larger than the pivot to "larger" sub linked list.
        -Recursively call the quick sort on "smaller" and "larger" sub linked list.
        -Merge "smaller" and "larger" sub linked list to form a sorted linked list.
    Get the head of sorted linked list (required by question).

In q3.py,
    First implement a stack class on list.
    Then break the step into several shorter steps.
    The order of the steps are the same as previous steps.
    Continuously operating these steps until all steps are basic steps.
    Decode the steps into required form.