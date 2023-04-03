from PyQt5.QtWidgets import *
from pencere import Ui_Form
import random
import string
import pyperclip

class Ekran(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Şifrə Yaradıcı")
        self.app1 = Ui_Form()
        self.app1.setupUi(self)
        self.app1.slider_deyer.valueChanged.connect(self.slider_deyis)
        self.app1.yarat_buton.clicked.connect(self.yarat)
        self.app1.kopyala_buton.clicked.connect(self.kopyala)
        self.k_h = False
        self.b_h = False
        self.s_h = False
        self.len = 0
    def cap_et(self,text):
        self.app1.main_label.setText(text)
    def kopyala(self):
        pyperclip.copy(self.app1.main_label.text())
    
    def pass_gen(self,lowercase, uppercase, symbols, length):
    
        characters = string.ascii_letters + string.digits + string.punctuation
        allowed_characters = string.digits
    
        if lowercase:
            allowed_characters += string.ascii_lowercase
    

        if uppercase:
            allowed_characters += string.ascii_uppercase
    

        if symbols:
            allowed_characters += string.punctuation

        password = ''.join(random.choice(allowed_characters) for i in range(length))
        
        return password
    
    def yarat(self):
    
        if self.app1.boyukherf_box.isChecked():
            self.b_h = True
        else:
            self.b_h = False
        if self.app1.kicikherf_box.isChecked():
            self.k_h = True
        else:
            self.k_h = False
        if self.app1.simvollar_box.isChecked():
            self.s_h = True
        else:
            self.s_h = False
        value = self.app1.slider_deyer.value()
        self.len = value
        
        p = self.pass_gen(self.k_h,self.b_h,self.s_h,self.len)
        
        self.cap_et(p)
    
        
    def slider_deyis(self, value):
        self.app1.uzunlug_deyer.setText(str(value))
    
    
    

app = QApplication([])
ekran = Ekran()
ekran.show()
app.exec_()
