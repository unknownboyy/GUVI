class Node:
    def __init__(self, key):
        self.key=key
        self.left=None
        self.right=None

def insert(root,index,n):
    if index<=n:
        if root is None:
            root=Node(s[index-1])
        if 2*index<=n:
            root.left=insert(root.left,2*index,n)
        if 2*index+1<=n:
            root.right=insert(root.right,2*index+1,n)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)


n=int(input())
s=list(map(int,input().split()))
c=[False]*(n+1)
root=None
root=insert(root,1,n)
inorder(root)