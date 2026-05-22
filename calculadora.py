def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

print("Prueba suma:", suma(3, 5))
print("Prueba resta:", resta(10, 4))
print("Prueba multiplicacion:", multiplicacion(3, 7))
print("Prueba division:", division(10, 2))
