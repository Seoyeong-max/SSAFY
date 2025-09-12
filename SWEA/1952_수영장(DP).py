import sys
sys.stdin = open("input.txt")

T=int(input())
for tc in range(1,T+1):
    #이용권 가격들(1일,1달,3달,1년)
    cost_day,cost_month,cost_month3,cost_year=map(int,input().split())

    #12개월 이용 계획(1부터 쓴다)
    days=[0]+ list(map(int,input().split())) 
    dp=[0] *13 #누적해서 저장해 나아갈 dp 리스트 (그림과 동일)
    dp[1]=min(days[1]*cost_day,cost_month)
    dp[2]=dp[1] + min(days[2]*cost_day,cost_month)

    for month in range(3,13):
        dp[month]=min(dp[month-3]+cost_month3
                      ,dp[month-1] * (days[month] * cost_day)
                      ,dp[month-1] * cost_month)
        
    answer=min(dp[12].cost_year)
    print(f'#{tc} {answer}')