from PyQt6.QtWidgets import (
    QApplication,
    QColorDialog,
    QFileDialog,
    QFontDialog,
    QInputDialog,
    QMessageBox,
)

app = QApplication([])

QMessageBox.information(
    None,
    "Información",
    "Este es un mensaje.",
)

# Abrir un archivo
file_path, _ = QFileDialog.getOpenFileName(None, "Abrir Archivo")
if file_path:
    QMessageBox.information(
        None,
        "Archivo Seleccionado",
        f"Seleccionaste: {file_path}",
    )

# Seleccionar un color
color = QColorDialog.getColor()
if color.isValid():
    QMessageBox.information(
        None, "Color Seleccionado", f"Seleccionaste: {color.name()}"
    )

# Seleccionar una fuente
font, ok = QFontDialog.getFont()
if ok:
    QMessageBox.information(
        None, "Fuente Seleccionada", f"Seleccionaste: {font.family()}"
    )

# Entrada de texto
text, ok = QInputDialog.getText(None, "Entrada de Texto", "Escribe algo:")
if ok and text:
    QMessageBox.information(None, "Texto Ingresado", f"Escribiste: {text}")

app.exec()
