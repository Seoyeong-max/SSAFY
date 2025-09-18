di=[0,1,0,-1]
dj=[1,0,-1,0]

number=1
def dfs(row,col):
    visited[r][c]=1
    global number

    for dir in range(4):
        nr=row+di[dir]
        nc=col+dj[dir]

        if 0<=nr<N and 0<=nc<N:
            if house[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc]=1
                house[nr][nc]=number
                dfs(nr,nc)

N=int(input())
house=[list(map(int,input())) for _ in range(N)]
visited=[[0]*N for _ in range(N)]
answer=0


for r in range(N):
    for c in range(N):
        if house[r][c] == 1 and visited[r][c]==0: 
            dfs(r,c) #집에 1이 있고 방문안했으면 재귀함수 실행 
            house[r][c] = number
            answer+=1
            number+=1
            print(visited.count(1))

print(answer)