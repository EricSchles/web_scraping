from tree import Tree
from linkedlists import Node
from time import time
import random
head = Node()
cur = head
tree = Tree()
for i in xrange(100):
    node = Node(i)
    cur.next = node
    cur = cur.next
    tree.append(random.randint(0,10000))

cur = head
start = time()
print "start linked list"
while cur:
    print cur
    cur = cur.next
linked_list_time = "linked list total time", time() - start

print "tree start"
start = time()
tree.pretty_print()
print linked_list_time
print "tree end", time() - start
