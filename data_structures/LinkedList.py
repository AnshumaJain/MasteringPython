# Implement a Linked List in python with add(), find(), remove() functionalities

class Node:
    def __init__(self, data, next_node_add):
        self.data = data
        self.next_node_add = next_node_add


class LinkedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def print(self):
        value = self.root
        while value:
            print(value.data, " ", end="")  # suppress newline using 'end'
            value = value.next_node_add
        print("")

    def add(self, num):
        node = Node(num, self.root)
        self.root = node
        self.size += 1

    def find(self, num):
        ptr = self.root
        while ptr:
            if num == ptr.data:
                return True
            else:
                ptr = ptr.next_node_add
        return False

    def remove(self, num):
        ptr = self.root
        prev_ptr = None
        while ptr:
            if num == ptr.data:
                prev_ptr.next_node_add = ptr.next_node_add
                break
            else:
                prev_ptr = ptr
                ptr = ptr.next_node_add
        return False


p = LinkedList()
p.add(3)
p.add(6)
p.add(7)
p.add(2)
p.print()
print(p.remove(8))
print(p.find(6))
print(p.remove(7))
p.print()
