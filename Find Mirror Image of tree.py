class Node:
    def __init__(self, key):
        self.key=key
        self.left=None
        self.right=None

def insert(root,key):
    if root is None:
        root=Node(key)
        return root
    if root.key>key:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)
    return root

def mirror_image(root):
    if root:
        temp=root.left
        root.left=root.right
        root.right=temp
        mirror_image(root.left)
        mirror_image(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)

n=int(input('Enter No. Of Elements \n'))
s=list(map(int,input('Enter elements (space separated) \n').split()))
root=None
for i in s:
    root=insert(root,i)
mirror_image(root)
inorder(root)