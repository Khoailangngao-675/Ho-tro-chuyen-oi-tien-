A = ["Khoa","Kiệt","Khánh","Long","Khang","Nhân"]
A.append("Mai")
A.pop(2)
# pop là xóa giá trị ở số thứ tự 2
A.insert(4,"Minh")
for i in range (len(A)) :
    print(A[i])