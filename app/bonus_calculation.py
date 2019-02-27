def bonuses(purchase_amount, previous_purchase_amount):
    standard_card_bonuses = 50
    silver_card_bonuses = 70
    golden_card_bonuses = 100

    if 1 < (previous_purchase_amount + purchase_amount) < 15_001:
        return purchase_amount // 1000 * standard_card_bonuses

    if 15_001 < (previous_purchase_amount + purchase_amount) <= 150_000:
        return purchase_amount // 1000 * silver_card_bonuses

    if (previous_purchase_amount + purchase_amount) > 150_000:
        return purchase_amount // 1000 * golden_card_bonuses
