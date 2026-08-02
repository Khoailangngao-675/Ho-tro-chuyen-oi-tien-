# lệnh in 
# lệnh được sử dụng như thế này if xau1 in xau 2 


#lệnh find()
#tìm xem vị trí ở chỗi ở đâu


#lệnh replace() vd chỗi là 
# VD: n = "i like me" khi ghi n.replace("me","My")
#thì nó sẽ thành "i like My"



#lệnh split
# tách 
ngay = input("nhập ngày tháng năm vào theo định dạng ngày/tháng/năm")
x = ngay.split("/")
ngay = x[0]
thang = x [1]
nam =x[2]
print("Ngày", ngay , "Tháng",thang , "Năm",nam)