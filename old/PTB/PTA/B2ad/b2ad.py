class xe :
    def __init__(self,hang,mau,nam_san_xuat,gia_tien) :
        self.hang = hang
        self.mau = mau
        self.nam_san_xuat = nam_san_xuat
        self.gia_tien = gia_tien


    def thong_tin_xe (self) : 
        return f"hãng xe {self.hang} ,Màu sắc : {self.mau} , năm sản xuất {self.nam_san_xuat} , Giá tiền {self.gia_tien}VND"
    def thue_xe(self,so_ngay):
     gia_thue =  self.gia_tien * 0.001 * so_ngay
     return f"Giá thuê xe{gia_thue} , trong {so_ngay} ngay"

# mẫu xe
xe_1 = xe("Toyota","đỏ" ,2020 ,500)
print(xe_1.thong_tin_xe())


# truy cập đổi tên đỏi màu
xe_1.mau = "cam"
print(xe_1.thong_tin_xe())


# giá thuê xe nhân 0.001 so ngày thuê

print(xe_1.thue_xe(5))