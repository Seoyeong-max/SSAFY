#가로길이:M,세로길이:N #K:배추가 심어져 있는 위치의 개수 
dr=[0,0,1,-1]
dc=[1,-1,0,0]

def dfs(row,col):
    visited[row][col]=1

    for dir in range(4):
        nr= row+dr[dir]
        nc= col+dc[dir]

        if 0<=nr< N and 0<=nc<M:
            if graph[nr][nc]==1 and visited[nr][nc]==0:
                dfs(nr,nc)



T=int(input())
for _ in range(T):
    M,N,K=map(int,input().split())
    graph=[[0]*M for _ in range(N)]
    visited=[[0]*M for _ in range(N)]

    for _ in range(K):
        a,b = map(int, input().split())
        graph[b][a]=1

    for r in range(N):
        for c in range(M):
            if graph[r][c]==1 and visited[r][c]==0:
                dfs(r,c)
                answer+=1
    print(answer)