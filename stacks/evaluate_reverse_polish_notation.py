class Stack():
    def __init__(self):
        self.operands_stack = [] 
    
    def push_operand(self, element):
        self.operands_stack.append(element)
    
    def pop_operand(self): 
        if len(self.operands_stack) == 0:
            raise IndexError("Stack is empty!")
        return self.operands_stack.pop()

    def print_operands_stack(self):
        print("-------------")
        for item in reversed(self.operands_stack):  # Reverse for stack visualization
            print(item)
        print("-------------")
    
    def operands_top(self):
        return self.operands_stack[len(self.operands_stack)-1] if self.operands_stack else None

def evaluate_reverse_polish_notation(expression):
    stack = Stack()
    for char in expression:
        if char.isdigit():
            stack.push_operand(int(char))
        elif char in '+*/-':
            operand2 = stack.pop_operand()
            operand1 = stack.pop_operand()
            if char == '+':
                stack.push_operand(operand1 + operand2)
            elif char == '*':
                stack.push_operand(operand1 * operand2)
            elif char == '/':
                stack.push_operand(operand1/operand2)
            elif char == '-':
                stack.push_operand(operand1-operand2)
            
    return stack.operands_top()

    

if __name__ == "__main__":
    print(evaluate_reverse_polish_notation(["2", "1", "+", "3", "*"])) # 9