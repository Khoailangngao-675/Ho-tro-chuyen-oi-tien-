from PyQt6.QtWidgets import QApplication , QWidget , QPushButton , QLabel
import sys 


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Met ghe')


button = QPushButton('Click Me', parent=window)
button.setGeometry(100, 100, 100, 30)  # (x,y,width,height)
label = QLabel('print("helloword)', parent=window)


window.show()
app.exec()