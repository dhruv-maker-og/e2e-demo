from app.discount import apply_discount


def test_ten_percent_off_fifty():
    assert apply_discount(50.0, 10.0) == 45.0


def test_twenty_percent_off_hundred():
    assert apply_discount(100.0, 20.0) == 80.0


def test_zero_percent():
    assert apply_discount(30.0, 0.0) == 30.0
