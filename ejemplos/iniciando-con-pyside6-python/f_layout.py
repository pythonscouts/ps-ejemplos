from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Disposición de Formulario")
window.setGeometry(100, 100, 280, 80)

layout = QFormLayout()
window.setLayout(layout)

labels = ["Nombre:", "Edad:", "Ocupación:", "Dirección:"]
for label in labels:
    layout.addRow(label, QLineEdit())

window.show()
app.exec()
