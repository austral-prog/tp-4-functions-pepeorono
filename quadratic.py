# Replace the "ANSWER HERE" for your answer
import math

def roots(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        r1 = (-b + math.sqrt(delta)) / (2*a)
        r2 = (-b - math.sqrt(delta)) / (2*a)
        return f"({r1}, {r2})"

    elif delta == 0:
        r = (-b) / (2*a)
        return f"({r})"

    else:
        return "( )"

def value_y(a, b, c, x):
    return a*x**2 + b*x + c

def to_string(a, b, c):
    if a == 0:
        if b == 0:
            return f"f(x) = {c}"
        return f"f(x) = {b} * X + {c}"

    if b == 0:
        return f"f(x) = {a} * X^2 + {c}"

    return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    if a == 0:
        return f"f'(x) = {b}"

    if b == 0:
        return f"f'(x) = {2 * a} * X"

    return f"f'(x) = {2 * a} * X + {b}"

print(roots(1, -3, 2))
print(roots(1, -2, 1))
print(roots(1, 2, 3))
print(value_y(1, -3, 2, 0))
print(value_y(1, -3, 2, 1))
print(value_y(1, -3, 2, -1))
print(to_string(2, -3, 1))
print(derivation(2, -3, 1))