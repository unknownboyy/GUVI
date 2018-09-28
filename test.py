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

def getheight(root):
    if root is None:
        return -1
    return max(getheight(root.left),getheight(root.right))+1

def fillList(root,level):
    global li
    if root:
        if level:
            fillList(root.left,level-1)
            fillList(root.right,level-1)
        else:
            li.append(root.key)
li=[]
for target_list in range(int(input())) :
    n=int(input())
    root=None
    s=list(map(int,input().split()))
    
    for i in range(getheight(root)):
        li=[]
        fillList(root,i)
        li.sort()
        print(*li)