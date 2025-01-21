from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Disposición en Cuadrícula")

layout = QGridLayout()
window.setLayout(layout)

button_names = [
    "Botón (0, 0)",
    "Botón (0, 1)",
    "Botón (0, 2)",
    "Botón (1, 0)",
    "Botón (1, 1)",
    "Botón (1, 2)",
    "Botón (2, 0)",
]
for i, name in enumerate(button_names):
    button = QPushButton(name)
    layout.addWidget(button, i // 3, i % 3)

layout.addWidget(
    QPushButton("Botón (2, 1) + 2 Columnas de Amplitud"),
    2,
    1,
    1,
    2,
)

window.show()
app.exec()
