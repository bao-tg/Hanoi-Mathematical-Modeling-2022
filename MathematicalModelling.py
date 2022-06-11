lst1=[[0,1,4,0,1,0,0,12,0,2,0,0,1,0],
[0,2,7,0,6,5,0,0,0,8,0,0,0,0],
[0,0,2,0,3,0,0,6,0,1,0,0,3,0],
[2,0,0,2,0,6,2,10,0,4,0,0,0,0],
[0,0,0,0,5,0,0,5,0,0,0,0,0,0],
[0,3,0,0,0,1,0,0,0,0,0,0,0,1],
[0,0,1,0,4,4,1,2,0,0,0,0,0,0],
[0,0,0,0,0,3,0,9,0,5,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,0,4],
[1,0,0,0,0,0,0,4,0,0,7,0,0,0],
[0,0,0,0,7,0,3,0,0,3,0,0,5,0],
[0,0,0,0,0,0,0,1,0,0,0,0,0,0],
[5,4,3,0,8,2,0,0,0,0,4,0,7,0],
[0,0,0,0,0,0,0,3,0,0,0,0,0,2],
[0,0,0,0,0,0,0,0,0,0,9,0,4,0],
[0,0,0,0,0,0,0,0,0,0,8,0,0,3],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,2,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,5],
[0,0,0,4,0,0,0,0,0,6,0,0,0,0],
[0,0,0,0,0,7,0,0,2,0,0,0,8,0],
[3,0,0,0,10,0,0,0,0,0,3,4,2,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,5,0,8,0,0,5,0,0,0,0,0],
[0,0,0,5,0,8,0,0,5,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,3,0,6,3,0,0],
[0,0,0,0,0,0,0,0,6,0,0,0,0,0],
[0,0,0,0,0,0,4,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,4,0,0,1,0,0],
[0,0,0,0,0,0,0,7,0,0,0,0,0,0],
[0,0,6,0,9,0,0,0,0,0,5,0,6,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,5,0,0,0,0,0,0,0],
[0,5,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,2,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,3,0,0,0,0,1,0,11,0,0,0],
[4,0,0,0,0,0,0,8,0,7,0,0,0,0],
[0,5,0,0,0,0,0,0,0,0,2,0,0,0],
[0,0,0,0,0,9,0,0,0,0,10,0,0,0]]
#lst1 là list chứa thông tin về "Mức độ đóng góp của từng thành viên trong các cuộc hội thoại" đã được mã hóa.

lst2=[1,0,0,2,0,2,2,0,3,0,1,1,0,1]
#lst2 là list chứa thông tin về "Mức độ nghiêm trọng của cuộc hội thoại" đã được mã hóa.

lst3=[3,5,6,8]
#lst3 là index của các cuộc hội thoại "Cực kì nghiêm trọng"
lst4=[0,10,11,13]
#lst4 là index của các cuộc hội thoại "Nghiêm trọng"

import os
os.system('cls')
#Xóa màn hình Terminal

Red=[]
Yellow=[]
#Hai lst chứa sô lượng topic "Cực nghiêm trọng", "Nghiêm trọng" của từng đối tượng
for j in range(41):
    ye=0
    re=0
    for i in lst3:
        if lst1[j][i]!=0:
            re+=1
    for i in lst4:
        if lst1[j][i]!=0:
            ye+=1
    #Hai câu lệnh trên dùng để đếm xem người thứ j đã tham gia bao nhiêu cuộc hội thoại "Nghiêm trọng" và bao nhiêu cuộc hội thoại "Cực kì nghiêm trọng"
    Red.append(re)
    Yellow.append(ye)
#Đoạn đếm Red, Yellow từng đối tượng.

Valuef=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#Lst chứa giá trị hàm mục tiêu của từng đối tượng
for j in range(41):
    if Red[j]==0 and Yellow[j]==0:
        Valuef[j]=0
    else:
        if Red[j]==0 and (Yellow[j]>0 or Yellow[j]<3):
            Valuef[j]=0
        else:
            for i in range(14):
                if lst1[j][i] == 0:
                    #Do mục tiêu của chúng ta là tìm giá trị nhỏ nhất của hàm mục tiêu. Do đó ta sẽ dùng phép trừ cho các bước tính toán đến hàm cuối cùng
                     Valuef[j]-=lst1[j][i]*lst2[i]
                else:
                     #Mức độ nghiêm trọng của cuộc hội thoại và mức độ đóng góp của từng thành viên vào các cuộc hội thoại sẽ tỉ lệ với nhau theo hàm lũy thừa
                    Valuef[j]-=(0.5**lst1[j][i])*lst2[i]
#Đoạn tính Value Function từng đối tượng.

print("Đối tượng không bị tình nghi là: ")
print()
for j in range(41):
    if Red[j]==0 and Yellow[j]==0:
        print(f"Người có số thứ tự {j+1}")
#In ra danh sách những người không bị tình nghi

print()
print("--------------------------------------------------------------------------------------------------------------------------")
print()
print("Đối tượng ít bị tình nghi là: ")
print()
for j in range(41):
    if Red[j]==0 and Yellow[j]!=0 and Yellow[j]<3:
        print("Người có số thứ tự:",j+1)
#In ra danh sách những người ít bị tình nghi

print()
print("--------------------------------------------------------------------------------------------------------------------------")
print()
print("Đối tượng bị tình nghi là: ")
print()
sorted=sorted(Valuef)
stt=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(sorted)):

         for j in range(41):
            if sorted[i]==Valuef[j] and Valuef[j]!=0:
                stt[i]=j+1
newstt=list(dict.fromkeys(stt))
for i in range(len(newstt)):
    print(f"Người bị tình nghi thứ {i+1} là: Người có số thứ tự: {newstt[i]} với giá trị hàm mục tiêu: {sorted[i]}")        
#In ra danh sách những người bị tình nghi
