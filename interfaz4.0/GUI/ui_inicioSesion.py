# Form implementation generated from reading ui file 'inicioSesion.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import os
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        image_logo = os.path.join(sys._MEIPASS, "images/logo.png")
        icon_Cerrar = os.path.join(sys._MEIPASS, "images/x.svg")
        icon_minimizar = os.path.join(sys._MEIPASS, "images/minimizar-ventana.svg")
        icon_expandir = os.path.join(sys._MEIPASS, "images/expandir.svg")
        icon_comprimir = os.path.join(sys._MEIPASS, "images/comprimir.svg")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 684)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(parent=self.frame)
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_superior.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame_superior)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_minimize = QtWidgets.QPushButton(parent=self.frame_superior)
        self.bt_minimize.setMinimumSize(QtCore.QSize(0, 20))
        self.bt_minimize.setMouseTracking(False)
        self.bt_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_minimizar), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_minimize.setIcon(icon)
        self.bt_minimize.setObjectName("bt_minimize")
        self.horizontalLayout.addWidget(self.bt_minimize)
        self.bt_maximize = QtWidgets.QPushButton(parent=self.frame_superior)
        self.bt_maximize.setMinimumSize(QtCore.QSize(0, 20))
        self.bt_maximize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(icon_expandir), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_maximize.setIcon(icon1)
        self.bt_maximize.setObjectName("bt_maximize")
        self.horizontalLayout.addWidget(self.bt_maximize)
        self.bt_normal = QtWidgets.QPushButton(parent=self.frame_superior)
        self.bt_normal.setMinimumSize(QtCore.QSize(0, 20))
        self.bt_normal.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(icon_comprimir), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_normal.setIcon(icon2)
        self.bt_normal.setObjectName("bt_normal")
        self.horizontalLayout.addWidget(self.bt_normal)
        self.bt_close = QtWidgets.QPushButton(parent=self.frame_superior)
        self.bt_close.setMinimumSize(QtCore.QSize(0, 20))
        self.bt_close.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(icon_Cerrar), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_close.setIcon(icon3)
        self.bt_close.setObjectName("bt_close")
        self.horizontalLayout.addWidget(self.bt_close)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(212, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_4.setMinimumSize(QtCore.QSize(400, 500))
        self.frame_4.setMaximumSize(QtCore.QSize(500, 500))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(148, 148, 148);\n"
"color:rgb(247, 247, 247);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(image_logo))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.rutUser = QtWidgets.QLineEdit(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rutUser.setFont(font)
        self.rutUser.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(148,148,148);\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.rutUser.setObjectName("rutUser")
        self.verticalLayout_3.addWidget(self.rutUser)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.contraUser = QtWidgets.QLineEdit(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.contraUser.setFont(font)
        self.contraUser.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(148,148,148);\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.contraUser.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.contraUser.setObjectName("contraUser")
        self.verticalLayout_3.addWidget(self.contraUser)
        self.checkBox = QtWidgets.QCheckBox(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.iniciarSesion = QtWidgets.QPushButton(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.iniciarSesion.setFont(font)
        self.iniciarSesion.setStyleSheet("QPushButton {\n"
"border-radius: 8px;\n"
"border: 2px solid rgb(148,148,148);\n"
"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.iniciarSesion.setObjectName("iniciarSesion")
        self.verticalLayout_3.addWidget(self.iniciarSesion)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.lblmss = QtWidgets.QLabel(parent=self.frame_4)
        self.lblmss.setText("")
        self.lblmss.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblmss.setObjectName("lblmss")
        self.verticalLayout_3.addWidget(self.lblmss)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_5.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(148, 148, 148);\n"
"color:rgb(247, 247, 247);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.cambio = QtWidgets.QPushButton(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.cambio.setFont(font)
        self.cambio.setStyleSheet("QPushButton {\n"
"border-radius: 8px;\n"
"border: 2px solid rgb(148,148,148);\n"
"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.cambio.setObjectName("cambio")
        self.verticalLayout_3.addWidget(self.cambio)
        self.verticalLayout_4.addWidget(self.frame_4)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem10 = QtWidgets.QSpacerItem(211, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Inicio sesion"))
        self.label_2.setText(_translate("MainWindow", "Inicia Sesion"))
        self.label_3.setText(_translate("MainWindow", "Rut:"))
        self.label_4.setText(_translate("MainWindow", "Contraseña:"))
        self.checkBox.setText(_translate("MainWindow", "Monstrar contraseña"))
        self.iniciarSesion.setText(_translate("MainWindow", "Iniciar Sesion"))
        self.label_5.setText(_translate("MainWindow", "¿Olvidaste la contraseña?"))
        self.cambio.setText(_translate("MainWindow", "Cambio de contraseña"))
