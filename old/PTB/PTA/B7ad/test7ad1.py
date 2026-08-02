import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6 import uic

# Lấy đường dẫn thư mục hiện tại của file code
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_DIR = os.path.join(BASE_DIR, "ui")

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load file UI bằng đường dẫn linh hoạt
        uic.loadUi(os.path.join(UI_DIR, "login.ui"), self)
        self.btnRegister.clicked.connect(self.show_register)
        self.btnLogin.clicked.connect(self.check_login)
        self.msg_box = QMessageBox()

    def check_login(self):
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        if email == "Kh04" and password == "1":
            main.show()
            self.close()
        else:
            self.msg_box.setText("Vui lòng kiểm tra lại thông tin đăng nhập")
            self.msg_box.setIcon(QMessageBox.Icon.Warning)
            self.msg_box.exec()

    def show_register(self):
        register.show()
        self.close()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(UI_DIR, "dangky.ui"), self)
        self.btnLogin.clicked.connect(self.show_login)
        self.msg_box = QMessageBox()

    def show_login(self):
        login.show()
        self.close()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(UI_DIR, "main.ui"), self)

        # kết nối nút bấm
        self.cua_hang.clicked.connect(self.show_cuahang)
        self.ttong.clicked.connect(self.may_tinh)

    def may_tinh(self):
        # Giá tiền
        gtTC = 40000
        gtNL = 80000
        gtB = 40000
        gtCOCA = 25000

        # Lấy số lượng từ SpinBox
        NL = self.so_luong_NL.value()
        TC = self.so_luong_TC.value()
        COCA = self.so_luong_COCA.value()
        B = self.so_luong_B.value()

        # Tính tổng tiền
        tong = (NL * gtNL) + (TC * gtTC) + (B * gtB) + (COCA * gtCOCA)

        # Hiển thị kết quả
        self.label_11.setText(f"{tong} VND")

    def show_cuahang(self):
        Cua_Hang.show()
        self.close()

class cuahang(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(UI_DIR, "cuahang.ui"), self)
        self.pushButton.clicked.connect(self.tinh_tien_cuahang)

    def tinh_tien_cuahang(self):
        # giá tiền
        tra_sua = 20000
        matcha_latte = 25000
        tra_dao = 20000
        milo_dam = 15000
        banh_tran_tron = 15000
        banh_flan = 15000

        # lấy giá trị 
        SL_trasua = self.so_luong_trasua.value()
        SL_tradao = self.so_luong_tradao.value()
        SL_matchalatte = self.so_luong_matchalatte.value()
        SL_milo_dam = self.so_luong_milodam.value()
        SL_banh_tran_tron = self.so_luong_banhtrantron.value()
        SL_banh_flan = self.so_luong_banhflan.value()

        # tính toán
        so_tien_cuahang = (SL_trasua*tra_sua) + (SL_tradao*tra_dao) + (SL_matchalatte*matcha_latte) + (SL_milo_dam * milo_dam) + (SL_banh_tran_tron * banh_tran_tron) + (SL_banh_flan * banh_flan)

        # hiển giá tiền 
        self.tinh_tien_cua_hang.setText(f"{so_tien_cuahang} VND")
        self.liet_ke_san_pham.setText(
            f"Số lượng:\n"
            f"Trà sữa: {SL_trasua}\n"
            f"Trà đào: {SL_tradao}\n"
            f"Matcha latte: {SL_matchalatte}\n"
            f"Milo dầm: {SL_milo_dam}\n"
            f"Bánh tráng trộn: {SL_banh_tran_tron}\n"
            f"Bánh flan: {SL_banh_flan}"
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Thiết lập font chữ hỗ trợ tiếng Việt
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    login = Login()
    login.show()
    register = Register()
    main = Main()
    Cua_Hang = cuahang()
    
    sys.exit(app.exec())

