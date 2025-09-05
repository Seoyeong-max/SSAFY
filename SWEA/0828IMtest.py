#1번문은 들어가면 무조건 다음 포탈로 들어간다. 2~N번 문은 들어가면 처음 방문 했을 경우 왼쪽 포탈을 타고 다시 방문 했을때는 오른쪽 포탈을 탄다.
#테스트 케이스를 첫줄에 입력 받고 그 다음 줄에 문의 개수를 입력받는다.

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    sum_arr=0

    for i in range(1,N-1):
        number=(i+1)-arr[i]
        sum_arr+=number
    number_2=2*N-3

    print(sum_arr)
    print(f'#{tc} {sum_arr+number_2}')
