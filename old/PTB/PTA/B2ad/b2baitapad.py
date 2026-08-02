class babantronglop :
    def __init__(self,hoten,lop,truong,diemtoan,diemvan,diemanh):
        self.hoten = hoten
        self.lop = lop
        self.truong = truong
        self.diemtoan = diemtoan
        self.diemvan = diemvan
        self.diemanh = diemanh

    def thong_tin(self) :
        return f"Họ và ten {self.hoten} , lớp {self.lop} ,trường {self.truong} , điểm toán{self.diemtoan} ,điểm văn {self.diemvan}, điểm anh {self.diemanh}"
hs1 = babantronglop("Nguyễn Như Khoa","9/6","THCS An Bình",4,4,4)
print(hs1.thong_tin())
hs2 = babantronglop("675", "9/6", "THCS An Bình", 8, 7, 9)
print(hs2.thong_tin())
hs3 = babantronglop("TNTM","9/6","THCS An Bình", 9, 9, 9)
print(hs3.thong_tin())