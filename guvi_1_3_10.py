x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
diff=abs((x1*60+y1)-(x2*60+y2))
print(diff//60,diff%60)