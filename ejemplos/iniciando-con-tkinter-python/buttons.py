from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle("Botones PyQt")
window.setGeometry(100, 100, 180, 50)
layout = QVBoxLayout()
window.setLayout(layout)

for text in ["Ok", "Cancelar", "Aplicar", "Sí", "No", "Cerrar"]:
    button = QPushButton(text, parent=window)
    layout.addWidget(button)

window.show()
app.exec()
