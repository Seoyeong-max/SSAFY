from collections import deque

dr=[-1,1,0,0]
dc=[0,0,-1,-1]

def crash(count,remain,graph):
    global answer 

    if not remain or count== N:
        answer== min(answer,remain)
        return
    
    #1.해당 count 번째에 구슬을 떨어트릴 행 고르기 
    for i in range(W):
        next_remain = remain

        #해당 행이 비어있다면 스킵 
        if not graph [i]:
            continue

        r = i
        c = len(graph[i])-1

        #2. 연쇄 폭발 영역 탐색
        q = deque()
        visited = [[0]*H for _ in range(W)]

        remain -=1
        visited[r][c] = 1
        q.append((r,c))

        while q:
            r,c = q.popleft()
            if graph[r][c] <=1:
                continue
            for dir in range(4):
                for step in range(graph[r][c]):
                    nr = r+dr[dir]*step
                    nc = c+dc[dir]*step

                    #맵 밖 벗어났을 때
                    if nr <0 or nr >=W or nc<0 or nc >=H:
                        continue
                    if visited[nr][nc]:
                        continue

                    #방문했을 때
                    if visited[nr][nc]:
                        continue

                    #해당 행의 사이즈를 벗어났을 때
                    if len(graph[nr])-1 < nc:
                        continue

                    next_remain-=1
                    visited[nr][nc] =1
                    q.append((nr,nc))

        #3. 폭파 & 떨어트리기
        copy_graph=[]
        for r in range(W):
            row=[]
            for c in range(len(graph[r])):
                if visited[r][c]:
                    continue
                row.append(graph[r][c])
            copy_graph.append(row)
        crash(count+1,next_remain,copy_graph)


T=int(input())

for tc in range(1,T+1):
    N,W,H= map(int,input().split())

    input_graph = [(list(map(int,input().split()))) for _ in range(H)]
    graph=[]
    answer=0

    for i in range(W):
        row=[]
        for j in range(H):
            if input_graph[H-1-j][i]==0:
                answer+=j
                break
            row.append(input_graph[H-1-j][i])
        else:
            answer+=H
        graph.append(row)

    #몇 번째 구슬을 놓는 중인지
    #남은 블럭수
    #변화된 그래프 
    crash(0, answer, graph)
    