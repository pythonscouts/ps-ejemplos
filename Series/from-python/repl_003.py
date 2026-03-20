def connect_to_database(connection_string):
    try:
        # Código de conexión
        raise ConnectionError("no se pudo conectar al servidor")
    except ConnectionError as error:
        raise RuntimeError("error en la base de datos") from error


print(connect_to_database("localhost:5432"))
