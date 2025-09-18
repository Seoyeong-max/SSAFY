import sys
sys.setrecursionlimit(10**6) # 재귀 깊이를 넉넉하게 1,000,000으로 설정

di=[0,1,0,-1]
dj=[1,0,-1,0]
def dfs(row,col):
    visited[row][col]=1      #방문표시한다 

    for  dir in range(4): 
        nr=row+di[dir]
        nc=col+dj[dir]

        if 0<=nr<N and 0<=nc<M:   #움직인 좌표가 
            if graph[nr][nc]==1 and visited[nr][nc]==0:   #배추가 있고 방문한 적이 없다면 다시 재귀 실행 
                dfs(nr,nc)

T=int(input())
for _ in range(1,T+1):
    answer=0   #배추흰지렁이 갯수 
    M,N,K=map(int,input().split())
    graph=[[0]*M for _ in range(N)]  #배추 심은 배추밭 
    visited=[[0]*M for _ in range(N)]  #방문 했는지 안했는지 확인 

    for _ in range(K):    
        a,b=map(int,input().split())
        graph[b][a]=1 #배추가 있으면 1로 바꿔준다 

    for r in range(N):
        for c in range(M):
                #좌표r,c에 배추가 있고(graph[r][c]==1) 방문한 적이 없다면 (visited[r][c]==0):
            if graph[r][c]==1 and  visited[r][c]==  0:
                    dfs(r,c)  #재귀 실행 
                    answer+=1

    print(answer)