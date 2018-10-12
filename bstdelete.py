class Node:
    def __init__(self, key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None


def insert(root,key,parent):
    if root is None:
        root=Node(key)
        root.parent=parent
        return root
    if root.key<key:
        root.right=insert(root.right,key,root)
    else:
        root.left=insert(root.left,key,root)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)
    
def mydelete(root,key):
    if root:
        if root.key==key:
            if root.left is None or root.right is None:
                if root.left is None:
                    root.right.parent=root
                    return root.right
                else:
                    root.left.parent=root
                    return root.left
            else:
                return 0
        else:
            if key<root.key:
                root.left=mydelete(root.left,key)
            else:
                root.right=mydelete(root.right,key)
    return root

def successor(root,key):
    if root is None:
        return None
    if root.key!=key:
        if root.key>key:
            return successor(root.left,key)
        else:
            return successor(root.right,key)
    return root



n=int(input())
s=list(map(int,input().split()))
tree=None
for i in s:
    tree=insert(tree,i,None)
inorder(tree)
