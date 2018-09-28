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

def getheight(root):
    if root is None:
        return -1
    return max(getheight(root.left),getheight(root.right))+1

def print_zig_zag(root,level,i):
    if root:
        if level==i:
            print(root.key,end=' ')
        elif level>i:
            if level%2==0:
                print_zig_zag(root.right,level,i+1)
                print_zig_zag(root.left,level,i+1)
            else:
                print_zig_zag(root.left,level,i+1)
                print_zig_zag(root.right,level,i+1)

n=int(input('Enter No. Of Elements \n'))
s=list(map(int,input('Enter elements (space separated) \n').split()))
root=None
for i in s:
    root=insert(root,i,None)
for i in range(getheight(root)+1):
    print_zig_zag(root,i,0)
