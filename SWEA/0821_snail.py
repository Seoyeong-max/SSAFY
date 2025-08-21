#필요한데이터
#T=테스트 케이스의 개수
#N=달팽이의 크기 
#arr은 0이 들어간 N*N 달팽이 
#델타값 
#현재 좌표

#구조 
#T입력
#tc 반복 
    #N입력, delta입력, dir(방향)입력
    #arr=[0]*N 반복
    #r=0,c=0
    #1부터 N*N까지 반복 
     #r이랑 c범위 확인
        #범위확인하는법->nr,nc로 확인 
        #범위 맞으면 +1 
        #범위 안맞으면 방향 바꿈 
di=[0,1,0,-1]
dj=[1,0,-1,0]

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[[0]*N for _ in range(N)]
    
    #방향
    dir=0
    r=0
    c=0

    for count in range(1,N*N+1):
        arr[r][c]=count
        #임시로 보내본다 
        nr=r+di[dir]
        nc=c+dj[dir]
        #임시로 보낸 범위가 안맞을때 
        if nr<0 or nr>=N or nc<0 or nc>=N or arr[nr][nc]!=0:
            #방향을 바꾼다 
            dir=(dir+1)%4
            r=r+di[dir]
            c=c+dj[dir]
        #임시로 보낸 범위가 맞음 
        else:
            r=nr
            c=nc       
    print(f'#{tc}')
    for row in arr:
        print(*row)

