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
    
    def top(self):
        return self.stack_list[len(self.stack_list)-1] if self.stack_list else None

def next_greater_element(arr):
    stack = Stack()
    result = [-1] * len(arr)  # Initialize result with -1
    
    for i in range(len(arr) - 1, -1, -1):  # Traverse from right to left
        # Remove all elements smaller than or equal to the current element
        while stack.size() > 0 and stack.top() <= arr[i]:
            stack.pop()
        
        # If stack is not empty, the top is the next greater element
        if stack.size() > 0:
            result[i] = stack.top()
        
        # Push current element onto the stack
        stack.push(arr[i])
    
    return result

if __name__ == '__main__':
    print(next_greater_element([1,2,3]))
    print(next_greater_element([5,2,3,6,3,1,0,54]))
    print(next_greater_element([5,3,1]))