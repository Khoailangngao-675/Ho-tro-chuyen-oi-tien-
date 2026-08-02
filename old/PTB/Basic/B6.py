m = int(input("Hãy nhập mật khẩu:"))
print("MK của bạn :",m)
xacnhan = int(input("nếu đồng ý thì bấm số 1 , ko đồng ý thì bấm số 2:"))
while xacnhan == 2:
    m=int(input("Hãy nhập mật khẩu:"))
    print("MK của bạn :",m)
    xacnhan = int(input("nếu đồng ý thì bấm số 1 ko đồng ý thì bấm số 2"))
nguoidung = int(input("hãy nhập mk "))
while nguoidung != m :
    nguoidung = int(input("sai rồi hãy nhập lại mk "))
print("đăng nhập thành công")