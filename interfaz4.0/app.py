from PyQt6.QtWidgets import QApplication
from GUI.iniSecion import Login


class wss():
    if __name__ == "__main__":
        app = QApplication([])
        window = Login()
        window.show()
        app.exec()