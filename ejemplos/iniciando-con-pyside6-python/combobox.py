from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QVBoxLayout,
    QWidget,
)

app = QApplication([])

window = QWidget()
window.setWindowTitle("Lista desplegable PySide6")
window.setGeometry(100, 100, 250, 50)
layout = QVBoxLayout()
window.setLayout(layout)

combo = QComboBox(parent=window)
combo.addItems(["PySide6", "PyQt", "Kivy", "Tkinter", "wxPython"])
layout.addWidget(combo)

window.show()
app.exec()
