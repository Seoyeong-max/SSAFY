N=int(input())
for i in range(1,N+1):
    K=2*i-1
    R=(2*N-K)//2
    arr=" "*R+"*"*K
    print(arr)


for j in range(N-1,0,-1):
    K=2*j-1
    R=(2*N-K)//2
    arr_B=" "*R+"*"*K
    print(arr_B)

    #--------------------------

N=int(input())
for i in range(-N+1,N):
    #i를 -N+1 부터 N-1까지 반복
    #N=3이면 i = -2,-1,0,1,2
    spaces=abs(i) #abs는 절댓값 함수
    stars=2*(N-abs(i))-1
    print(" "*spaces+"*"*stars)

#abs함수(절댓값함수)-> '0'으로부터의 거리를 알려주기 때문에 대칭 구현에 완벽하다.