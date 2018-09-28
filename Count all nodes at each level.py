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

def count_at_level_x(root,level):
    if root:
        if level==0:
            return 1
        else:
            if level:
                return count_at_level_x(root.left,level-1)+count_at_level_x(root.right,level-1)
            else:
                return 0
    return 0

n=int(input('Enter No. Of Elements \n'))
s=list(map(int,input('Enter elements (space separated) \n').split()))
root=None
for i in s:
    root=insert(root,i,None)
for i in range(getheight(root)+1):
    print('Nodes at Level',i,'=',count_at_level_x(root,i))