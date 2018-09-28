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
    if root.key>key:
        root.left=insert(root.left,key,root)
    else:
        root.right=insert(root.right,key,root)
    return root

def printpath(root):
    if root:
        printpath(root.parent)
        print(root.key,end=' ')

def count_path_with_x(root,k):
    if root is None:
        return
    if root.left is None and root.right is None and k-root.key==0:
        printpath(root)
    elif k>0:
        count_path_with_x(root.left,k-root.key)
        count_path_with_x(root.right,k-root.key)
    else:   return


n=int(input('Enter No. Of Elements \n'))
s=list(map(int,input('Enter elements (space separated) \n').split()))
root=None
for i in s:
    root=insert(root,i,None)
print('Now enter the values of X')
k=int(input())
count_path_with_x(root,k)