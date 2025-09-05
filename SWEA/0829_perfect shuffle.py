T = int(input())
for tc in range(1, T+1):
    N=int(input())
    arr=input().split()
    

    #투포인터이용
    l=0
    if N%2==0:
        r=l+(N/2)
    else:
        r=l+(N/2)+1

        #for문이 하는일:
        #지금이 몇번째반복인지? 만을 알려주는 역할
        #이번이 짝수턴이라면 l을 가져오고,홀수턴이라면 r을 가져와
        for i in range(N):
            if i % 2==0:
                print(arr[l], end='')
                l+=1
            else:
                print(arr[r], end='')
                r+=1