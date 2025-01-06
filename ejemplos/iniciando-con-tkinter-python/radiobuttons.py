from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Botones radiales PyQt")
window.setGeometry(100, 100, 230, 80)
layout = QVBoxLayout()
window.setLayout(layout)
layout.addWidget(QLabel("¿Qué prefieres?"))

foods = ["Pizza", "Hamburguesa", "Pasta", "Pollo asado"]
for food in foods:
    radio = QRadioButton(food)
    layout.addWidget(radio)

window.show()
app.exec()
