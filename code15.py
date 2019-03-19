for _ in range(int(input())):
    m, n = map(int,input().split())
    points = [[0 for i in range(n)] for i in range(m)]
    top = [[0 for i in range(n)] for i in range(m)]
    bottom = [[0 for i in range(n)] for i in range(m)]
    left = [[0 for i in range(n)] for i in range(m)]
    right = [[0 for i in range(n)] for i in range(m)]
    front = [[0 for i in range(n)] for i in range(m)]
    back = [[0 for i in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                top[i][j]=1
                front[i][j]=2
                left[i][j]=3
                right[i][j]=4
                bottom[i][j]=6
                back[i][j]=5
                points[i][j]=1
            elif i==0:
                top[i][j]=left[i][j-1]
                bottom[i][j]=right[i][j-1]
                left[i][j]=bottom[i][j-1]
                right[i][j]=top[i][j-1]
                front[i][j]=front[i][j-1]
                back[i][j]=back[i][j-1]
                points[i][j]+=points[i][j-1]+top[i][j]
            elif j==0:
                top[i][j]=back[i-1][j]
                bottom[i][j]=front[i-1][j]
                left[i][j]=left[i-1][j]
                right[i][j]=right[i-1][j]
                front[i][j]=top[i-1][j]
                back[i][j]=bottom[i-1][j]
                points[i][j]+=points[i-1][j]+top[i][j]
            else:
                if left[i][j-1]>back[i-1][j]:
                    top[i][j]=left[i][j-1]
                    bottom[i][j]=right[i][j-1]
                    left[i][j]=bottom[i][j-1]
                    right[i][j]=top[i][j-1]
                    front[i][j]=front[i][j-1]
                    back[i][j]=back[i][j-1]
                    points[i][j]+=points[i][j-1]+top[i][j]
                else:
                    top[i][j]=back[i-1][j]
                    bottom[i][j]=front[i-1][j]
                    left[i][j]=left[i-1][j]
                    right[i][j]=right[i-1][j]
                    front[i][j]=top[i-1][j]
                    back[i][j]=bottom[i-1][j]
                    points[i][j]+=points[i-1][j]+top[i][j]
    print(points[m-1][n-1])