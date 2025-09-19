T=int(input())
arr=[[0]*100 for _ in range(100)]
for _ in range(T):
    x,y=map(int,input().split())

    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j]=1

result=0
for r in arr: 
    result += sum(r)
print(result)

