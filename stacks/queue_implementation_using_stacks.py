class Stack():
    def __init__(self):
        self.stack_list = [] 
    
    def size(self):
        return len(self.stack_list)
    
    def push(self, element):
        self.stack_list.append(element)
    
    def pop(self): 
        if self.size() == 0:
            raise IndexError("Stack is empty!")
        return self.stack_list.pop()

    def print_stack(self):
        print("-------------")
        for item in reversed(self.stack_list):  # Reverse for stack visualization
            print(item)
        print("-------------")

class Queue():
    def __init__(self):
        self.stack1 = Stack()  # Enqueue stack 
        self.stack2 = Stack()  # Dequeue stack 

    def push(self, element):
        self.stack1.push(element)
    
    def pop(self): 
        if self.stack2.size() == 0: 
            if self.stack1.size() == 0:
                raise IndexError("Queue is empty!")
            for i in range(self.stack1.size()):
                self.stack2.push(self.stack1.pop())                
        
        return self.stack2.pop()
    
    def print_queue(self): 
        print("Queue state:")
        print("-------------")
        print("Dequeue stack (stack2):")
        self.stack2.print_stack()
        print("Enqueue stack (stack1):")
        self.stack1.print_stack()
        print("-------------")

if __name__ == "__main__":
    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)

    print("Popped element:", queue.pop())  # Should return 1

    queue.print_queue()
