class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,data):
    if not root:
        temp=Node(data)
        return temp
    if root.data>data:
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)


n=int(input())
root=Node(int(input()))
for _ in range(1,n):
    i=int(input())
    root=insert(root,i)
inorder(root)