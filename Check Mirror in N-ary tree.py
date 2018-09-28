class Node:
    def __init__(self, key):
        self.key=key
        self.li=[]
def insert(root,parent,child):
    return root
for _ in range(int(input())) :
    nodes,edges=map(int,input().split())
    s1=list(map(int,input().split()))
    s2=list(map(int,input().split()))
    mylist1=Node(s1[0])
    mylist2=Node(s2[0])
    for i in range(0,len(s1),2):
        mylist1=insert(mylist1,s1[i],s1[i+1])
    for i in range(0,len(s2),2):
        mylist2=insert(mylist2,s2[i],s2[i+1])

        #not completed
    