#사다리의 규칙상 우선순위가 있다
#1순위: 좌/우로 갈수있는가?->좌우에 길이 있다면 반드시 그 수평길을 따라간다
#2순위: 좌/우에 길이없다면?-> 위로올라간다
for tc in range(1,11):
    T=int(input())

    ladder=[list(map(int,input().split())) for _ in range(100)]

    #idx라는 이름의 빈 리스트를 만든다
    #여기에는 도착점의 좌표(행,열)를 저장한다. 
    idx=[]

    #이중 for문으로 배열의 모든 칸을 (0,0)부터 (99,99)까지 전부 확인한다.
    for i in range(100):
        for j in range(100):
            #만약 현재 칸의 값이 2와 같다면 (도착점)을 찾았다면
            if ladder[i][j]==2:
                #idx리스트에 현재 행,열 번호 i와 j를 추가한다.
                idx.append(i)
                idx.append(j)

    r = idx[0] #위에서 찾은 도착점의 행과 열을 각각 r,c 변수에 저장한다
    c = idx[1]
    #맨 윗줄(0번 행)에 도착할 때까지 계속 반복한다
    while 0<r:
        #현재위치의 오른쪽에 길이있는지 확인한다(들어갈지 말지 결정하는 역할)
        if c<99 and ladder[r][c+1] ==1:
            #오른쪽에 길이 있다면, 그 길이 끝날 때까지 계속 오른쪽으로 이동한다 (고속도로 진입하면 달려)
            while c<99 and ladder[r][c+1]==1:
                c+=1
            r-=1
        #왼쪽에 길이 있는지 확인한다.
        elif c>0 and ladder[r][c-1] ==1:
            while c>0 and ladder[r][c-1] ==1:
                c-=1
            r-=1
        #만약 좌우 모두 길이 없다면
        else:
            r-=1
    print(f'#{tc} {c}')

        

                
                
                