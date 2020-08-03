
class Node():

    def __init__(self, data, nextNodeAdd):
        self.data = data
        self.nextNodeAdd = nextNodeAdd

class LinkedList():

    def __init__(self):
        self.root = None
        self.size = 0

    def Print(self):
        value = self.root
        while value:
            print(value.data)
            value = value.nextNodeAdd

    def Add(self, num):
        node = Node(num, self.root)
        self.root = node
        self.size += 1

    def Find(self, num):
        ptr = self.root
        while ptr:
            if num == ptr.data:
                return True
            else:
                ptr = ptr.nextNodeAdd
        return False

    def Remove(self, num):
        ptr = self.root
        while ptr:
            if num == ptr.data:
                Prevptr.nextNodeAdd = ptr.nextNodeAdd
                break
            else:
                Prevptr = ptr
                ptr = ptr.nextNodeAdd
        return False


p = LinkedList()
p.Add(3)
p.Add(6)
p.Add(7)
p.Add(2)
p.Print()
print(p.Remove(8))
print(p.Find(6))



