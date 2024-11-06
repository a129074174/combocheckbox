from combocheckbox import ComboCheckBox
from PySide6 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.combo_checkbox = ComboCheckBox(self)
        self.setCentralWidget(self.combo_checkbox)
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = MainWindow()
    win.setFixedSize(600, 400)

    # win.combo_checkbox.add_item('1班')
    class_list = [str(i) + '班' for i in range(1, 11)]
    win.combo_checkbox.add_items(class_list)
    # win.combo_checkbox.clear()

    win.show()
    app.exec()

