arr=[list(input()) for _ in range(5)]
temp=[]

max_len = 0
for i in range(len(arr)):
    # if len(arr[i]) >max_len:
    #     max_len=len(arr[i])
    max_len = max(max_len, len(arr[i]))

# 열 고정
for c in range(max_len):
    for r in range(5):
        if c < len(arr[r]):
            temp.append(arr[r][c])
print(''.join(temp))

# arr = [[i for i in range(3)] for _ in range(3)]

# # 밖에 값이 먼저 고정된 후 안의 값을 돌아주기
# # 행을 결정해놓고, 열을 돌아주기 > 행우선순회
# # 열을 결정해놓고, 행을 돌아주기 > 열우선순회
# for i in range(3):
#     for j in range(3):
#         print(arr[j][i])