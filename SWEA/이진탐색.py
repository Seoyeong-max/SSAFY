def binary_search_while(target):
    left=0   #검색 시작점
    right=len(arr)-1   #검색 끝점
    cnt=0 #몇 번만에 검색했는가? 

    while left<= right:  #교차되면 못찾은 것
        mid=(left+right) //2
        cnt+=1 #검색횟수 추가 

        if arr[mid] ==target:
            return mid,cnt #mid위치에 존재한다고 return
        
        #target 보다 정답이 왼쪽에 있는 경우
        if target < arr[mid]:
            right=mid-1
        #target 보다 정답이 오른쪽에 있는 경우
        else:
            left=mid+1
    return -1, cnt

arr=[4,2,9,7,11,23,19]
#이진 검색은 항상 정렬된 데이터에 적용
arr.sort()  #2 4 7 9 11 19 23

print(f'9={binary_search_while(9)}번째에 위치')