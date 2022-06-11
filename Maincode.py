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
lst4=[0,10,11,13]
#lst3 là index của các cuộc hội thoại "Cực kì nghiêm trọng"
#lst4 là index của các cuộc hội thoại "Nghiêm trọng"
lst5=[]
#lst5 là list chứa index của các đối tượng "Ít bị tình nghi"
lst6=[]
#lst6 là list chứa index của các đối tượng "Không bị tình nghi"
lst7=[]
#lst7 là list chứa kết quả của hàm mục tiêu cần tìm
print("Đối tượng ít bị tình nghi là: ")
for j in range(41):
    yellow=0
    red=0
    for i in lst3:
        if lst1[j][i]!=0:
            red+=1
    for i in lst4:
        if lst1[j][i]!=0:
            yellow+=1
    #Hai câu lệnh trên dùng để đếm xem người thứ j đã tham gia bao nhiêu cuộc hội thoại "Nghiêm trọng" và bao nhiêu cuộc hội thoại "Cực kì nghiêm trọng"
    if red ==0 and yellow < 3 and yellow!=0:
        print("Người có số thứ tự:",j+1)
        lst5.append(j)
#In ra danh sách những người ít bị tình nghi
    if red !=0 or yellow >=3:
        value_function=0
        #Giá trị của hàm mục tiêu
        for i in range(14):
            if lst1[j][i] == 0:
                #Do mục tiêu của chúng ta là tìm giá trị nhỏ nhất của hàm mục tiêu. Do đó ta sẽ dùng phép trừ cho các bước tính toán đến hàm cuối cùng
                value_function-=lst1[j][i]*lst2[i]
            else:
                #Mức độ nghiêm trọng của cuộc hội thoại và mức độ đóng góp của từng thành viên vào các cuộc hội thoại sẽ tỉ lệ với nhau theo hàm lũy thừa
                value_function-=(0.5**lst1[j][i])*lst2[i]
        lst7.append(value_function)
 
print("Đối tượng không bị tình nghi là: ")
for j in range(41):
    yellow=0
    red=0
    for i in lst3:
        if lst1[j][i]!=0:
            red+=1
    for i in lst4:
        if lst1[j][i]!=0:
            yellow+=1
    if red==0 and yellow == 0:
        print(f"Người có số thứ tự {j+1}")
        lst6.append(j)
lst8=[]
print("Đối tượng bị tình nghi là: ")
for i in range(41):
    if i not in lst5 and i not in lst6:
        lst8.append(i)
for i in range(len(lst7)):
    print("Người có số thứ tự tứ:", lst8[i]+1,", giá trị hàm mục tiêu của họ là: ", lst7[i])
sorted_lst7=sorted(lst7)
lst9=[]
dicts={}

for i in range(len(lst8)):
    dicts[lst8[i]+1]=lst7[i]

print("Xếp hạng đối tượng bị tình nghi dựa trên giá trị hàm mục tiêu:")
for i in range(len(lst7)):
    for j in dicts:
        if sorted_lst7[i]==dicts[j]:
            lst9.append(j)
lst9=list(dict.fromkeys(lst9))
for i in range(len(lst9)):
    print("Người có số thứ tự thứ: ",lst9[i])
