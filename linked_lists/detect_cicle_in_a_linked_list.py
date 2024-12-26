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
        if isinstance(value, Node):
            new_node = value 
        else:
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

    def has_cycle(self):
        existence_dict = {}
        curr = self.head 

        while curr.next is not None:
            if existence_dict.get(curr, False):
                return True 
            existence_dict[curr] = 1

            curr = curr.next

        return False

if __name__ == "__main__":
    ll = LinkedList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    ll.append(n1)
    ll.append(n2)
    ll.append(n3)
    ll.append(n4)
    ll.append(n5)
    ll.append(n1) # add the cycle in the linked list

    # print("Original linked list:")
    # ll.print_list()

    print("Does linked list has cycle:", ll.has_cycle())
