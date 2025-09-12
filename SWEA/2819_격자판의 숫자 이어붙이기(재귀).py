#상하좌우를 봐야하니까 델타
#visited 안쓴다 
#서로 다른 수가 있음  -> set사용 
#6번 이동  
    #종료조건: 6번
    #가지의수: 4개(상하좌우)
    #-> 재귀호출 안쓴다면 BFS이용 

import sys
sys.stdin = open("input.txt")

dy=[-1,1,0,0]
dx=[0,0,-1,1]


#1.종료 조건: 숫자 7자리 일때 종료
#2:가지의 수: 4개(상하좌우)
def recur(y,x,number):
    if len(number) == 7:
        result.add(number)
        return


    for i in range(4):  #상하좌우
        ny=y+dy[i]
        nx=x+dx[i]

        #범위 밖이면 continue
        if ny<0 or ny>=4 or nx<0 or nx>=4:
            continue

        #다음 위치로 이동 
        recur(ny,nx,number+ matrix[ny][nx])



T=int(input())
for tc in range(1,T+1):
    matrix=[ input().split() for _ in range(4)] #숫자 공백이지만 하나하나를 문자로 생각함 
    result= set()

    # 7자리 만드는 코드 
    #-4*4가 모두 출발점이 될 수 있다
    for sy in range(4):
        for sx in range(4):
            recur(sy,sx,matrix[sy][sx])


    print(f'#{tc} {len(result)}')


