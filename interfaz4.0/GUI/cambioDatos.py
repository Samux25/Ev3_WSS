import sys
#sys.path.append("D:/Codigos/Python Desarrollo/Ev3_WSS/Control")
sys.path.append("C:/taller/WSS/Control") #Ruta tito
from CTRR import * 
from PyQt6.QtWidgets import QMainWindow, QLineEdit
from GUI.ui_cambioDatos import Ui_MainWindow
from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtWidgets import QApplication

class cambioDatos(QMainWindow, Ui_MainWindow):
    def __init__(self,rut,datos):
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

        self.rut = rut
        self.nombreCompletoCambio.setText(datos[0])
        self.direccionResidenciaCambio.setText(datos[1])
        self.telefonoCambio.setText(datos[2])
        self.CorreoCambio.setText(datos[3])
        self.EspecialidadCambio.setText(datos[4])

        self.show()

        self.ConfirmCambio.clicked.connect(self.confirmarCambiarDatos)

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

    def confirmarCambiarDatos(self):
        campo = ['nombre_completo','correo', 'telefono', 'direccion_residencia','especialidad']
        nombre = self.nombreCompletoCambio.text()
        correo = self.CorreoCambio.text()
        telefono = self.telefonoCambio.text()
        direccion  = self.direccionResidenciaCambio.text()
        especialidad = self.EspecialidadCambio.text()
        self.contr.actualizarInformacion(self.rut,campo[0],nombre)
        self.contr.actualizarInformacion(self.rut,campo[1],correo)
        self.contr.actualizarInformacion(self.rut,campo[2],telefono)
        self.contr.actualizarInformacion(self.rut,campo[3],direccion)
        self.contr.actualizarInformacion(self.rut,campo[4],especialidad)
        self.lblmss.setText("Vuelva a iniciar sesion para visualizar cambios")