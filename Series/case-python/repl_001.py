def classify_age(age):
    match age:
        case n if n < 13:
            return "Eres un niño"
        case n if n < 20:
            return "Eres un adolescente"
        case _:
            return "Eres un adulto"


print(classify_age(10))
print(classify_age(15))
print(classify_age(30))
