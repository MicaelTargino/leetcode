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


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.print_stack()

    stack.pop()

    stack.print_stack()
