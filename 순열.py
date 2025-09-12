path = []
visited = [0] * (3+1)

def recur(cnt):
    if cnt == 2: # 순열에서 몇개를 고를 것인지
        print(*path)
        return

    for i in range(3): # 몇개의 카드를 가지고 있는지
        if visited[i]: # 중복 제거
            continue
        visited[i] = 1 # 방문 기록
        path.append(i) 
        recur(cnt + 1)
        path.pop()
        visited[i] = 0 # 방문 기록 초기화
recur(0)