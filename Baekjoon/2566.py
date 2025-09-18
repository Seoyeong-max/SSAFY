arr=[list(map(int,input().split())) for _ in range(9)]
min_number=-999999999
min_i,min_j=0,0
for i in range(9):
    for j in range(9):
        if arr[i][j]>min_number:
            min_number=arr[i][j]
            min_i,min_j=i+1,j+1
print(min_number)
print(min_i,min_j)