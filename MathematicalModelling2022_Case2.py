lst1=[[0,1,4,0,1,0,0,11,0,2,0,0,1,0],
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
[0,0,0,0,0,7,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,2,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,5],
[0,0,0,4,0,0,0,0,0,6,0,0,0,0],
[0,0,0,0,0,8,0,0,2,0,0,0,8,0],
[3,0,0,0,10,0,0,0,0,0,3,4,2,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,5,0,9,0,0,5,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,3,0,6,3,0,0],
[0,0,0,0,0,0,0,0,6,0,0,0,0,0],
[0,0,0,0,0,0,4,0,0,0,0,5,0,0],
[0,0,0,0,0,0,0,0,4,0,0,1,0,0],
[0,0,0,0,0,0,0,7,0,0,0,0,0,0],
[0,0,6,0,9,0,0,0,0,0,5,0,6,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,5,0,0,0,0,0,0,0],
[0,0,5,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,2,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,3,0,0,0,0,1,0,11,0,0,0],
[4,0,0,0,0,0,0,8,0,7,0,0,0,0],
[0,5,0,0,0,0,0,0,0,0,2,0,0,0],
[0,0,0,0,0,10,0,0,0,0,10,0,0,0]]
#lst1 chứa index về "Mức độ đóng góp của từng thành viên trong các cuộc hội thoại" đã được mã hóa.

lst2=[0,0,0,0,1,0,0,0,0,2,0,0,3,0]
#lst2 chứa index về "Mức độ nghiêm trọng của cuộc hội thoại" đã được mã hóa.

lst3=[9,12]
#lst3 chứa index của các cuộc hội thoại "Cực kì nghiêm trọng".

lst4=[4]
#lst4 chứa index của các cuộc hội thoại "Nghiêm trọng".

lst5=[]
#lst5 chứa STT của nhân vật nhóm "Ít bị tình nghi".

lst6=[]
#lst6 chứa STT của nhân vật nhóm "Không bị tình nghi".

lst8=[]
#lst6 chứa STT của nhân vật nhóm "Rất bị tình nghi".

lst7=[]
#lst7 chứa kết quả của hàm mục tiêu.

Danhsach={
1:"Hải", 
2:"Huyền", 
3:"Duy", 
4:"Việt", 
5:"Tân", 
6:"Khuê", 
7:"Mía", 
8:"Giang", 
9:"Phanh", 
10:"Ánh", 
11:"Yến", 
12:"Đan", 
13:"Tô",
14:"Thiện",
15:"Trang", 
16:"Thảo", 
17:"Ngọc", 
18:"Châu", 
19:"Bảo", 
20:"Dương", 
21:"Yang", 
22:"Trường", 
23:"Sơn", 
24:"An", 
25:"Đậu", 
26:"Hà", 
27:"Đào", 
28:"Nguyên",
29:"Bình",
30:"Hương",
31:"Chi",
32:"Nhi",
33:"Trâm",
34:"Đức Anh",
35:"Tuấn",
36:"Minh",
37:"Vân Anh",
38:"Thu",
39:"Tiên",
40:"Diệu",
41:"Hằng"}
#Danhsanh là mã hóa STT theo tên nhân vật.

import os
os.system('cls')
#Xóa màn hình Terminal

##Chương trình con đếm Red&Yellow.
Red=[]
Yellow=[]
#2 lsts chứa số cuộc hội thoại "Cực nghiêm trọng", "Nghiêm trọng" của từng nhân vật.

for j in range(41):
    ye=0
    re=0
    for i in lst3:
        if lst1[j][i]!=0:
            re+=1
    for i in lst4:
        if lst1[j][i]!=0:
            ye+=1
        #2commands đếm số lượng cuộc hội thoại "Cực nghiêm trọng" -Red, "Nghiêm trọng" -Yellow mà nhân vật (j) tham gia.
    Red.append(re)
    Yellow.append(ye)
##-------------------------------

print("Nhóm \"Không bị tình nghi\" gồm:")
print("______________________________")
print()

for j in range(41):
    if Red[j]==0 and Yellow[j]==0:
        if j+1<10:
            print(f"Nhân vật (0{j+1}) - {Danhsach[j+1]}")
        else:
            print(f"Nhân vật ({j+1}) - {Danhsach[j+1]}")
        ##In "0" trước số chỉ 1 chữ số.
        print()
        lst6.append(j)
#In nhóm "Không bị tình nghi" với điều kiện Red=Yellow=0.

print("______________________________")
print("______________________________")

print()
print()
print()

print("Nhóm \"Ít bị tình nghi\" gồm:")
print("______________________________")
print()

for j in range(41):
    if j not in lst6 and Red[j]<2:
        if j+1<10:
            print(f"Nhân vật (0{j+1}) - {Danhsach[j+1]}")
        else:
            print(f"Nhân vật ({j+1}) - {Danhsach[j+1]}")
        print()
        lst5.append(j)
#In nhóm "Ít bị tình nghi" với điều kiện không thuộc nhóm "Không bị tình nghi" và Red<2.

for j in range(41):
    if Red[j]>=2 and Yellow[j]>=1:
        value_function=0
        #Giá trị của hàm mục tiêu.
        #Do mục tiêu: min hàm mục tiêu nên dùng (-) cho tính toán đến hàm tổng.

        for i in range(14):
            if lst1[j][i]!=0:
            #Nếu nhân vật (j) không tham gia cuộc hội thoại i thì không ảnh hưởng giá trị hàm mục tiêu.

                value_function-=(0.5**lst1[j][i])*lst2[i]
                #Mức độ nghiêm trọng và thứ hạng đóng góp vào các cuộc hội thoại sẽ tỉ lệ với nhau theo hàm lũy thừa.
        lst7.append(value_function)

print("______________________________")
print("______________________________")

print()
print()
print()

print("Nhóm \"Rất bị tình nghi\" gồm: (xếp hạng theo khả năng chủ mưu giảm dần)")
print("______________________________")
print()

for i in range(41):
    if i not in lst5 and i not in lst6:
        lst8.append(i)
#Phân hoạch phần bù 2 nhóm kia là nhóm "Rất bị tình nghi".

sorted_lst7=sorted(lst7)
#sorted_lst7 là lst7 xếp theo thứ tự tăng dần.
lst9=[]
#lst9 chứa STT các nhân vật nhóm "Rất bị tình nghi" theo khả năng chủ mưu giảm dần.
dicts={}
#từ điển STT ứng với giá trị hàm mục tiêu.

for i in range(len(lst8)):
    dicts[lst8[i]+1]=lst7[i]
#định nghĩa lần lượt giá trị hàm mục tiêu vào từ điển.

for i in range(len(lst8)):
    for j in dicts:
        if sorted_lst7[i]==dicts[j]:
            lst9.append(j)
#Tra phần từ trùng của sorted và dicts, gán theo thứ tự tăng dần (do tính chất sorted) vào lst9.

for i in range(len(lst9)):
    if lst9[i]<10:
        print(f"{i+1}. Nhân vật (0{lst9[i]}) - {Danhsach[lst9[i]]} (\"Uy tín\" = {sorted_lst7[i]})")
    else:
        print(f"{i+1}. Nhân vật ({lst9[i]}) - {Danhsach[lst9[i]]} (\"Uy tín\" = {sorted_lst7[i]})")
    print()