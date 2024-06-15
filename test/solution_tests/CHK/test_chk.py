import random

from solutions.CHK import checkout_solution


def shuffle_string(s: str) -> str:
    items = list(s)
    random.shuffle(items)
    return "".join(items)


class TestSum:
    def test_single_product(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("E") == 40
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("G") == 20
        assert checkout_solution.checkout("H") == 10
        assert checkout_solution.checkout("I") == 35
        assert checkout_solution.checkout("J") == 60
        assert checkout_solution.checkout("K") == 70
        assert checkout_solution.checkout("L") == 90
        assert checkout_solution.checkout("M") == 15
        assert checkout_solution.checkout("N") == 40
        assert checkout_solution.checkout("O") == 10
        assert checkout_solution.checkout("P") == 50
        assert checkout_solution.checkout("Q") == 30
        assert checkout_solution.checkout("R") == 50
        assert checkout_solution.checkout("S") == 20
        assert checkout_solution.checkout("T") == 20
        assert checkout_solution.checkout("U") == 40
        assert checkout_solution.checkout("V") == 50
        assert checkout_solution.checkout("W") == 20
        assert checkout_solution.checkout("X") == 17
        assert checkout_solution.checkout("Y") == 20
        assert checkout_solution.checkout("Z") == 21

    def test_simple_offers(self):
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("BB") == 45

    def test_multiple_products(self):
        assert checkout_solution.checkout("AB") == 80

    def test_interspersed_skus_with_offer(self):
        # 130 AAA offer + 30 B
        assert checkout_solution.checkout("AABA") == 160

    def test_invalid_sku(self):
        assert checkout_solution.checkout("z") == -1

    def test_offer_plus_extras(self):
        # 4A: 3A (130) + A (50) = 180
        assert checkout_solution.checkout("A" * 4) == 180

    def test_free_item(self):
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("QRRR") == 150
        assert checkout_solution.checkout("N" * 6 + "M" * 2) == 40 * 6

    def test_free_item_disrupting_another_offer(self):
        assert checkout_solution.checkout("BBEE") == 110
        assert checkout_solution.checkout("QQQRRR") == 210

    def test_offer_combination(self):
        assert checkout_solution.checkout("A" * 9) == 200 + 130 + 50

    def test_buy_two_get_one_free(self):
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        # weird case, as the customer could've bought one extra F for the same total
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40

    def test_buy_three_get_one_free(self):
        assert checkout_solution.checkout("U" * 3) == 120
        assert checkout_solution.checkout("U" * 4) == 120
        assert checkout_solution.checkout("U" * 5) == 160
        assert checkout_solution.checkout("U" * 8) == 240

    def test_huge_purchase(self):
        purchase = shuffle_string("V" * 6 + "U" * 4 + "R" * 3 + "Q" * 4 + "A" * 4)
        assert checkout_solution.checkout(purchase) == (
            (130 * 2)  # 3V * 2
            + (40 * 3)  # 1U * 3, one free
            + (50 * 3)  # 1R * 3
            + 80  # 3Q + 1Q free from R
            + (130 + 50)  # 3A + 1A
        )

    def test_group_discount_simple(self):
        assert checkout_solution.checkout("XYZ") == 45
        assert checkout_solution.checkout("XXX") == 45
        assert checkout_solution.checkout("STS") == 45

    def test_group_discount_multiple(self):
        assert checkout_solution.checkout("XYZZST") == 90
        assert checkout_solution.checkout("XXXXXX") == 90

    def test_group_discount_with_leftovers(self):
        # it should take the most expensive skus in the group discount
        assert checkout_solution.checkout("YXZZX") == 79

