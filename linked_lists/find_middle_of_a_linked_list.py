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

def find_middle(ll: LinkedList) -> int:

    if not ll.head:
        return  None
    if not ll.head.next:
        return ll.head.value

    s = ll.head # slow ptr
    f = ll.head.next # fast ptr 

    while f and f.next:
        s = s.next
        f = f.next.next

    return s.value

if __name__ == "__main__":
    ll1 = LinkedList()
    
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll1.append(7)

    middle = find_middle(ll1)

    print("Meio da lista:", middle)
    