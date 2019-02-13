from app.bonus_calculation import bonuses


def test_bonuses_for_standard_card():
    accrued_bonuses = bonuses(2_000, 10_000)

    assert 100 == accrued_bonuses


def test_bonuses_for_silver_card():
    accrued_bonuses = bonuses(4_500, 100_000)

    assert 280 == accrued_bonuses


def test_bonuses_for_golden_card():
    accrued_bonuses = bonuses(1_950, 200_000)

    assert 100 == accrued_bonuses


def test_bonuses_for_input_error():
    accrued_bonuses = bonuses(1_300, -100000)

    assert "Неверное формат поля <<Суммы предыдущих покупок>>" == accrued_bonuses
