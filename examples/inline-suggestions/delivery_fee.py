from decimal import Decimal


# Standard first line of code?

def calculate_delivery_fee(
    order_total: Decimal,
    is_priority_member: bool,
) -> Decimal:
    """Calculate the delivery fee.

    Rules:
    - Priority members receive free delivery.
    - Orders of at least £50 receive free delivery.
    - Otherwise, delivery costs £4.99.
    """



def test_priority_members_receive_free_delivery():
