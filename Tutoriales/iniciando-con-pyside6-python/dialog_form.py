from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)


class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QDialog")

        layout = QVBoxLayout()
        self.setLayout(layout)

        form_layout = QFormLayout()
        labels = ["Nombre:", "Edad:", "Ocupación:", "Dirección:"]
        for label in labels:
            form_layout.addRow(label, QLineEdit())

        layout.addLayout(form_layout)
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok
        )
        layout.addWidget(buttons)


app = QApplication([])
window = Window()
window.show()
app.exec()
