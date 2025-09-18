#재귀를 짤 때: 깊이를 고려 
#DFS,인접리스트로 세팅 

def dfs(node): 
    for next in adj_list[node]:
        if visited[next]:
            continue
        visited[next]=1
        dfs(next)


T=int(input())
for tc in range(1,T+1):
    answer=0

    N,M=map(int,input().split()) #N은 사람수 M은 연결관계의 수 
    connections = list(map(int,input().split())) #연결관계수 
    adj_list=[[] for _ in range(N+1)]
    visited=[0]*(N+1)

    for i in range(M):
        idx1=i*2
        idx2=idx1 + 1
        
        #내가 연결하고 싶은 친구는 a와 b야 
        a=connections[idx1]
        b=connections[idx2]

        adj_list[connections[idx1]].append(connections[idx2])
        adj_list[connections[idx2]].append(connections[idx1])
    
    for node in range(1,N+1):
        if visited[node]:
            continue 
        
        answer+=1
        visited[node] = 1 
        dfs(node)

    print(f'#{tc} {answer}')