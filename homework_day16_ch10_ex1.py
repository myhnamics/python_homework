import random


class Node():
    def __init__(self):
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end = ' ')
    print()

def go_store(con):
    global memory, head, current, pre
    node = Node()
    node.data = con
    memory.append(node)
    if head == None:
        head = node
        return

    print(head.data[2])
    d1 =  ((head.data[1]) * (head.data[1]) + (head.data[2]) * (head.data[2]))
    if d1 > (con[1]*con[1]+con[2]*con[2]):
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        s1 = ((current.data[1])*(current.data[1])+(current.data[2])*(current.data[2]))
        if s1 > (con[1]*con[1]+con[2]*con[2]):
            pre.link = node
            node.link = current
            return
    current.link = node
    node.link = head




memory = []
head, current, pre = None, None, None
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
stores = [(i, random.randint(1,100), random.randint(1,100)) for i in alphabet]
print(stores)
print(stores[1][1])
if __name__ == "__main__":
    node = Node()
    for store in stores[1:]:
        go_store(store)

    print_nodes(head)

