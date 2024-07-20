import sys
#sys.path.append("D:/Codigos/Python Desarrollo/Ev3_WSS/Control")
sys.path.append("C:/taller/WSS/Control") #Ruta tito
from CTRR import *
from PyQt6.QtWidgets import QMainWindow
from GUI.ui_anadirEmpleado import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore, QtWidgets

from PyQt6.QtCore import Qt, QPointF

class anadirEmpleado(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_normal.hide()
        self.click_posicion = None
        self.bt_minimize.clicked.connect(lambda: self.showMinimized())
        self.bt_normal.clicked.connect(self.control_bt_normal)
        self.bt_maximize.clicked.connect(self.control_bt_maximize)
        self.bt_close.clicked.connect(lambda: self.close())
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        self.contr = Controlador()
        self.show()

        self.respuestaCargo = None
        self.cargoSupervisor.clicked.connect(self.cargo)
        self.cargoTrabajador.clicked.connect(self.cargo)
        self.anadirEmpleado.clicked.connect(self.AnadirEmpleado)

    
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

    def cargo(self):
        if self.sender() == self.cargoSupervisor:
            self.respuestaCargo = "Supervisor"
        elif self.sender() == self.cargoTrabajador:
            self.respuestaCargo = "Trabajador"
        print(f"Cargo: {self.respuestaCargo}")

    def AnadirEmpleado(self):
        rut = self.rutEmplNuevo.text()
        nombre = self.nombreEmplNuevo.text()
        correo = self.CorreoEmplNuevo.text()
        telefono = self.telefonoEmplNuevo.text()
        direccion = self.direcEmplNuevo.text()
        especialidad = self.EspecialidadEmplNuevo.text()
        contraseña = self.contrasenaEmplNuevo.text()
        msg = self.contr.agregarEmpleado(rut,nombre,correo,telefono,direccion,self.respuestaCargo,especialidad,contraseña)
        self.lblmss.setText(msg)
        self.respuestaCargo = None