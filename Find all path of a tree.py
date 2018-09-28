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
# function to count paths or to count left nodes.
def find_all_path(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return find_all_path(root.left)+find_all_path(root.right)

n=int(input('Enter No. Of Elements \n'))
s=list(map(int,input('Enter elements (space separated) \n').split()))
root=None
for i in s:
    root=insert(root,i)
print(find_all_path(root))