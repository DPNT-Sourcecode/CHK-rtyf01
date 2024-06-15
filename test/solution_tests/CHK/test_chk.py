from solutions.CHK import checkout_solution


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
        assert checkout_solution.checkout("K") == 80
        assert checkout_solution.checkout("L") == 90
        assert checkout_solution.checkout("M") == 15
        assert checkout_solution.checkout("N") == 40
        assert checkout_solution.checkout("O") == 10
        assert checkout_solution.checkout("P") == 50
        assert checkout_solution.checkout("Q") == 30
        assert checkout_solution.checkout("R") == 50
        assert checkout_solution.checkout("S") == 30
        assert checkout_solution.checkout("T") == 20
        assert checkout_solution.checkout("U") == 40
        assert checkout_solution.checkout("V") == 50
        assert checkout_solution.checkout("W") == 20
        assert checkout_solution.checkout("X") == 90
        assert checkout_solution.checkout("Y") == 10
        assert checkout_solution.checkout("Z") == 50

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




