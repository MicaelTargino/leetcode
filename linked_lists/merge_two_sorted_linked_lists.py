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

def merge_linked_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    final_ll = LinkedList()

    curr_1 = ll1.head
    curr_2 = ll2.head

    # Merge the two lists by comparing node values
    while curr_1 and curr_2:
        if curr_1.value < curr_2.value:
            final_ll.append(curr_1.value)
            curr_1 = curr_1.next
        else:
            final_ll.append(curr_2.value)
            curr_2 = curr_2.next

    # Append the remaining nodes from the first list, if any
    while curr_1:
        final_ll.append(curr_1.value)
        curr_1 = curr_1.next

    # Append the remaining nodes from the second list, if any
    while curr_2:
        final_ll.append(curr_2.value)
        curr_2 = curr_2.next

    return final_ll
    

if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()
    
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll1.append(7)

    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    ll2.append(8)

    ll: LinkedList = merge_linked_lists(ll1, ll2)

    ll1.print_list()
    ll2.print_list()
    ll.print_list()
    