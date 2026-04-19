# ---- Funciones provistas (NO modificar) ----

def is_even(n):
    """Dado un número entero n, retorna True si es par, False si es impar."""
    return n % 2 == 0

def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    return n > 0

# ---- Función a implementar ----

def classify_number(n):
    if n == 0:
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