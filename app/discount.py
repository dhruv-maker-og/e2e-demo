"""Drop-in module for the Agent Mode (Segment 3) red -> green demo.

Copy this file to `app/discount.py` and the test to `tests/test_discount.py`,
commit on a branch, and let CI go RED. Then use Agent Mode in VS Code to fix
`apply_discount` until `pytest` is green.

The bug: percentage handling is wrong. A 20% discount on 100 should return 80.0,
but this implementation subtracts the raw percent (100 - 20 = 80 only by luck for
some inputs) — try it with pct=10 on price=50 and it returns 40.0 instead of 45.0.
"""


def apply_discount(price: float, pct: float) -> float:
    return price * (1 - pct / 100)
