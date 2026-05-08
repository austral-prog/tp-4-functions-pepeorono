# ---- Funciones provistas (NO modificar) ----
from traceback import print_tb


def is_even(n):
    """Dado un número entero n, retorna True si es par, False si es impar."""
    return n % 2 == 0

def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    return n > 0

# ---- Función a implementar ----

def classify_number(n):
    """
    Dado un número entero n, retorna un string que lo clasifica.
    Debe USAR las funciones is_even e is_positive para resolver el ejercicio.

    Clasificaciones posibles:
      - "positive even"   (positivo y par)
      - "positive odd"    (positivo e impar)
      - "negative even"   (negativo y par)
      - "negative odd"    (negativo e impar)
      - "zero"            (el número es 0)
    """
    if n==0:
        return "zero"

    if is_positive(n):
        if is_even(n):
            return "positive even"
        else:
            return "positive odd"

    else:
        if is_even(n):
            return "negative even"
        else:
            return "negative odd"

print(classify_number(4))
print(classify_number(3))
print(classify_number(-2))
print(classify_number(-1))
print(classify_number(0))