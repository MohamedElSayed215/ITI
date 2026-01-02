class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class Queue:
    """
    We consider that the queue is a group of nodes and link together using single linked-list 
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, d):
        nd = Node(d)
        if self.head is None:
            self.head = nd
            self.tail = nd
        else:
            self.tail.next = nd
            self.tail = nd

    def delete(self):
        if self.head is None:
            print('Queue is Empty.')
            return None

        nd = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return nd

    def display(self):
        tmp = self.head
        while tmp is not None:
            print(f'\t{tmp.data}')
            tmp = tmp.next
q=Queue()
q.insert(10)
q.insert(20)
q.display()
