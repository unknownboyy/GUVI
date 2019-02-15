class Node:
    def __init__(self, key):
        self.data=key
        self.left=None
        self.right=None
def insert(root,key):
    if root is None:
        root=Node(key)
        return root
    if root.data>key:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)
    return root

def diameter(root):
    if root is None:
        return 1
    return max(3+get_height(root.left)+get_height(root.right),diameter(root.left),diameter(root.right))


def get_height(root):
    if root is None:
        return -1
    return 1+max(get_height(root.left),get_height(root.right))
def getbf(root):
    if root is None:
        return 0
    left_height=get_height(root.left)
    right_height=get_height(root.right)
    return abs(left_height-right_height)

def isBalanced(root):
    if root is None:
        return True
    if getbf(root)<=1:
        return isBalanced(root.left) and isBalanced(root.right)
    else:
        return False

def countLeaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return countLeaves(root.left)+countLeaves(root.right)

def postorderTraversal(root):
    if root:
        print(root.data,end=' ')
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        
def traverse_level_order( root ):
    if root:
        q=[]
        q.append(root)
        while len(q)>0:
            app=q.pop(0)
            print(app,end=' ')
            if app.left:
                q.append(app.left)
            if app.right:
                q.append(app.right)
my_tree=None
n=int(input())
s=list(map(int,input().split()))
for i in s:
    my_tree=insert(my_tree,i)
print(diameter(my_tree))