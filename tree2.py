class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def insert(self, root, key):
        if root is None:
            root=Node(key)
            return root
        if root.key>key:
            root.left=self.insert(root.left,key)
        else:
            root.right=self.insert(root.right,key)
        return root
def getheight(root):
    if root is None:
        return -1
    return max(getheight(root.left),getheight(root.right))+1

def inorder(root):
    global li
    if root:
        inorder(root.left)
        li.append(root.key)
        inorder(root.right)
li=[]
for _ in range(int(input())):
    try:
        n=int(input())
        li=[]
        s=list(map(int,input().split()))
        mytree=Tree()
        for i in s:
            mytree.root=mytree.insert(mytree.root,i)
        inorder(mytree.root)
        flag=True
        if len(li)!=len(set(s)):
            flag=False
        for i in range(n):
            if s[i]!=li[i]:
                flag=False;break
        print(1) if flag else print(0)
    except:
        pass