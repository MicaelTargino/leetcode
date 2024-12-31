class Stack():
    def __init__(self):
        self.queue1 = Queue()  # Primary queue
        self.queue2 = Queue()  # Auxiliary queue

    def push(self, value):
        self.queue1.push(value)

    def pop(self):
        if self.queue1.size() == 0:
            raise IndexError("Stack is empty!")

        # Transfer all elements except the last to queue2
        while self.queue1.size() > 1:
            self.queue2.push(self.queue1.pop())

        # The last element in queue1 is the top of the stack
        popped_value = self.queue1.pop()

        # Swap the roles of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_value

    def print_stack(self):
        print("Stack elements (top to bottom):")
        print("-------------")
        for item in reversed(self.queue1.queue_list):
            print(item)
        print("-------------")


class Queue():
    def __init__(self):
        self.queue_list = []

    def push(self, item):
        self.queue_list.append(item)

    def pop(self):
        if self.size() == 0:
            raise IndexError("Queue is empty!")
        return self.queue_list.pop(0)

    def size(self):
        return len(self.queue_list)


# Testing the Stack
if __name__ == "__main__":
    stack = Stack()

    # Test push operation
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Print stack
    stack.print_stack()  # Expected: 3 2 1

    # Test pop operation
    print("Popped element:", stack.pop())  # Expected: 3
    print("Popped element:", stack.pop())  # Expected: 2

    # Print stack after pops
    stack.print_stack()  # Expected: 1

    # Test pop operation on remaining element
    print("Popped element:", stack.pop())  # Expected: 1