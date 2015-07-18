class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return repr(self.data)

class Tree:
    def __init__(self,data=None):
        if data:
            self.head = Node(data)
        else:
            self.head = None
    
    def append(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.left != None or cur.right != None:
                if cur.left < data:
                    cur = cur.left
                else:
                    cur = cur.right
            if not cur.left:
                cur.left = Node(data)
            else:
                cur.right = Node(data)
                
    def pretty_print(self):
        if self.head:
            self._pretty_print(self.head)
        else:
            print None
    def _pretty_print(self,node):
        if node.left:
            self._pretty_print(node.left)
        print node
        if node.right:
            self._pretty_print(node.right)

if __name__ == '__main__':
    tree = Tree()
    tree.append(5)
    tree.append(7)
    tree.append(-2)
    tree.append(-12)
    tree.append(22)
    tree.append(21)
    tree.pretty_print()
