#N:채팅방의 기록수 
N=int(input())
list=[]
list_2=[]
cnt=0

for _ in range(N):
    ID=input()
    if ID != "ENTER":
        list.append(ID)
    else:
        list_2=set(list)
        list=[]


for i in range(len(list_2)):
    cnt+=1

print(cnt)