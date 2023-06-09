


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 698)
        Form.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"background-color: rgb(0, 170, 127);")
        self.slider_deyer = QtWidgets.QSlider(Form)
        self.slider_deyer.setGeometry(QtCore.QRect(160, 110, 371, 31))
        self.slider_deyer.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.slider_deyer.setStyleSheet("color: rgb(170, 0, 0);")
        self.slider_deyer.setMaximum(20)
        self.slider_deyer.setOrientation(QtCore.Qt.Horizontal)
        self.slider_deyer.setObjectName("slider_deyer")
        self.uzunlug_deyer = QtWidgets.QLabel(Form)
        self.uzunlug_deyer.setGeometry(QtCore.QRect(420, 50, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.uzunlug_deyer.setFont(font)
        self.uzunlug_deyer.setAlignment(QtCore.Qt.AlignCenter)
        self.uzunlug_deyer.setObjectName("uzunlug_deyer")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(230, 50, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.boyukherf_box = QtWidgets.QCheckBox(Form)
        self.boyukherf_box.setGeometry(QtCore.QRect(210, 180, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.boyukherf_box.setFont(font)
        self.boyukherf_box.setStyleSheet("QCheckBox::indicator {\n"
"    width: 40px;\n"
"    height: 40px;\n"
"}")
        self.boyukherf_box.setObjectName("boyukherf_box")
        self.kicikherf_box = QtWidgets.QCheckBox(Form)
        self.kicikherf_box.setGeometry(QtCore.QRect(210, 260, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.kicikherf_box.setFont(font)
        self.kicikherf_box.setStyleSheet("QCheckBox::indicator {\n"
"    width: 40px;\n"
"    height: 40px;\n"
"}")
        self.kicikherf_box.setObjectName("kicikherf_box")
        self.simvollar_box = QtWidgets.QCheckBox(Form)
        self.simvollar_box.setGeometry(QtCore.QRect(210, 340, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.simvollar_box.setFont(font)
        self.simvollar_box.setStyleSheet("QCheckBox::indicator {\n"
"    width: 40px;\n"
"    height: 40px;\n"
"}")
        self.simvollar_box.setObjectName("simvollar_box")
        self.yarat_buton = QtWidgets.QPushButton(Form)
        self.yarat_buton.setGeometry(QtCore.QRect(220, 440, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.yarat_buton.setFont(font)
        self.yarat_buton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.yarat_buton.setStyleSheet("color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.yarat_buton.setObjectName("yarat_buton")
        self.kopyala_buton = QtWidgets.QPushButton(Form)
        self.kopyala_buton.setGeometry(QtCore.QRect(220, 500, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.kopyala_buton.setFont(font)
        self.kopyala_buton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kopyala_buton.setStyleSheet("color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.kopyala_buton.setObjectName("kopyala_buton")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 580, 601, 91))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.main_label = QtWidgets.QLabel(self.groupBox)
        self.main_label.setGeometry(QtCore.QRect(10, 10, 581, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.main_label.setFont(font)
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setObjectName("main_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.uzunlug_deyer.setText(_translate("Form", "0"))
        self.label_2.setText(_translate("Form", "Uzunluq :"))
        self.boyukherf_box.setText(_translate("Form", "Böyük hərflər"))
        self.kicikherf_box.setText(_translate("Form", "Kiçik hərflər"))
        self.simvollar_box.setText(_translate("Form", "Simvollar"))
        self.yarat_buton.setText(_translate("Form", "Yarat"))
        self.kopyala_buton.setText(_translate("Form", "Kopyala"))
        self.main_label.setText(_translate("Form", "None"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
