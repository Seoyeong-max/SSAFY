# # while 조건식:
# #     조건식이 참(TRUE)일 동안 반복해서 실행할 코드 


di=[0,1,0,-1]
dj=[1,0,-1,0]


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    cnt=0

    #0:빈칸, 1:벽, 2:괴물 
    # 1. 괴물 위치를 고르자
    r, c = -1, -1
    for i in range(N):
        for j in range(N):
            #괴물찾기
            if arr[i][j]==2:
                r, c = i, j

    #괴물에서 방향(k),얼만큼(c) 이동할 지 결정 
    for dir in range(4):
        
        # 범위 안쪽이고 1이 아니면
        # 범위 안 쪽? > 우주 괴물의 위치(r,c)로부터 레이저를 쏜 위치(nr, nc)가 맵 안쪽이라면
        # 1이 아니면? > 우주 괴물이 레이저를 쏜 위치(nr, nc)에 적혀있는 숫자(arr[nr][nc])가 1이 아니라면
        step = 1
        while 0 <= r + di[dir]*step < N and 0 <= c + dj[dir]*step < N and arr[r + di[dir]*step][c + dj[dir]*step] != 1:
            arr[r + di[dir]*step][c + dj[dir]*step] = 1

            step += 1

        # for o in range(1,N):
        #     ni=r+di[k]*o
        #     nj=c+dj[k]*o
        #     #ni,nj 범위 확인하기 
        #     if 0 > ni or ni >= N or 0 > nj or nj >= N or arr[ni][nj] == 1:
        #         break
            
        #     arr[ni][nj]=3
                #arr[ni][nj] == 0일동안 반복해서 0을 3으로 바꾼다.
                # while arr[ni][nj]==0:
                #     arr[ni][nj]=3
                #     #arr[ni][nj]은 1만나면 멈춤 
                #     if arr[ni][nj]!=1:
                #         break

    for i in range(N):
        for j in range(N):
            if arr[i][j]==0:
                cnt+=1
    print(f'#{tc} {cnt}')


numbers = [1,2,3,4,5]
# # for i in numbers:
# #     if i == 3:
# #         print(i)

# for > '반복대상'을 순회해라
# while > 조건을 만족한다면 반복해라
#       > numbers의 끝 요소까지...
#       > 끝 요소는 어떻게 알지?
#       > 끝 요소는 index가 len(numbers)-1 이야...
#       > index는 i로 운용할거야...

i = 0
while i < len(numbers):
    print(numbers[i])
    i=i+1

# numbers = [12,3]

# print(numbers[100])