import sys
#sys.path.append("D:/Codigos/Python Desarrollo/Ev3_WSS/Control")
sys.path.append("C:/taller/WSS/Control") #Ruta tito
from CTRR import *
from PyQt6.QtWidgets import QMainWindow
from GUI.ui_supervisor import Ui_MainWindow
from GUI.cambioDatos import cambioDatos
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidgetItem
from PyQt6 import QtCore, QtWidgets

from PyQt6.QtCore import Qt, QPointF

class Supervisor(QMainWindow, Ui_MainWindow):
    def __init__(self,rut, datos):
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
        self.datos = datos
        self.rut = rut
        self.NombreSuper.setText(datos[0])
        self.DireccionSuper.setText(datos[1])
        self.TelefonoSuper.setText(datos[2])
        self.CorreoSuper.setText(datos[3])
        self.show()

        self.cambiarInfoSuper.clicked.connect(self.abrirCambioDatos)
        self.ElegirArtSuper.activated.connect(self.decision)
        self.resultado = ""
        self.actualizarARTS.clicked.connect(self.mostrarTablaART)
        self.actualizar.clicked.connect(self.mostrarTablaTrabajadores)
        self.ElegirArtSuper.activated.connect(self.decision)
        self.ordenarActividad.clicked.connect(self.mostrarTablaArtActividad)

        self.respuestasPS = []
        self.respuestasRc1 =[]
        self.respuestasRc2 =[]

        self.respuesta_Ps1 = None
        self.respuesta_Ps2 = None
        self.respuesta_Ps3 = None
        self.respuesta_Ps4 = None
        self.respuesta_Ps5 = None
        self.respuesta_Ps6 = None

        self.respuesta_superRc1Pr1 = None
        self.respuesta_superRc1Pr2 = None
        self.respuesta_superRc1Pr3 = None
        self.respuesta_superRc1Pr4 = None
        self.respuesta_superRc1Pr5 = None
        self.respuesta_superRc1Pr6 = None
        self.respuesta_superRc1Pr7 = None
        self.respuesta_superRc1Pr8 = None

        self.respuesta_superRc2Pr1 = None
        self.respuesta_superRc2Pr2 = None
        self.respuesta_superRc2Pr3 = None
        self.respuesta_superRc2Pr4 = None
        self.respuesta_superRc2Pr5 = None
        self.respuesta_superRc2Pr6 = None
        self.respuesta_superRc2Pr7 = None
        self.respuesta_superRc2Pr8 = None

        self.Ps1_si.clicked.connect(self.pregunta1)
        self.Ps1_no.clicked.connect(self.pregunta1)
        self.Ps2_si.clicked.connect(self.pregunta2)
        self.Ps2_no.clicked.connect(self.pregunta2)
        self.Ps3_si.clicked.connect(self.pregunta3)
        self.Ps3_no.clicked.connect(self.pregunta3)
        self.Ps4_si.clicked.connect(self.pregunta4)
        self.Ps4_no.clicked.connect(self.pregunta4)
        self.Ps5_si.clicked.connect(self.pregunta5)
        self.Ps5_no.clicked.connect(self.pregunta5)
        self.Ps6_si.clicked.connect(self.pregunta6)
        self.Ps6_no.clicked.connect(self.pregunta6)

        self.superRc1Pr1_si.clicked.connect(self.RiesgCrit1Pr1)
        self.superRc1Pr1_no.clicked.connect(self.RiesgCrit1Pr1)
        self.superRc1Pr2_si.clicked.connect(self.RiesgCrit1Pr2)
        self.superRc1Pr2_no.clicked.connect(self.RiesgCrit1Pr2)
        self.superRc1Pr3_si.clicked.connect(self.RiesgCrit1Pr3)
        self.superRc1Pr3_no.clicked.connect(self.RiesgCrit1Pr3)
        self.superRc1Pr4_si.clicked.connect(self.RiesgCrit1Pr4)
        self.superRc1Pr4_no.clicked.connect(self.RiesgCrit1Pr4)
        self.superRc1Pr5_si.clicked.connect(self.RiesgCrit1Pr5)
        self.superRc1Pr5_no.clicked.connect(self.RiesgCrit1Pr5)
        self.superRc1Pr6_si.clicked.connect(self.RiesgCrit1Pr6)
        self.superRc1Pr6_no.clicked.connect(self.RiesgCrit1Pr6)
        self.superRc1Pr7_si.clicked.connect(self.RiesgCrit1Pr7)
        self.superRc1Pr7_no.clicked.connect(self.RiesgCrit1Pr7)
        self.superRc1Pr8_si.clicked.connect(self.RiesgCrit1Pr8)
        self.superRc1Pr8_no.clicked.connect(self.RiesgCrit1Pr8)

        self.superRc2Pr1_si.clicked.connect(self.RiesgCrit2Pr1)
        self.superRc2Pr1_no.clicked.connect(self.RiesgCrit2Pr1)
        self.superRc2Pr2_si.clicked.connect(self.RiesgCrit2Pr2)
        self.superRc2Pr2_no.clicked.connect(self.RiesgCrit2Pr2)
        self.superRc2Pr3_si.clicked.connect(self.RiesgCrit2Pr3)
        self.superRc2Pr3_no.clicked.connect(self.RiesgCrit2Pr3)
        self.superRc2Pr4_si.clicked.connect(self.RiesgCrit2Pr4)
        self.superRc2Pr4_no.clicked.connect(self.RiesgCrit2Pr4)
        self.superRc2Pr5_si.clicked.connect(self.RiesgCrit2Pr5)
        self.superRc2Pr5_no.clicked.connect(self.RiesgCrit2Pr5)
        self.superRc2Pr6_si.clicked.connect(self.RiesgCrit2Pr6)
        self.superRc2Pr6_no.clicked.connect(self.RiesgCrit2Pr6)
        self.superRc2Pr7_si.clicked.connect(self.RiesgCrit2Pr7)
        self.superRc2Pr7_no.clicked.connect(self.RiesgCrit2Pr7)
        self.superRc2Pr8_si.clicked.connect(self.RiesgCrit2Pr8)
        self.superRc2Pr8_no.clicked.connect(self.RiesgCrit2Pr8)

        
    def pregunta1(self):
        if self.sender() == self.Ps1_si:
            self.respuesta_PS1 = "SI"
        elif self.sender() == self.Ps1_no:
            self.respuesta_PS1 = "NO"
        print(f"Pregunta 1: {self.respuesta_PS1}")

    def pregunta2(self):
        if self.sender() == self.Ps2_si:
            self.respuesta_PS2 = "SI"
        elif self.sender() == self.Ps2_no:
            self.respuesta_PS2 = "NO"
        print(f"Pregunta 2: {self.respuesta_PS2}")

    def pregunta3(self):
        if self.sender() == self.Ps3_si:
            self.respuesta_PS3 = "SI"
        elif self.sender() == self.Ps3_no:
            self.respuesta_PS3 = "NO"
        print(f"Pregunta 3: {self.respuesta_PS3}")

    def pregunta4(self):
        if self.sender() == self.Ps4_si:
            self.respuesta_PS4 = "SI"
        elif self.sender() == self.Ps4_no:
            self.respuesta_PS4 = "NO"
        print(f"Pregunta 4: {self.respuesta_PS4}")

    def pregunta5(self):
        if self.sender() == self.Ps5_si:
            self.respuesta_PS5 = "SI"
        elif self.sender() == self.Ps5_no:
            self.respuesta_PS5 = "NO"
        print(f"Pregunta 5: {self.respuesta_PS5}")

    def pregunta6(self):
        if self.sender() == self.Ps6_si:
            self.respuesta_PS6 = "SI"
        elif self.sender() == self.Ps6_no:
            self.respuesta_PS6 = "NO"
        print(f"Pregunta 6: {self.respuesta_PS6}")


    def RiesgCrit1Pr1(self):
        if self.sender() == self.superRc1Pr1_si:
            self.respuesta_Rc1Pr1 = "SI"
        elif self.sender() == self.superRc1Pr1_no:
            self.respuesta_Rc1Pr1 = "NO"
        print(f"ResgoCrit1Pregunta 1: {self.respuesta_Rc1Pr1}")

    def RiesgCrit1Pr2(self):
        if self.sender() == self.superRc1Pr2_si:
            self.respuesta_Rc1Pr2 = "SI"
        elif self.sender() == self.superRc1Pr2_no:
            self.respuesta_Rc1Pr2 = "NO"
        print(f"ResgoCrit1Pregunta 2: {self.respuesta_Rc1Pr2}")

    def RiesgCrit1Pr3(self):
        if self.sender() == self.superRc1Pr3_si:
            self.respuesta_Rc1Pr3 = "SI"
        elif self.sender() == self.superRc1Pr3_no:
            self.respuesta_Rc1Pr3 = "NO"
        print(f"ResgoCrit1Pregunta 3: {self.respuesta_Rc1Pr3}")

    def RiesgCrit1Pr4(self):
        if self.sender() == self.superRc1Pr4_si:
            self.respuesta_Rc1Pr4 = "SI"
        elif self.sender() == self.superRc1Pr4_no:
            self.respuesta_Rc1Pr4 = "NO"
        print(f"ResgoCrit1Pregunta 4: {self.respuesta_Rc1Pr4}")

    def RiesgCrit1Pr5(self):
        if self.sender() == self.superRc1Pr5_si:
            self.respuesta_Rc1Pr5 = "SI"
        elif self.sender() == self.superRc1Pr5_no:
            self.respuesta_Rc1Pr5 = "NO"
        print(f"ResgoCrit1Pregunta 5: {self.respuesta_Rc1Pr5}")

    def RiesgCrit1Pr6(self):
        if self.sender() == self.superRc1Pr6_si:
            self.respuesta_Rc1Pr6 = "SI"
        elif self.sender() == self.superRc1Pr6_no:
            self.respuesta_Rc1Pr6 = "NO"
        print(f"ResgoCrit1Pregunta 6: {self.respuesta_Rc1Pr6}")

    def RiesgCrit1Pr7(self):
        if self.sender() == self.superRc1Pr7_si:
            self.respuesta_Rc1Pr7 = "SI"
        elif self.sender() == self.superRc1Pr7_no:
            self.respuesta_Rc1Pr7 = "NO"
        print(f"ResgoCrit1Pregunta 7: {self.respuesta_Rc1Pr7}")

    def RiesgCrit1Pr8(self):
        if self.sender() == self.superRc1Pr8_si:
            self.respuesta_Rc1Pr8 = "SI"
        elif self.sender() == self.superRc1Pr8_no:
            self.respuesta_Rc1Pr8 = "NO"
        print(f"ResgoCrit1Pregunta 8: {self.respuesta_Rc1Pr8}")


    def RiesgCrit2Pr1(self):
        if self.sender() == self.superRc2Pr1_si:
            self.respuesta_Rc2Pr1 = "SI"
        elif self.sender() == self.superRc2Pr1_no:
            self.respuesta_Rc2Pr1 = "NO"
        print(f"ResgoCrit2Pregunta 1: {self.respuesta_Rc2Pr1}")

    def RiesgCrit2Pr2(self):
        if self.sender() == self.superRc2Pr2_si:
            self.respuesta_Rc2Pr2 = "SI"
        elif self.sender() == self.superRc2Pr2_no:
            self.respuesta_Rc2Pr2 = "NO"
        print(f"ResgoCrit2Pregunta 2: {self.respuesta_Rc2Pr2}")

    def RiesgCrit2Pr3(self):
        if self.sender() == self.superRc2Pr3_si:
            self.respuesta_Rc2Pr3 = "SI"
        elif self.sender() == self.superRc2Pr3_no:
            self.respuesta_Rc2Pr3 = "NO"
        print(f"ResgoCrit2Pregunta 3: {self.respuesta_Rc2Pr3}")

    def RiesgCrit2Pr4(self):
        if self.sender() == self.superRc2Pr4_si:
            self.respuesta_Rc2Pr4 = "SI"
        elif self.sender() == self.superRc2Pr4_no:
            self.respuesta_Rc2Pr4 = "NO"
        print(f"ResgoCrit2Pregunta 4: {self.respuesta_Rc2Pr4}")

    def RiesgCrit2Pr5(self):
        if self.sender() == self.superRc2Pr5_si:
            self.respuesta_Rc2Pr5 = "SI"
        elif self.sender() == self.superRc2Pr5_no:
            self.respuesta_Rc2Pr5 = "NO"
        print(f"ResgoCrit2Pregunta 5: {self.respuesta_Rc2Pr5}")

    def RiesgCrit2Pr6(self):
        if self.sender() == self.superRc2Pr6_si:
            self.respuesta_Rc2Pr6 = "SI"
        elif self.sender() == self.superRc2Pr6_no:
            self.respuesta_Rc2Pr6 = "NO"
        print(f"ResgoCrit2Pregunta 6: {self.respuesta_Rc2Pr6}")

    def RiesgCrit2Pr7(self):
        if self.sender() == self.superRc2Pr7_si:
            self.respuesta_Rc2Pr7 = "SI"
        elif self.sender() == self.superRc2Pr7_no:
            self.respuesta_Rc2Pr7 = "NO"
        print(f"ResgoCrit2Pregunta 7: {self.respuesta_Rc2Pr7}")

    def RiesgCrit2Pr8(self):
        if self.sender() == self.superRc2Pr8_si:
            self.respuesta_Rc2Pr8 = "SI"
        elif self.sender() == self.superRc2Pr8_no:
            self.respuesta_Rc2Pr8 = "NO"
        print(f"ResgoCrit2Pregunta 8: {self.respuesta_Rc2Pr8}")

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

    def abrirCambioDatos(self):
        cambioDatos(self.rut, self.datos)
        self.hide()

    def procesarSeleccion(self, seleccion):
        if seleccion == "Lavado de material":
            return "Lavado de material"
        elif seleccion == "Lecturas en equipo de A.A":
            return "Lecturas en equipo de A.A"
        elif seleccion == "Masado de muestras":
            return "Masado de muestras"
        elif seleccion == "Digestión acida de muestras":
            return "Digestión acida de muestras"
        elif seleccion == "Lixiviaxión de muestras":
            return "Lixiviaxión de muestras"
        else:
            return "Selección desconocida"

    def decision(self):
        seleccion = self.ElegirArtSuper.currentText()
        self.resultado = self.procesarSeleccion(seleccion)
        riesgoCrit = self.contr.visualizarRiesgoActividad(self.resultado)
        if riesgoCrit == "Selección desconocida":
            return "seleccione una opcion"
        if riesgoCrit[1] == '6':
            self.RC1PR6.setVisible(False)
            self.RC1PR7.setVisible(False)
            self.RC1PR8.setVisible(False)
        if riesgoCrit[3] == '7':
            self.RC2PR8.setVisible(False)
        if riesgoCrit[3] != (''):
            self.frame_102.setVisible(True)
        if riesgoCrit[3] == (''):
            self.frame_102.setVisible(False)

        self.NombreActividad.setText(riesgoCrit[0])
        self.superNombreRc1.setText(riesgoCrit[2])
        self.superNombreRc2.setText(riesgoCrit[4])
        self.superCodRc1.setText(riesgoCrit[1])
        self.superCodRc2.setText(riesgoCrit[3])

    def mostrarTablaTrabajadores(self):
        trabajadores = self.contr.mostrarTrabajadores()
        print(trabajadores)
        self.trabajadores.setRowCount(0)
        self.trabajadores.setRowCount(len(trabajadores))
        for i, trabajador in enumerate(trabajadores):
            self.trabajadores.setItem(i, 0, QTableWidgetItem(trabajador[0]))  # nombre_completo
            self.trabajadores.setItem(i, 1, QTableWidgetItem(trabajador[1]))  # rut
            self.trabajadores.setItem(i, 2, QTableWidgetItem(trabajador[2]))  # correo
            self.trabajadores.setItem(i, 3, QTableWidgetItem(trabajador[3]))  # especialidad

    def mostrarTablaART(self):
        Arts = self.contr.mostrarARTCreadas()
        print(Arts)
        self.verARTS.setRowCount(0)
        self.verARTS.setRowCount(len(Arts))
        for i, trabajador in enumerate(Arts):
            self.verARTS.setItem(i, 0, QTableWidgetItem(trabajador[0]))  # nombre_completo
            self.verARTS.setItem(i, 1, QTableWidgetItem(trabajador[1]))  # rut
            self.verARTS.setItem(i, 2, QTableWidgetItem(trabajador[2]))  # actividad
            self.verARTS.setItem(i, 3, QTableWidgetItem(trabajador[3]))  # fecha
            self.verARTS.setItem(i, 4, QTableWidgetItem(trabajador[4]))  # hora_inicio
            self.verARTS.setItem(i, 5, QTableWidgetItem(trabajador[5]))  # hora_termino

    def mostrarTablaArtActividad(self):
        artActividad = self.contr.mostrarARTporActividad(self.resultado)
        print(artActividad)
        self.verLlenarART.setRowCount(0)
        self.verLlenarART.setRowCount(len(artActividad))
        for i, trabajador in enumerate(artActividad):
            self.verLlenarART.setItem(i, 0, QTableWidgetItem(trabajador[0]))  # nombre_completo
            self.verLlenarART.setItem(i, 1, QTableWidgetItem(trabajador[1]))  # actividad
            self.verLlenarART.setItem(i, 2, QTableWidgetItem(trabajador[2]))  # trabajo_simultaneo
            self.verLlenarART.setItem(i, 3, QTableWidgetItem(trabajador[3]))  # estado_trabajador

    def EndSuperART(self):
        self.respuestasPS.append(self.respuesta_PS1)
        self.respuestasPS.append(self.respuesta_PS2)
        self.respuestasPS.append(self.respuesta_PS3)
        self.respuestasPS.append(self.respuesta_PS4)
        self.respuestasPS.append(self.respuesta_PS5)
        self.respuestasPS.append(self.respuesta_PS6)
        self.respuestasRc1.append(self.respuesta_Rc1Pr1)
        self.respuestasRc1.append(self.respuesta_Rc1Pr2)
        self.respuestasRc1.append(self.respuesta_Rc1Pr3)
        self.respuestasRc1.append(self.respuesta_Rc1Pr4)
        self.respuestasRc1.append(self.respuesta_Rc1Pr5)
        self.respuestasRc1.append(self.respuesta_Rc1Pr6)
        self.respuestasRc1.append(self.respuesta_Rc1Pr7)
        self.respuestasRc1.append(self.respuesta_Rc1Pr8)
        self.respuestasRc2.append(self.respuesta_Rc2Pr1)
        self.respuestasRc2.append(self.respuesta_Rc2Pr2)
        self.respuestasRc2.append(self.respuesta_Rc2Pr3)
        self.respuestasRc2.append(self.respuesta_Rc2Pr4)
        self.respuestasRc2.append(self.respuesta_Rc2Pr5)
        self.respuestasRc2.append(self.respuesta_Rc2Pr6)
        self.respuestasRc2.append(self.respuesta_Rc2Pr7)
        self.respuestasRc2.append(self.respuesta_Rc2Pr8)
        print(self.respuestasSt)
        print(self.respuestasRc1)
        print(self.respuestasRc2)