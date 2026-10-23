from pricing import checkout_total


def test_discount_applied_once():
    # 10% off a 100.00 cart should be 90.00, not 81.00
    assert checkout_total([60.0, 40.0], 10) == 90.0
