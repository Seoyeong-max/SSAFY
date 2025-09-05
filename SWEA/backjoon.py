#2차원 리스트에 1부터 16까지 넣기
# T=[list(map(int,input().split())) for _ in range(4)]
# for i in range(T):
#     for j in range(T):
#         print(T[i][j])

#while로 1부터 100까지 적기
T=int(input())
while T<101:
    if T %2 == 0:
        print(T)
    T+=1