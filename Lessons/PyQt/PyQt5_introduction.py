import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI") # Define el título de la ventana
        self.setGeometry(700, 300, 400, 300) # Los dos números indican que la ventana se abra en
        # en un lugar concreto de la pantalla, los otros dos datos son el tamaño de la ventana
        self.setWindowIcon(QIcon(""))
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()