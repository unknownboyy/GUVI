def main():
    n=int(input())
    scores=list(map(int,input().split()))
    m=int(input())
    new_scores=list(map(int,input().split()))
    myscoreset=set(scores+new_scores)
    leaderboard=list(myscoreset)
    leaderboard.sort(reverse=True)
    d=dict()
    for i in leaderboard:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    l=len(leaderboard)
    ii=n-1;totalcount=scores;rank=n-1
    print(leaderboard)
    for i in range(m):
        curr_score=new_scores[i]
        while ii>=0 and curr_score>leaderboard[ii]:
            ii-=1
            rank-=d[leaderboard[ii]]
        if ii==0:
            print(1)
        else:
            print(ii)
if __name__ == '__main__':
    main()