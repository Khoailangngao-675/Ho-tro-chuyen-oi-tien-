# class Xe:
#     def __init__(self, hang, mau_sac, gia_tien):
#         self.hang = hang
#         self.mau_sac = mau_sac
#         self.gia_tien = gia_tien
#     def khoi_dong(self):
#         print(f"xe {self.hang} đã khởi động")

# class XeHoi(Xe):
#     def chay_bang_bon_banh(self):
#         print(f"xe {self.hang} chạy bằng động cơ")
# class XeDap(Xe):
#     def chay_bang_hai_chan(self):
#         print(f"xe {self.hang} chạy bằng hai chân")

# xe_hoi_1 = XeHoi("Toyota", "Đỏ", 500000000)
# xe_dap_1 = XeDap("Martin", "Xanh", 3000000)
# xe_hoi_1.khoi_dong()
# xe_hoi_1.chay_bang_bon_banh()
# xe_dap_1.khoi_dong()
# xe_dap_1.chay_bang_hai_chan()









# class ThietBiDien:
#     def __init__(self,ten,cong_suat,hang_san_xuat):
#         self.ten = ten
#         self.cong_suat = cong_suat
#         self.hang_san_xuat = hang_san_xuat
#     def thongtin(self):
#         print(f"tên {self.ten} , công suất {self.cong_suat} , hãng sản xuất {self.hang_san_xuat}")
# class Quat(ThietBiDien):
#     def quatquay(self):
#         print("Quạt đang quay")
# class Den(ThietBiDien) :
#     def densang(self):
#         print("đèn đang sáng")
# den_1 = ThietBiDien("Đèn trắng", 12,"Skibidi")
# den_1.thongtin()





class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1,0 

        while s[i] == " ":
            i = i - 1
        while i >= 0 and s[i] != " ":
            length = length + 1
            i = i - 1
        return length