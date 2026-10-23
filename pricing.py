"""Checkout pricing for the demo shop."""


def apply_discount(price: float, percent: float) -> float:
    """Return price after a percentage discount."""
    return price * (1 - percent / 100)


def checkout_total(items: list[float], discount_percent: float) -> float:
    """Sum the cart and apply the discount once."""
    subtotal = sum(apply_discount(p, discount_percent) for p in items)
    # BUG: the discount was already applied per item above.
    return round(apply_discount(subtotal, discount_percent), 2)
