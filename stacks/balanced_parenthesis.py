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

def is_balanced_parenthesis(expression: str) -> bool: 
    stack = Stack()

    matching_char = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in expression: 
        if char in "({[": # opening characters 
            stack.push(char)
        elif char in "}])":
            if stack.size() <= 0 or stack.top() != matching_char[char]:
                return False 
            stack.pop()
        
    return stack.size() == 0

if __name__ == "__main__":
    print(is_balanced_parenthesis("[{()}]")) # True
    print(is_balanced_parenthesis("[{()]")) # False
    print(is_balanced_parenthesis("}")) # False 
    print(is_balanced_parenthesis("[[[()]]]")) # True 