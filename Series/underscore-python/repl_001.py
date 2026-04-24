def check_service_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "No encontrado"
        case _:
            return "Cualquier otro estado"


print(check_service_status(200))
print(check_service_status(404))
print(check_service_status(500))
