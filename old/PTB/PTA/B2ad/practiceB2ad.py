class VatNuoi :
    def __init__(self,giong,mausac,tuoi,cannang) :
        self.giong = giong
        self.mausac = mausac
        self.tuoi = tuoi
        self.cannang = cannang

    def thong_tin(self):
        return f"Giống : {self.giong} , màu {self.mausac} , tuổi {self.tuoi} , cân nặng {self.cannang}"


VatNuoi_1 = VatNuoi("mèo","đen",67,8)
print(VatNuoi_1.thong_tin())