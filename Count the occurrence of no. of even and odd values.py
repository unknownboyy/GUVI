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

def count_x_type_nodes(root,x):
    if root:
        if root.key%2==x:
            return 1+count_x_type_nodes(root.left,x)+count_x_type_nodes(root.right,x)
        else:
            return count_x_type_nodes(root.left,x)+count_x_type_nodes(root.right,x)
    return 0

n=int(input('Enter No. Of Elements \n'))
s=list(map(int,input('Enter elements (space separated) \n').split()))
root=None
for i in s:
    root=insert(root,i,None)
print('Even Nodes = ',count_x_type_nodes(root,0))
print('Odd Nodes = ',count_x_type_nodes(root,1))
