V,E=map(int,input().split())

#1.간선들을 가중치 기준으로 정렬
edges=[]
for _ in range(E):
    start, end, weight=map(int,input().split())
    edges.append((start,end,weight))

#가중치 기준 오름차순 정렬 
edges.sort(key=lambda x: x[2])

#2. 가중치가 작은 간선부터 순서대로 선택하자 
#사이클이 발생하면 고르지 말자! 
#언제까지? 
#MST가 완성될 때까지
#==V-1개를 선택할 때 까지
cnt=0 #현재까지 선택한 간선의 수 
result=0 #가중치의 합 

for u,v, w in edges:
    #사이클이 아니라면 
    #- 연결(같은 집합으로 만든다)
    pass