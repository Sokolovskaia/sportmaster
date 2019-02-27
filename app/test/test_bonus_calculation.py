from app.bonus_calculation import bonuses


def test_bonuses_for_standard_card():
    assert 100 == bonuses(2_000, 10_000)


def test_bonuses_for_silver_card():
    assert 280 == bonuses(4_500, 100_000)


def test_bonuses_for_golden_card():
    assert 100 == bonuses(1_950, 200_000)
