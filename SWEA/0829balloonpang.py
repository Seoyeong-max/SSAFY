#N*N배열을 하나씩 돌면서 2인값을찾는다
#2에서부터 상하좌우로 범위가 끝나지않을때까지 쭉쭉직진한다.
#필요한 데이터:N,sum,max,delta,c(얼마나갈지)
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr= [list(map(int,input().split())) for _ in range(N)]
    max_arr=-999999
    
    di=[0,1,0,-1]
    dj=[1,0,-1,0]
    r=0
    c=0

    for i in range(N):
        for j in range(N):
            sum_arr=0
            #2가 써진 풍선 찾기
            if arr[i][j]==2:
                r=i
                c=j
                
            for k in range(4):    #방향 결정
                for p in range(1,N):  #얼마나 갈지 결정
                    nr=i+di[k]*p   
                    nc=j+dj[k]*p

                    #범위에서 벗어나면 방향 바꾸고
                    if nr<0 or nc>=N or nc<0 or nr>=N:   
                        continue
                    #안벗어나면 더해줌
                    else:
                        sum_arr+=arr[nr][nc]
            if sum_arr>max_arr:
                max_arr=sum_arr
    print(f"#{tc} {max_arr}")
        
                        
                    


