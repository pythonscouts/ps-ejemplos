from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Disposición Vertical")
window.setGeometry(100, 100, 230, 80)

layout = QVBoxLayout()
window.setLayout(layout)

positions = ["Arriba", "Centro", "Abajo"]
for position in positions:
    button = QPushButton(position)
    layout.addWidget(button)

window.show()
app.exec()
