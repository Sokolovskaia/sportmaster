from app.bonus_calculation import bonuses


def test_bonuses_for_types():
    accrued_bonuses = bonuses("три тысячи", 100000)

    assert "произошла ошибка начисления" == accrued_bonuses


def test_bonuses_for_standard_card():
    accrued_bonuses = bonuses(2_000, 10_000)

    assert 100 == accrued_bonuses


def test_bonuses_for_silver_card():
    accrued_bonuses = bonuses(4_500, 100_000)

    assert 280 == accrued_bonuses


def test_bonuses_for_golden_card():
    accrued_bonuses = bonuses(1_950, 200_000)

    assert 100 == accrued_bonuses


def test_bonuses_for_input_errors():
    accrued_bonuses = bonuses(-1000, 0)

    assert "произошла ошибка начисления" == accrued_bonuses
