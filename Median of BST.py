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

    def inorder(root):
        global li
        if root:
            inorder(root.left)
            li.append(root.key)
            inorder(root.right)
    li=[]
    for _ in range(int(input())):
        n=int(input())
        li=[]
        s=list(map(int,input().split()))
        mytree=Tree()
        for i in s:
            mytree.root=mytree.insert(mytree.root,i)
        inorder(mytree.root)
        if len(li)%2==1:
            print(li[len(li)//2])
        else:
            print((li[len(li)//2]+li[len(li)])/2)