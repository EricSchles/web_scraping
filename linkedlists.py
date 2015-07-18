class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return repr(self.data)
if __name__ == '__main__':
    head = Node()
    cur = head
    for i in xrange(1000):
        node = Node(i)
        cur.next = node
        cur = cur.next

    cur = head
    while cur:
        print cur
        cur = cur.next



