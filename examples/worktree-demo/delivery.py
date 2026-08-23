from decimal import Decimal


FREE_DELIVERY_THRESHOLD = Decimal("50.00")
STANDARD_DELIVERY_FEE = Decimal("4.99")


def calculate_delivery_fee(
    order_total: Decimal,
    is_priority_member: bool,
) -> Decimal:
    """Return the delivery fee for an order.

    Priority members and orders worth at least £50 receive free delivery.
    All other orders use the standard delivery fee.
    """
    if order_total < 0:
        raise ValueError("order total cannot be negative")

    if is_priority_member or order_total >= FREE_DELIVERY_THRESHOLD:
        return Decimal("0.00")

    return STANDARD_DELIVERY_FEE
