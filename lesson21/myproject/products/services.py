def apply_discount(product, percent):
    """
    Aplică reducere procentuală la un produs și salvează modificarea
    """
    product.price -= product.price * percent / 100
    product.save()
