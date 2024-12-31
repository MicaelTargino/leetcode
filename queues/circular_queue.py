class CircularQueue:
    def __init__(self, length=6):
        self.length = length
        self.base_list = [None] * length # Fixed size list 
        self.front_ptr = -1 # Points to the front element
        self.rear_ptr = -1 # Points to the rear element 

    def get_next_enqueue_index(self):
        return (self.rear_ptr + 1) % self.length
    
    def get_next_dequeue_index(self):
        return (self.front_ptr + 1) % self.length 

    def is_full(self):
        return self.get_next_enqueue_index() == self.front_ptr
    
    def is_empty(self):
        return self.front_ptr == -1
    
    def enqueue(self, value): 
        if self.is_full():
            self.resize()
        elif self.is_empty():
            self.front_ptr += 1
        self.rear_ptr = (self.rear_ptr + 1) % self.length
        self.base_list[self.rear_ptr] = value 
    
    def dequeue(self):
        if self.is_empty(): 
            print("Could not dequeue: Queue is empty!")
         
        temp = self.base_list[self.front_ptr]
        if self.front_ptr == self.rear_ptr:
            self.front_ptr = self.rear_ptr = -1
        else:
            self.front_ptr = (self.front_ptr + 1) % self.length
        
        return temp

    def peek(self):
        if self.is_empty():
            print("Could not Peek: Queue is empty!")
        return self.base_list[self.front_ptr]

    def resize(self):
        # Create a new list with double the size of the current list
        new_base_list = [None] * (self.length * 2)

        # Copy elements from the old list to the new list in order
        current_index = self.front_ptr
        for i in range(self.length):
            new_base_list[i] = self.base_list[current_index]
            current_index = (current_index + 1) % self.length

        # Update pointers to reflect the new list
        self.front_ptr = 0
        self.rear_ptr = self.length - 1

        # Replace the old list with the new list
        self.base_list = new_base_list

        # Update the length of the queue
        self.length *= 2

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue contents:", end=" ")
            i = self.front_ptr
            while True:
                print(self.base_list[i], end=" ")
                if i == self.rear_ptr:
                    break
                i = (i + 1) % self.length
            print()

if __name__ == "__main__":
    queue = CircularQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.display()
    print("Dequeued:", queue.dequeue())
    queue.display()
    queue.enqueue(60)
    queue.display()
