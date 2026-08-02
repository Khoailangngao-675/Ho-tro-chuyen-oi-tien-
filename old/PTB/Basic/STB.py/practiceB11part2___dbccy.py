def in_danh_sach_va_tong(danh_sach):
    print("Danh sách các phân tử")
    for so in danh_sach :
        print(so)
    
    tong = sum(danh_sach)
    print("tổng của danh sách ", tong)


danh_sach =[]
n = int(input("Nhập số phân tử trong danh sách :"))
for i in range(n):
    so = int(input("Nhập phân tử thứ{}:" . format(i+1)))
    danh_sach.append(so)

in_danh_sach_va_tong(danh_sach)