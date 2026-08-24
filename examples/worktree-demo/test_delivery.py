import unittest
from decimal import Decimal

from delivery import calculate_delivery_fee


class CalculateDeliveryFeeTests(unittest.TestCase):
    def test_standard_delivery_costs_4_99(self) -> None:
        fee = calculate_delivery_fee(
            order_total=Decimal("25.00"),
            is_priority_member=False,
        )

        self.assertEqual(fee, Decimal("4.99"))

    def test_priority_members_receive_free_delivery(self) -> None:
        fee = calculate_delivery_fee(
            order_total=Decimal("25.00"),
            is_priority_member=True,
        )

        self.assertEqual(fee, Decimal("0.00"))

    def test_orders_of_at_least_50_receive_free_delivery(self) -> None:
        fee = calculate_delivery_fee(
            order_total=Decimal("50.00"),
            is_priority_member=False,
        )

        self.assertEqual(fee, Decimal("0.00"))

    def test_negative_order_total_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "order total cannot be negative"):
            calculate_delivery_fee(
                order_total=Decimal("-0.01"),
                is_priority_member=False,
            )


if __name__ == "__main__":
    unittest.main()
