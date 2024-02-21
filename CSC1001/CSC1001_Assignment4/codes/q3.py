"""
You are only permitted to write code between Start and End.
Don't change the template. Otherwise, you will get zero point.
Don't write any `print` function in your code. 
"""


## Here you can write some extra code if needed, or you can igore this block.
# Start writing your code.
#Create a stack class
class stack:
    def __init__(self):
        self.data=[]
    def push(self,x):
        self.data.append(x)
    def pop(self):
        return self.data.pop()
    def all_basic_steps(self):
        flag=True
        for i in self.data:
            if i[0]!=1:
                flag=False
        return flag
# End writing your code.


def HanoiTower(n, from_rod ='A',aux_rod ='B',to_rod ='C'):
    result_list = []
    # Start writing your code.
    stack1=stack()  #Create 2 stacks to operate with
    stack2=stack()
    stack1.push((n, from_rod ,aux_rod ,to_rod)) #push the target into 1 stack
    while not stack1.all_basic_steps(): #Continue processing as long as there are non-basic steps
        while stack1.data!=[]:  #Process all steps in stack1
            step=stack1.pop()   #Get next step to process
            if step[0]==1:      #If step is already a basic step, plug into processed stack directly.
                stack2.push((step[0], step[1], step[2], step[3]))
            else:               #If step is not a basic step, break it down into 3 steps.
                stack2.push((step[0]-1, step[1], step[3], step[2]))
                stack2.push((1, step[1], step[2], step[3]))
                stack2.push((step[0]-1, step[2], step[1], step[3]))
        while stack2.data!=[]:  #Reorder the steps in stack1
            stack1.push(stack2.pop())
    while stack1.data!=[]:  #Reorder to correct output
        stack2.push(stack1.pop())
    for i in stack2.data:   #Decode all basic steps into standard format
        result_list.append({'from': i[1], 'to': i[3]})
    # End writing your code.
    return result_list


"""
You should store each line your output in result_list defined above.
For example, if the steps of your HanoiTower are: 
                A --> C
                A --> B
then you must store them in result_list by writing: 

step = {'from': 'A', 'to': 'C'}
result_list.append(step)
step = {'from': 'A', 'to': 'B'}
result_list.append(step)

Thus, once you determine one step, please store it in a dict which includes keys 'from' and 'to', and then add the dict to the result_list. 

Don't write any `print()` function in your code, since we only write code as follows to check your answer. You can remain or delete the following code in the submission. Because the following code will be rewritten when checking your answer.
"""
if __name__ == '__main__':
    n = 10  # An example. We will change it during testing.
    result_list = HanoiTower(n)
    for step in result_list:
        print(step['from'], '-->', step['to'])
