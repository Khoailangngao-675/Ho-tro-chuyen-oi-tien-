class brank :
    def __init__(self,ten_ngan_hang,ten_chu_tai_khoan,so_tai_khoan,so_tien_trong_tai_khoan):
        self.ten_ngan_hang = ten_ngan_hang
        self.ten_chu_tai = ten_chu_tai_khoan
        self.so_tai_khoan =so_tai_khoan
        self.so_tien_trong_tai_khoan =so_tien_trong_tai_khoan
    def rut_tien(self,so_tien_rut):
        self.so_tien_rut = so_tien_rut
        if so_tien_rut > self.so_tien_trong_tai_khoan:
            print("Số tiền trong tài khoản ko đủ")
        elif so_tien_rut > self.so_tien_trong_tai_khoan:
            print("số tiền rút ko hợp lệ")
        else :
            self.so_tien_trong_tai_khoan -= so_tien_rut
            print(f"đã rút thành công {so_tien_rut} VND số du hiện tại{self.so_tien_trong_tai_khoan}")
    def them_de(self,so_tien_them):
        self.so_tien_trong_tai_khoan += so_tien_them
        print(f"nạp vip thành công số dư hiện tại{self.so_tien_trong_tai_khoan}")
    def thong_tin(self):
        print(f"số tài khoản là{self.so_tai_khoan} số dư hiện tại {self.so_tien_trong_tai_khoan} ")
TNH = input("tenn ngan hang ")
TCH = input("ten j ")
STK = input("so tai khoan la j vay ")
SD = int(input("so tie dang co "))
STR = int(input("muon rut bao nhieu "))
STN = int(input("muon nap vip ba nhieu "))
tai_khoan_cua_ban = brank(TNH,TCH,STK,SD)

tai_khoan_cua_ban.them_de(STN)

tai_khoan_cua_ban.rut_tien(STR)

tai_khoan_cua_ban.thong_tin()