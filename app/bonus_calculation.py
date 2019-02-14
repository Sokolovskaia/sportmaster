standard_card_bonuses = 50
silver_card_bonuses = 70
golden_card_bonuses = 100
input_error = "произошла ошибка начисления"


def bonuses(purchase_amount, previous_purchase_amount):
    if type(purchase_amount) != str and type(previous_purchase_amount) != str:

        if 1 < (previous_purchase_amount + purchase_amount) < 15_001:
            accrued_bonuses = purchase_amount // 1000 * standard_card_bonuses

        elif 15_001 < (previous_purchase_amount + purchase_amount) <= 150_000:
            accrued_bonuses = purchase_amount // 1000 * silver_card_bonuses

        elif (previous_purchase_amount + purchase_amount) > 150_000:
            accrued_bonuses = purchase_amount // 1000 * golden_card_bonuses

        else:
            accrued_bonuses = input_error

    else:
        accrued_bonuses = input_error

    return accrued_bonuses


print("У вас", bonuses(2000, 10000), "бонусов")

