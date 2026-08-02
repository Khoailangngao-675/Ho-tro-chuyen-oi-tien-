# class skibidi :
#     def __init__ (self,mau,kichthuoc,giatien,nhucau):
#         self.mau = mau
#         self.kichthuoc = kichthuoc
#         self.giatien = giatien
#         self.nhucau = nhucau

#         print(f"mau : {mau} , kich thuc {kichthuoc} ,giatien {giatien} , nhu cau {nhucau}")

# pls_donate = skibidi("do","trung binh", "12 trieu" , "hoctap")
# print(pls_donate)

# pls_donate.mau = "cam"
# print(f"mau dc doi",pls_donate.mau)

# # Trong các phươg thức hệ thống của lớp . phương thức __init__() đóng vai tò rất quan trọng 
# # Nó gán tự động các thuộc tính cho đối tượng khi mới khởi tạo


class HinhChuNhat :
    def __init__(self,CD,CR):
        self.CD =CD
        self.CR = CR
    def tinhtoan (self):
        dientich = self.CD * self.CR
        print(f"Diện tích của hình chữ nhật là{dientich} " )

        chuvi = (self.CR + self.CD) * 2
        print(f"Chu vi hình chữ nhật là {chuvi}")


x = int(input("hãy nhập Chiều rộng"))
y = int(input("hay nhap Chieu Rong"))
hinh1 = HinhChuNhat(x,y)



