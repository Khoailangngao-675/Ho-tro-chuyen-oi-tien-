n = int(input("Nhập số bì kiểm tra em đã làm"))
while n < 0 :
    n = int(input("Hay nhap lai bang so duong"))
diem =[]
m = 0
for i in range(1,n+1):
    m = float(input("Nhập só điêm của bạn"))
    diem.append(m)
diem.sort()
diem_moi = []

for d in diem:
    if d >= 8:
        diem_moi.append(d)

print("Số điểm lớn hơn hoặc bằng 8 của bạn là", diem_moi)
