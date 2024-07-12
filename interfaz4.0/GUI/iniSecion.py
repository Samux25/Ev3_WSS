import sys
#sys.path.append("D:/Codigos/Python Desarrollo/Ev3_WSS/Control")
sys.path.append("C:/taller/WSS/Control") #Ruta tito
from CTRR import * 
from PyQt6.QtWidgets import QMainWindow, QLineEdit
from GUI.ui_inicioSesion import Ui_MainWindow
from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtWidgets
from GUI.trab import Trabajador
from GUI.supervisor import Supervisor
from PyQt6.QtCore import Qt, QPointF

class Login(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.rutUser.setFocus()
        self.rutUser.returnPressed.connect(self.contraUser.setFocus)
        self.contraUser.returnPressed.connect(self.iniciarSesion.click)
        self.bt_normal.hide()
        self.click_posicion = None
        self.bt_minimize.clicked.connect(lambda: self.showMinimized())
        self.bt_normal.clicked.connect(self.control_bt_normal)
        self.bt_maximize.clicked.connect(self.control_bt_maximize)
        self.bt_close.clicked.connect(lambda: self.close())
        self.checkBox.stateChanged.connect(self.mostrar_contrasena)
        
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        self.contr = Controlador()
        self.InicioSesion()
        self.show()


    def control_bt_normal(self): 
        self.showNormal()
        self.bt_normal.hide()
        self.bt_maximize.show()

    def control_bt_maximize(self): 
        self.showMaximized()
        self.bt_maximize.hide()
        self.bt_normal.show()

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.click_posicion = event.globalPosition()

    def mover_ventana(self, event):
        if not self.isMaximized():
            if event.buttons() == Qt.MouseButton.LeftButton:
                delta = QPointF(event.globalPosition() - self.click_posicion)
                self.move(self.pos() + delta.toPoint())
                self.click_posicion = event.globalPosition()
                event.accept()
        if event.globalPosition().y() <= 5 or event.globalPosition().x() <= 5:
            self.showMaximized()
            self.bt_maximize.hide()
            self.bt_normal.show()
        else:
            self.showNormal()
            self.bt_normal.hide()
            self.bt_maximize.show()
    
    def mostrar_contrasena(self, clicked):
        if clicked:
            self.contraUser.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.contraUser.setEchoMode(QLineEdit.EchoMode.Password)

    def ingresar(self):
        if self.rutUser.text() == "":
            self.lblmss.setText("Ingrese su RUT")
            self.rutUser.setFocus()
        elif self.contraUser.text() == "":
            self.lblmss.setText("Ingrese su contraseña")
            self.contraUser.setFocus()
        else:
            self.lblmss.setText("")
            rut = self.rutUser.text()
            contraseña = self.contraUser.text()
            usurio = self.contr.inicioSesion(rut,contraseña)
            if usurio[1] == "Trabajador":
                self.lblmss.setText(usurio[0])
                datos = self.contr.visualizarEmpleadoRut(rut)
                Trabajador(datos)
                self.hide()
            elif usurio[1] == "Supervisor":
                self.lblmss.setText(usurio[0])
                datos = self.contr.visualizarEmpleadoRut(rut)
                Supervisor(datos)
                self.hide()
            else:
                self.lblmss.setText(usurio[0])

    def InicioSesion(self):
        self.iniciarSesion.clicked.connect(self.ingresar)
