from PySide6.QtWidgets import (
    QApplication,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

app = QApplication([])

window = QWidget()
window.setWindowTitle("Campos de texto PySide6")
window.setGeometry(100, 100, 250, 50)
layout = QVBoxLayout()
window.setLayout(layout)

for text in ["Nombre", "Usuario", "Contraseña"]:
    edit = QLineEdit(parent=window)
    edit.setPlaceholderText(text)
    layout.addWidget(edit)

window.show()
app.exec()
