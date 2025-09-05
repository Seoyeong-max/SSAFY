T=int(input())
for tc in range(1,T+1):
    N,M=list(map(int,input().split()))
    arr=[list(map(int,input().split())) for _ in range(N)]
    max_arr=-999999

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_arr=0
            for k in range(M):
                for l in range(M):
                    sum_arr+=arr[i+k][j+l]
            if max_arr<sum_arr:
                max_arr=sum_arr

    print(f"#{tc} {max_arr}")
