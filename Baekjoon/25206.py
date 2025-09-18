#A+: 등급, 4.5: 과목평점(subject_GPA), 3.0: 학점 (GPA)
# -> 전공평점=과목별로 (학점x과목평점)/학점의 총합 

temp=[]
temp_2=[]
arr={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
for i in range(20):
    subject, GPA, grade= input().split()
    GPA=float(GPA)
    
    if grade =="P":
        continue
    else:
        subject_GPA=arr[grade]





    temp.append(GPA*subject_GPA)  #학점*과목평점
    temp_2.append(GPA)

answer=sum(temp)/sum(temp_2)
round_number=round(answer,6)
print(round_number)




