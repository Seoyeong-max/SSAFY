T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr_N=list(map(int,input().split()))
    arr_M=list(map(int,input().split()))

    #뭐가짧고긴줄 모르니까 걍 N이 긴걸로 맞춰준다
    if N<M:
        arr_N,arr_M=arr_M,arr_N
        N,M=M,N

    max_v = 0
    #짧은 리스트를 긴 리스트 위에서 한칸씩 움직임
    #range(N-M+1)은 루프가 한번씩 돌아갈 때마다 짧은 배열이 자리잡는 특정지점
    for i in range(N-M+1):
        sum_v=0
        #짧은 리스트의 길이만큼 반복한다 "반복" 여기서 곱하는거는 생각하지말자
        for j in range(M):
            sum_v+=arr_N[i+j]*arr_M[j]
        if max_v<sum_v:
            max_v = sum_v
    print(f'#{tc} {max_v}')