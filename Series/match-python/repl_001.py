def process_command(command):
    match command:
        case "start":
            return "Iniciando..."
        case "stop":
            return "Deteniendo..."
        case _:
            return "Comando desconocido"


print(process_command("start"))
print(process_command("stop"))
