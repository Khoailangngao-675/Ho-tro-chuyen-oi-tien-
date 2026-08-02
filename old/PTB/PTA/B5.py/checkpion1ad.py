class HocSinh:
    def __init__(self,ten,dia_chi,chieu_cao,can_nang,hoc_luc) :
        self.ten = ten 
        self.dia_chi = dia_chi
        self.chieu_cao = chieu_cao
        self.can_nang = can_nang
        self.hoc_luc = hoc_luc
    def chuyen_nha(self,dia_chi_moi):
        self.dia_chi = dia_chi_moi
        print("Đã cập nhật địa chỉ thành công")
    def kham_suc_khoe(self,chieu_cao_moi,can_nang_moi):
        self.chieu_cao = chieu_cao_moi
        self.can_nang = can_nang_moi
        print("Đã cập nhật chiều cao và cân nặng")
    def bang_thong_tin(self):
        print(" ================== BẢNG THÔNG TIN ==================")

        print(f"Họ và tên của học sinh {self.ten} , Địa chỉ của HS {self.dia_chi} ") 

        print("====== SỨC KHỎE ======")

        print(f"Chiều cao {self.chieu_cao} , cân nặng {self.can_nang}")

        print("========= HỌC LỰC ==========")

        print(f"Học lực {self.hoc_luc}")

hocsinh1=HocSinh("Ngyen van A","Dong Nai",160,47,"Gioi")

hocsinh1.chuyen_nha("DONG NAI")

hocsinh1.kham_suc_khoe(165,50)

hocsinh1.bang_thong_tin()