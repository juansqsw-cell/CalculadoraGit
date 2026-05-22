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

def potencia(base, exponente):
    return base ** exponente

print("Suma:", suma(3, 5))
print("Resta:", resta(10, 4))
print("Multiplicacion:", multiplicacion(3, 7))
print("Division:", division(10, 2))
print("Potencia:", potencia(2, 8))
