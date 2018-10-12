class Node:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None
def insert(root,key,parent):
    if root is None:
        root=Node(key)
        root.parent=parent
        return root
    if root.data>key:
        root.left=insert(root.left,key,root)
    else:
        root.right=insert(root.right,key,root)
    return root
def search(root,key):
    while (root!= None and root.data!=key):
        if key < root.data:
            root=root.left
        else:
            root=root.right
    if root is None:
        return root
    if(key==root.data):
        k=root.data
        return k
def minimum(root):
    while root.left!=None:
        root=root.left
    print(root.data)
def maximum(root):
    while root.right!=None:
        root=root.right
    print(root.data)
def predicessor(root,key):
    key=find(root,key)
    if key.left != None:
        maximum(key.left)
    else:
        if key.parent is not None:
            print(key.parent.data)
        else:
            print("Failed to find")
def sucecessor(root,key):
    key=find(root,key)
    if key.right != None:
        minimum(key.right)
    else:
        if key.parent is not None:
            print(key.parent.data)
        else:
            print("Failed to find")
def find(root,key):
    if root is None:
        return root
    if root.data==key:
        return root
    if root.data>key:
        return find(root.left,key)
    else:
        return find(root.right,key)
def preorder(root):
    if root:
        preorder(root.left)
        print(root.data,end=' ')
        preorder(root.right)
def insertion(root,key):
    parent=None
    myroot=root
    while root != None:
        if root.data>key:
            parent=root
            root=root.left
        else:
            parent=root
            root=root.right
    if parent is None:
        root=Node(key)
        return root
    else:
        if parent.data>key:
            parent.left=Node(key)
            parent.left.parent=parent
            return myroot
        else:
            parent.right=Node(key)
            parent.right.parent=parent
            return myroot
            """
    root=root.parent
    if root==None:
        root=Node(key)
        root.parent
    else:
        if root.data>key:
            root=root.left
            root.data=key
        else:
            root=root.right
            root.data=key
            """
    
n=int(input("No of element in bst:"))
l=list(map(int,input("Enter the element:").split()))
root=None
for i in l:
    root=insert(root,i,None)
minimum(root)
maximum(root)
print("Enter the key to insert")
key2=int(input())
root=insertion(root,key2)

"""
print("Enter the key for predicessor & Sucessor")
key1=int(input())
predicessor(root,key1)
sucecessor(root,key1)

print("Enter the key to search")
key=int(input())
k=search(root,key)
if (k==key):
    print("Element Found")
else:
    print("Element Not Found")
preorder(root)
"""