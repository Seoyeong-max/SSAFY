#특정 정점 기준으로 시작 
# 갈수 있는 노드들 중 가중치가 가장 작은 노드부터 간다 
# 작은 노드를 먼저 꺼내기 위해 우선순위큐를 활용한다 

import heapq
from heapq import heappush, heappop


def prim(start_node):
    pq = [(0, start_node)] #(가중치, 노드) 형태  -> 정렬기준이 앞이므로 (가중치, 노드) 형태로 만든다 
    MST=[0]*V #visited 와 동일하다 
    min_weight= 0 #최소비용 

    while pq:
        weight, node= heappop(pq)  #가장 작은 가중치 

        #이미 방문한 노드라면 continue 
        if MST[node]:
            continue

        MST[node]=1 #node로 가는 최소비용이 선택되었다 
        min_weight +=weight #누적합 추가 

        for next_node in range(V):
            if graph[node][next_node]==0:
                continue

            #이미 방문했으면 continue
            if MST[next_node]:
                continue

            #원래 BFS에서는 여기서 방문 처리 -> 최소 비용 X 
            heappush(pq,(graph[node][next_node],next_node))

    return min_weight



V,E= int(input().split())
graph=[[0]*V for _ in range(V)]

for _ in range(E):
    start, end, weight=map(int,input().split())
    graph[start][end]=weight
    graph[end][start]=weight #양방향 
    
result = prim(0) #출발 정점과 함께 시작 
print(f'최소비용 = {result}')
