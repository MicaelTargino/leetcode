class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def size(self):
        acc = 0
        curr = self.head
        while curr is not None:
            acc = acc + 1
            curr = curr.next
        return acc

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        # Initialize three pointers: curr, prev and next
        curr = self.head
        prev = None
        # Traverse all the nodes of Linked List
        while curr is not None:
            # Store next
            next_node = curr.next
            # Reverse current node's next pointer
            curr.next = prev
            # Move pointers one position ahead
            prev = curr
            curr = next_node

        # update the head of reversed linked list
        self.head = prev

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    print("Original linked list:")
    ll.print_list()

    ll.reverse()

    print("Reversed linked list:")
    ll.print_list()
