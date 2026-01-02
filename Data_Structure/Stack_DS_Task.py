class Stack:
    """
    Implement Stack using List. 
    Stack : class with attributes : 
        top -> point the available next position
        size -> refer to the size of a stack 
        lisk -> container for the data 
    """
    def __init__(self):
        self.top=0
        self.size=10
        self.list=[None]*self.size
    def push_data(self,d):
        if self.top <= self.size :
            self.list[self.top]=d
            self.top=self.top+1
        else : 
            print('Stack is Full.')    
    def pop_data(self):
        if self.top == 0 : 
            return 'Stack is Empty.'
        else : 
            self.top-=1
            return self.list[self.top]
    def display_stack(self):
        print(self.list[:self.top])


s=Stack()
s.push_data(10)
s.push_data(20)
s.push_data(30)
s.push_data(40)
s.push_data(50)

s.display_stack()
print(f'{s.pop_data()}')
s.display_stack()