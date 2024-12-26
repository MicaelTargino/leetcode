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

def remove_nth_node_from_the_end(ll: LinkedList, n:int) -> None: 
    if n > ll.size():
        raise Exception("N is bigger than list")
    
    if n == ll.size():
        ll.head = ll.head.next
        return 
    
    s = ll.head 
    f = ll.head 
    prev_s = ll.head
    post_s = None

    for i in range(ll.size() - n):
        prev_s = s
        post_s = s.next.next
        s = s.next 
        f = f.next
    
    prev_s.next = post_s 

if __name__ == "__main__":
    ll = LinkedList()
    
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)

    n = int(input("Remove the N-th Node from the end: "))

    remove_nth_node_from_the_end(ll, n)

    ll.print_list()
