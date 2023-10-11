class Node():
    def __init__(self,data):
        self.data = data
        self.next =  None
    


class Stack():
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.size is None
    
    def __len__(self):
        return self.size
         
    def peek(self):
        if not self.isEmpty:
            return self.top.data
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1


    def pop(self):
        if not self.isEmpty:
            node = self.top
            self.top = self.top.next
            self.size -= 1
            return node.data

    def show(self):
        if not self.isEmpty():
            pointer = self.top
            while (pointer is not None):
                print(pointer.data, sep = "," ,end = " ")
                pointer = pointer.next
       




a = Stack()
a.push(6)
a.push(8)
a.show()
print(a.peek())