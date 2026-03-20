import zipfile

with zipfile.ZipFile(
    "archivo.zip", mode="w", compression=zipfile.ZIP_DEFLATED
) as zip_file:
    zip_file.write("archivo_0.txt")
    zip_file.write("archivo_1.txt")
