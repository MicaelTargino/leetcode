class Stack():
    def __init__(self):
        self.main_stack = [] 
        self.min_stack = []
    
    def size(self):
        return len(self.main_stack)
    
    def push(self, element):
        self.main_stack.append(element)
        
        # Push to min_stack if it's the first element or smaller than the current minimum
        if not self.min_stack or element <= self.min_stack[-1]:
            self.min_stack.append(element)
    
    def pop(self): 
        if self.size() == 0:
            raise IndexError("Stack is empty!")
        
        # If the top of main_stack matches the top of min_stack, pop from both
        if self.main_stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        return self.main_stack.pop()

    def print_stack(self):
        print("-------------")
        for item in reversed(self.main_stack):  # Reverse for stack visualization
            print(item)
        print("-------------")
    
    def top(self):
        if not self.main_stack:
            raise IndexError("Stack is empty!")
        return self.main_stack[-1]
    
    def get_min(self):
        if not self.min_stack:
            raise IndexError("Stack is empty!")
        return self.min_stack[-1]


if __name__ == "__main__":
        # Initialize the stack
        stack = Stack()
        
        # Test push operation
        stack.push(5)
        stack.push(3)
        stack.push(7)
        stack.push(2)
        stack.push(8)

        # Print the stack
        print("Stack after pushes:")
        stack.print_stack()

        # Test get_min operation
        print("Current minimum:", stack.get_min())  # Expected: 2

        # Test pop operation
        print("Popped element:", stack.pop())  # Expected: 8
        print("Popped element:", stack.pop())  # Expected: 2

        # Print the stack
        print("Stack after pops:")
        stack.print_stack()

        # Test get_min after pops
        print("Current minimum:", stack.get_min())  # Expected: 3

        # Test top operation
        print("Current top:", stack.top())  # Expected: 7
