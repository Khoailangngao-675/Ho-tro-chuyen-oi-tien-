import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow , QApplication
from PyQt6.QtCore import Qt


# Tạo lớp MainWindow kế thừa từ QMainWidow
class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow,self).__init__()

        # Load phần UI mà mình tạo
        self.ui = uic.loadUI(r"D:\PTB\PTI\B7\listwidget.ui",self)

        self.list = ["Dog","Cat","Duck"]
        self.ui.listWidget.addItems(self.list)
        self.ui.listWidget.InsertItem(0,"Tiger")
        self.ui.listWidget.takeItem(3)
        #tiềm kiếm thông tin
        matched_items = self.ui.listWiget.findItems("hi",Qt.MatchFlag.MatchContains)
        for i in range(self.ui.listWidget.count()):
            it = self.ui.listWidget.item(i)
            it.setHidden(it not in matched_items)


        self.show()


if __name__ == "_main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())