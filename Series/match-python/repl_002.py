def process_http_status(status):
    match status:
        case 200 | 201 | 204:
            return "Éxito"
        case 400 | 401 | 404:
            return "Error del cliente"
        case 500 | 503:
            return "Error del servidor"
        case _:
            return "Otro código"


print(process_http_status(200))
print(process_http_status(404))
