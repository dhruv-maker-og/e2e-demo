"""Drop-in module for the Agent Mode (Segment 3) red -> green demo.

Copy this file to `app/discount.py` and the test to `tests/test_discount.py`,
commit on a branch, and let CI go RED. Then use Agent Mode in VS Code to fix
`apply_discount` until `pytest` is green.

The bug: forgot to divide pct by 100 before applying it, so any non-zero pct
blows up the result (e.g. price=50, pct=10 returns -450.0 instead of 45.0).
The pct=0 case still passes by coincidence (2 of 3 tests fail).
"""


def apply_discount(price: float, pct: float) -> float:
    # BUG: pct should be divided by 100 before being applied
    return price - price * (pct / 100)
