# ---- Funciones provistas (NO modificar) ----

def apply_discount(price, discount_pct):
    """Dado un precio y un porcentaje de descuento, retorna el precio con el descuento aplicado."""
    return price * (1 - discount_pct / 100)

def apply_tax(price, tax_pct):
    """Dado un precio y un porcentaje de impuesto, retorna el precio con el impuesto aplicado."""
    return price * (1 + tax_pct / 100)

# ---- Funciones a implementar ----

def final_price(price, quantity, discount_pct, tax_pct):
    subtotal = price * quantity
    with_discount = apply_discount(subtotal, discount_pct)
    with_tax = apply_tax(with_discount, tax_pct)
    return round(with_tax, 2)


def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):
    final_a = final_price(price_a, qty_a, disc_a, tax_pct)
    final_b = final_price(price_b, qty_b, disc_b, tax_pct)

    if final_a <= final_b:
        return "A"
    else:
        return "B"