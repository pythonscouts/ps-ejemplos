from PySide6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle("PySide6 Demo")
window.setGeometry(100, 100, 280, 80)
hello = QLabel("<h1>Hola, Mundo!</h1>", parent=window)
hello.move(60, 15)

window.show()
app.exec()
