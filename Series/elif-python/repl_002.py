status_code = 404
if 100 <= status_code < 200:
    print("Respuesta informativa")
elif 200 <= status_code < 300:
    print("Respuesta exitosa")
elif 300 <= status_code < 400:
    print("Redirección")
elif 400 <= status_code < 500:
    print("Error del cliente")
elif 500 <= status_code < 600:
    print("Error del servidor")
else:
    print("Código desconocido")
