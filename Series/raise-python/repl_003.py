try:
    int("abc")
except ValueError as original_error:
    raise RuntimeError("error al convertir a entero") from original_error
