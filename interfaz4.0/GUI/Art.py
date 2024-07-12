from PyQt6.QtWidgets import QMainWindow
from GUI.ui_ART import Ui_MainWindow
from PyQt6 import QtCore, QtWidgets

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt, QPointF

class ART(QMainWindow, Ui_MainWindow):
    def __init__(self,datos, riesgoCrit,controlRiesgo):
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
        self.NombreActividad.setText(riesgoCrit[0])
        self.nombreRiesgo1.setText(riesgoCrit[2])
        self.nombreRiesgo2.setText(riesgoCrit[4])
        self.NumCod1.setText(riesgoCrit[1])
        self.NumCod2.setText(riesgoCrit[3])
        self.mostrarOtroRiesgo.setText(controlRiesgo[0])
        self.mostrarMedidasControl.setText(controlRiesgo[1])
        self.CargoTrab.setText("")
        self.nombreTrab.setText(datos[0])
        self.show()
        
        self.respuesta_PT1 = None
        self.respuesta_PT2 = None
        self.respuesta_PT3 = None
        self.respuesta_PT4 = None
        self.respuesta_PT5 = None
        self.respuesta_PT6 = None

        self.respuesta_Rc1Pr1 = None
        self.respuesta_Rc1Pr2 = None
        self.respuesta_Rc1Pr3 = None
        self.respuesta_Rc1Pr4 = None
        self.respuesta_Rc1Pr5 = None
        self.respuesta_Rc1Pr6 = None
        self.respuesta_Rc1Pr5 = None
        self.respuesta_Rc1Pr6 = None

        self.respuesta_Rc2Pr1 = None
        self.respuesta_Rc2Pr2 = None
        self.respuesta_Rc2Pr3 = None
        self.respuesta_Rc2Pr4 = None
        self.respuesta_Rc2Pr5 = None
        self.respuesta_Rc2Pr6 = None
        self.respuesta_Rc2Pr5 = None
        self.respuesta_Rc2Pr6 = None

        self.respuesta_trabSimult = None
        self.respuesta_CoordLider = None
        self.respuesta_VerifCCritic = None
        self.respuesta_TSVerificado = None
        self.respuesta_confirCondicion = None

        self.PT1_si.clicked.connect(self.pregunta1)
        self.PT1_no.clicked.connect(self.pregunta1)
        self.PT2_si.clicked.connect(self.pregunta2)
        self.PT2_no.clicked.connect(self.pregunta2)
        self.PT3_si.clicked.connect(self.pregunta3)
        self.PT3_no.clicked.connect(self.pregunta3)
        self.PT4_si.clicked.connect(self.pregunta4)
        self.PT4_no.clicked.connect(self.pregunta4)
        self.PT5_si.clicked.connect(self.pregunta5)
        self.PT5_no.clicked.connect(self.pregunta5)
        self.PT6_si.clicked.connect(self.pregunta6)
        self.PT6_no.clicked.connect(self.pregunta6)

        self.Rc1Pr1_si.clicked.connect(self.RiesgCrit1Pr1)
        self.Rc1Pr1_no.clicked.connect(self.RiesgCrit1Pr1)
        self.Rc1Pr2_si.clicked.connect(self.RiesgCrit1Pr2)
        self.Rc1Pr2_no.clicked.connect(self.RiesgCrit1Pr2)
        self.Rc1Pr3_si.clicked.connect(self.RiesgCrit1Pr3)
        self.Rc1Pr3_no.clicked.connect(self.RiesgCrit1Pr3)
        self.Rc1Pr4_si.clicked.connect(self.RiesgCrit1Pr4)
        self.Rc1Pr4_no.clicked.connect(self.RiesgCrit1Pr4)
        self.Rc1Pr5_si.clicked.connect(self.RiesgCrit1Pr5)
        self.Rc1Pr5_no.clicked.connect(self.RiesgCrit1Pr5)
        self.Rc1Pr6_si.clicked.connect(self.RiesgCrit1Pr6)
        self.Rc1Pr6_no.clicked.connect(self.RiesgCrit1Pr6)
        self.Rc1Pr7_si.clicked.connect(self.RiesgCrit1Pr7)
        self.Rc1Pr7_no.clicked.connect(self.RiesgCrit1Pr7)
        self.Rc1Pr8_si.clicked.connect(self.RiesgCrit1Pr8)
        self.Rc1Pr8_no.clicked.connect(self.RiesgCrit1Pr8)

        self.Rc2Pr1_si.clicked.connect(self.RiesgCrit2Pr1)
        self.Rc2Pr1_no.clicked.connect(self.RiesgCrit2Pr1)
        self.Rc2Pr2_si.clicked.connect(self.RiesgCrit2Pr2)
        self.Rc2Pr2_no.clicked.connect(self.RiesgCrit2Pr2)
        self.Rc2Pr3_si.clicked.connect(self.RiesgCrit2Pr3)
        self.Rc2Pr3_no.clicked.connect(self.RiesgCrit2Pr3)
        self.Rc2Pr4_si.clicked.connect(self.RiesgCrit2Pr4)
        self.Rc2Pr4_no.clicked.connect(self.RiesgCrit2Pr4)
        self.Rc2Pr5_si.clicked.connect(self.RiesgCrit2Pr5)
        self.Rc2Pr5_no.clicked.connect(self.RiesgCrit2Pr5)
        self.Rc2Pr6_si.clicked.connect(self.RiesgCrit2Pr6)
        self.Rc2Pr6_no.clicked.connect(self.RiesgCrit2Pr6)
        self.Rc2Pr7_si.clicked.connect(self.RiesgCrit2Pr7)
        self.Rc2Pr7_no.clicked.connect(self.RiesgCrit2Pr7)
        self.Rc2Pr8_si.clicked.connect(self.RiesgCrit2Pr8)
        self.Rc2Pr8_no.clicked.connect(self.RiesgCrit2Pr8)

        self.trabSimult_si.clicked.connect(self.trabSimultaneo)
        self.trabSimult_no.clicked.connect(self.trabSimultaneo)

        self.CoordLider_si.clicked.connect(self.coordinLider)
        self.CoordLider_no.clicked.connect(self.coordinLider)

        self.VerifCCritic_si.clicked.connect(self.verifCCr)
        self.VerifCCritic_no.clicked.connect(self.verifCCr)        

        self.TSVerificado_si.clicked.connect(self.verifTrab)
        self.TSVerificado_no.clicked.connect(self.verifTrab)

        self.confirCondicion_si.clicked.connect(self.condicionFisica)
        self.confirCondicion_no.clicked.connect(self.condicionFisica)


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

    def pregunta1(self):
        if self.sender() == self.PT1_si:
            self.respuesta_PT1 = "SI"
        elif self.sender() == self.PT1_no:
            self.respuesta_PT1 = "NO"
        print(f"Pregunta 1: {self.respuesta_PT1}")

    def pregunta2(self):
        if self.sender() == self.PT2_si:
            self.respuesta_PT2 = "SI"
        elif self.sender() == self.PT2_no:
            self.respuesta_PT2 = "NO"
        print(f"Pregunta 2: {self.respuesta_PT2}")

    def pregunta3(self):
        if self.sender() == self.PT3_si:
            self.respuesta_PT3 = "SI"
        elif self.sender() == self.PT3_no:
            self.respuesta_PT3 = "NO"
        print(f"Pregunta 3: {self.respuesta_PT3}")

    def pregunta4(self):
        if self.sender() == self.PT4_si:
            self.respuesta_PT4 = "SI"
        elif self.sender() == self.PT4_no:
            self.respuesta_PT4 = "NO"
        print(f"Pregunta 4: {self.respuesta_PT4}")

    def pregunta5(self):
        if self.sender() == self.PT5_si:
            self.respuesta_PT5 = "SI"
        elif self.sender() == self.PT5_no:
            self.respuesta_PT5 = "NO"
        print(f"Pregunta 5: {self.respuesta_PT5}")

    def pregunta6(self):
        if self.sender() == self.PT6_si:
            self.respuesta_PT6 = "SI"
        elif self.sender() == self.PT6_no:
            self.respuesta_PT6 = "NO"
        print(f"Pregunta 6: {self.respuesta_PT6}")


    def RiesgCrit1Pr1(self):
        if self.sender() == self.Rc1Pr1_si:
            self.respuesta_Rc1Pr1 = "SI"
        elif self.sender() == self.Rc1Pr1_no:
            self.respuesta_Rc1Pr1 = "NO"
        print(f"ResgoCrit1Pregunta 1: {self.respuesta_Rc1Pr1}")

    def RiesgCrit1Pr2(self):
        if self.sender() == self.Rc1Pr2_si:
            self.respuesta_Rc1Pr2 = "SI"
        elif self.sender() == self.Rc1Pr2_no:
            self.respuesta_Rc1Pr2 = "NO"
        print(f"ResgoCrit1Pregunta 2: {self.respuesta_Rc1Pr2}")

    def RiesgCrit1Pr3(self):
        if self.sender() == self.Rc1Pr3_si:
            self.respuesta_Rc1Pr3 = "SI"
        elif self.sender() == self.Rc1Pr3_no:
            self.respuesta_Rc1Pr3 = "NO"
        print(f"ResgoCrit1Pregunta 3: {self.respuesta_Rc1Pr3}")

    def RiesgCrit1Pr4(self):
        if self.sender() == self.Rc1Pr4_si:
            self.respuesta_Rc1Pr4 = "SI"
        elif self.sender() == self.Rc1Pr4_no:
            self.respuesta_Rc1Pr4 = "NO"
        print(f"ResgoCrit1Pregunta 4: {self.respuesta_Rc1Pr4}")

    def RiesgCrit1Pr5(self):
        if self.sender() == self.Rc1Pr5_si:
            self.respuesta_Rc1Pr5 = "SI"
        elif self.sender() == self.Rc1Pr5_no:
            self.respuesta_Rc1Pr5 = "NO"
        print(f"ResgoCrit1Pregunta 5: {self.respuesta_Rc1Pr5}")

    def RiesgCrit1Pr6(self):
        if self.sender() == self.Rc1Pr6_si:
            self.respuesta_Rc1Pr6 = "SI"
        elif self.sender() == self.Rc1Pr6_no:
            self.respuesta_Rc1Pr6 = "NO"
        print(f"ResgoCrit1Pregunta 6: {self.respuesta_Rc1Pr6}")

    def RiesgCrit1Pr7(self):
        if self.sender() == self.Rc1Pr7_si:
            self.respuesta_Rc1Pr7 = "SI"
        elif self.sender() == self.Rc1Pr7_no:
            self.respuesta_Rc1Pr7 = "NO"
        print(f"ResgoCrit1Pregunta 7: {self.respuesta_Rc1Pr7}")

    def RiesgCrit1Pr8(self):
        if self.sender() == self.Rc1Pr8_si:
            self.respuesta_Rc1Pr8 = "SI"
        elif self.sender() == self.Rc1Pr8_no:
            self.respuesta_Rc1Pr8 = "NO"
        print(f"ResgoCrit1Pregunta 8: {self.respuesta_Rc1Pr8}")



    def RiesgCrit2Pr1(self):
        if self.sender() == self.Rc2Pr1_si:
            self.respuesta_Rc2Pr1 = "SI"
        elif self.sender() == self.Rc2Pr1_no:
            self.respuesta_Rc2Pr1 = "NO"
        print(f"ResgoCrit2Pregunta 1: {self.respuesta_Rc2Pr1}")

    def RiesgCrit2Pr2(self):
        if self.sender() == self.Rc2Pr2_si:
            self.respuesta_Rc2Pr2 = "SI"
        elif self.sender() == self.Rc2Pr2_no:
            self.respuesta_Rc2Pr2 = "NO"
        print(f"ResgoCrit2Pregunta 2: {self.respuesta_Rc2Pr2}")

    def RiesgCrit2Pr3(self):
        if self.sender() == self.Rc2Pr3_si:
            self.respuesta_Rc2Pr3 = "SI"
        elif self.sender() == self.Rc2Pr3_no:
            self.respuesta_Rc2Pr3 = "NO"
        print(f"ResgoCrit2Pregunta 3: {self.respuesta_Rc2Pr3}")

    def RiesgCrit2Pr4(self):
        if self.sender() == self.Rc2Pr4_si:
            self.respuesta_Rc2Pr4 = "SI"
        elif self.sender() == self.Rc2Pr4_no:
            self.respuesta_Rc2Pr4 = "NO"
        print(f"ResgoCrit2Pregunta 4: {self.respuesta_Rc2Pr4}")

    def RiesgCrit2Pr5(self):
        if self.sender() == self.Rc2Pr5_si:
            self.respuesta_Rc2Pr5 = "SI"
        elif self.sender() == self.Rc2Pr5_no:
            self.respuesta_Rc2Pr5 = "NO"
        print(f"ResgoCrit2Pregunta 5: {self.respuesta_Rc2Pr5}")

    def RiesgCrit2Pr6(self):
        if self.sender() == self.Rc2Pr6_si:
            self.respuesta_Rc2Pr6 = "SI"
        elif self.sender() == self.Rc2Pr6_no:
            self.respuesta_Rc2Pr6 = "NO"
        print(f"ResgoCrit2Pregunta 6: {self.respuesta_Rc2Pr6}")

    def RiesgCrit2Pr7(self):
        if self.sender() == self.Rc2Pr7_si:
            self.respuesta_Rc2Pr7 = "SI"
        elif self.sender() == self.Rc2Pr7_no:
            self.respuesta_Rc2Pr7 = "NO"
        print(f"ResgoCrit2Pregunta 7: {self.respuesta_Rc2Pr7}")

    def RiesgCrit2Pr8(self):
        if self.sender() == self.Rc2Pr8_si:
            self.respuesta_Rc2Pr8 = "SI"
        elif self.sender() == self.Rc2Pr8_no:
            self.respuesta_Rc2Pr8 = "NO"
        print(f"ResgoCrit2Pregunta 8: {self.respuesta_Rc2Pr8}")


    def trabSimultaneo(self):
        if self.sender() == self.trabSimult_si:
            self.respuesta_trabSimult = "SI"
        elif self.sender() == self.trabSimult_no:
            self.respuesta_trabSimult = "NO"
        print(f"respuesta_trabSimult: {self.respuesta_trabSimult}")

    def coordinLider(self):
        if self.sender() == self.CoordLider_si:
            self.respuesta_CoordLider = "SI"
        elif self.sender() == self.CoordLider_no:
            self.respuesta_CoordLider = "NO"
        print(f"respuesta_CoordLider: {self.respuesta_CoordLider}")

    def verifCCr(self):
        if self.sender() == self.VerifCCritic_si:
            self.respuesta_VerifCCritic = "SI"
        elif self.sender() == self.VerifCCritic_no:
            self.respuesta_VerifCCritic = "NO"
        print(f"respuesta_VerifCCritic: {self.respuesta_VerifCCritic}")
        
    def verifTrab(self):
        if self.sender() == self.TSVerificado_si:
            self.respuesta_TSVerificado = "SI"
        elif self.sender() == self.TSVerificado_no:
            self.respuesta_TSVerificado = "NO"
        print(f"respuesta_TSVerificado: {self.respuesta_TSVerificado}")

    def condicionFisica(self):
        if self.sender() == self.confirCondicion_si:
            self.respuesta_confirCondicion = "SI"
        elif self.sender() == self.confirCondicion_no:
            self.respuesta_confirCondicion = "NO"
        print(f"respuesta_confirCondicion: {self.respuesta_confirCondicion}")


if __name__ == "__main__":
        app = QApplication([])
        window = ART()
        window.show()
        app.exec()
