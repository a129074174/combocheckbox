from enum import Enum

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

class CheckState(Enum):
    NOT_SELECTED = 0
    PARTIAL_SELECTED = 1
    ALL_SELECTED = 2


class ComboCheckBox(QtWidgets.QComboBox):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.checkbox_list = []

        # 定义第一个checkbox为全选
        self.__first_box = QtWidgets.QCheckBox()
        self.__first_box.setText('全选')
        self.__first_box.clicked.connect(self.on_all_clicked)
        # self.checkbox_list.append(self.__first_box)
        self.view = QtWidgets.QListWidget()
        self.__lineedit = QtWidgets.QLineEdit()
        self.__lineedit.setReadOnly(True)
        self.view.setStyleSheet("font-size: 20px;height: 40px; margin-left: 5px")
        self.setStyleSheet("width: 300px; height: 50px; font-size: 25px; font-weight: bold")
        self.setLineEdit(self.__lineedit)
        self.__lineedit.adjustSize()
        self.setModel(self.view.model())
        self.setView(self.view)
        item = QtWidgets.QListWidgetItem(listview=self.view)
        self.view.setItemWidget(item, self.__first_box)
        self.__show_text = ''
        self.check_state = CheckState.NOT_SELECTED

    def set_first_box_text(self, text):
        self.__first_box.setText(text)

    def add_item(self, text):
        checkbox = QtWidgets.QCheckBox()
        checkbox.setText(text)
        self.checkbox_list.append(checkbox)
        self.checkbox_list[-1].clicked.connect(self.on_check_state_changed)
        item = QtWidgets.QListWidgetItem(listview=self.view)
        self.view.setItemWidget(item, checkbox)

    def add_items(self, texts):
        for i in range(len(texts)):
            self.add_item(texts[i])



    # 清空其余item,只保留全选复选框
    def clear(self):
        super().clear()
       # self.add_item(self.__first_box.text())



    def on_all_clicked(self):
        if self.check_state == CheckState.NOT_SELECTED or self.check_state == CheckState.PARTIAL_SELECTED:
            state = True
            self.check_state = CheckState.ALL_SELECTED
            self.set_show_text('全选')
        elif self.check_state == CheckState.ALL_SELECTED:
            state = False
            self.check_state = CheckState.NOT_SELECTED
            self.set_show_text('')
        else:
            pass
        for box in self.checkbox_list:
            box.setChecked(state)

    def on_check_state_changed(self):
        self.__show_text = ''
        selected_count = 0
        for box in self.checkbox_list:
            if box.isChecked():
                self.__show_text += box.text() + ';'
                selected_count+=1
        if 0< selected_count < len(self.checkbox_list):
            self.check_state = CheckState.PARTIAL_SELECTED
            self.__first_box.setChecked(False)
            self.set_show_text(self.__show_text)
        elif selected_count == len(self.checkbox_list) :
            self.check_state = CheckState.ALL_SELECTED
            self.__first_box.setChecked(True)
            self.set_show_text('全选')
        else:
            self.check_state = CheckState.NOT_SELECTED
            self.set_show_text('')



    def set_show_text(self, text):
        self.__show_text = text
        self.__lineedit.setText(self.__show_text)




