word=input().upper() #대문자로 입력받기 #[MISSISSIPI]
word_list=list(set(word)) #word에 중복을 제거하기  #[M,I,P,S]
cnt=[] #각 word_list들이 몇개있는지 넣어줄 새로운 리스트

for i in word_list:   
    X=word.count(i)  #word에서 각 단어들이 몇개 있는지 세어줌 
    cnt.append(X)   #세어준 횟수를 cnt에 추가해준다 

#그러면 cnt=[1,4,4,1]

#만약에 많이 사용된 알파벳이 여러개라면 
if cnt.count(max(cnt))>1:
    print("?")
    
#한개라면 
else:
    print(word_list[cnt.index(max(cnt))])