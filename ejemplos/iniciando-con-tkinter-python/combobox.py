from PyQt6.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle("Lista desplegable PyQt")
window.setGeometry(100, 100, 250, 50)
layout = QVBoxLayout()
window.setLayout(layout)

combo = QComboBox(parent=window)
combo.addItems(["PyQt", "PySide", "Kivy", "Tkinter", "wxPython"])
layout.addWidget(combo)

window.show()
app.exec()
