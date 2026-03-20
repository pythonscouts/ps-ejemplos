from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Disposición Horizontal")

layout = QHBoxLayout()
window.setLayout(layout)

positions = ["Izquierda", "Centro", "Derecha"]
for position in positions:
    button = QPushButton(position)
    layout.addWidget(button)

window.show()
app.exec()
