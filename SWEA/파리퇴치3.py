#옮겨가면서 중심을 정함
#델타를 이용해서 +,x 에 있는 파리의 개수들을 더해준다 
#중심이 옮겨질때마다 max_sum 과 비교하여 최대값을 갱신한다. 

#T:테스트 케이스 개수
#N:배열의 크기, M:스프레이의 세기 
#max_sum:한 번에 잡을 수 있는 최대 파리수 

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    max_sum=0

    #중심 정하기
    for i in range(N):
        for j in range(N):

            sum_plus_catch=arr[i][j]
            for dr,dc in [[0,1],[1,0],[-1,0],[0,-1]]:
                for c in range(1,M):
                    ni=i+dr*c
                    nj=j+dc*c
                    if 0<=ni<N and 0<=nj<N:
                        sum_plus_catch +=arr[ni][nj]
            if max_sum<sum_plus_catch:
                max_sum=sum_plus_catch

            sum_multiple_catch=arr[i][j]
            for dr2,dc2 in [[-1,1],[1,1],[1,-1],[-1,-1]]:
                for c in range(1,M):
                    nr=i+dr2*c
                    nc=j+dc2*c
                    if 0<=nr<N and 0<=nc<N:
                        sum_multiple_catch +=arr[nr][nc]

            if max_sum<sum_multiple_catch:
                max_sum=sum_multiple_catch

    print(f'#{tc} {max_sum}')



            
