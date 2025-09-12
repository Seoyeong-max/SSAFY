#T: 테스트 케이스, N:점원 수,B가 정해져있지 않아서 조합으로 생각하면 된다 ,선반의 높이  #대표적인 부분집합 문제, 재귀도 이용함 
import sys
sys.stdin = open("input.txt")

#재귀를 쓸 때 항상 생각할 것
#1.종료 조건: N명의 모든 점원을 고려했을 때 
#   -가지치기: 이미 높이가 B이상이면 더이상 쌓을 필요가 없다 
#2.가지의수:
#   - 점원을 탑에 포함시키는 경우 or 안시키는 경우


def recur(idx,total_height):
    global min_answer
    if total_height >=B:  #가지치기: B이상이면 더이상 쌓지 않는다 
        min_answer=min(min_answer, total_height)
        return

    if idx==N: #N명을 모두 고려함
        return
    
    recur(idx+1, total_height+heights[idx])  # 탑에 포함시키는 경우
    recur(idx+1, total_height)  # 탑에 포함 안 시키는 경우 



T=int(input())


for tc in range(1,T+1):
    N,B=map(int,input().split())
    heights = list(map(int,input().split()))
    min_answer=200000000 #나올 수 있는 최대범위 
    recur(0,0)
    print(f'#{tc} {min_answer-B}')