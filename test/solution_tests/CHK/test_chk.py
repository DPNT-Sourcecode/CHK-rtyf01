from solutions.CHK import checkout_solution


class TestSum:
    def test_single_product(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15

    def test_simple_offers(self):
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("BB") == 45

    def test_multiple_products(self):
        assert checkout_solution.checkout("AB") == 80

    def test_interspersed_skus_with_offer(self):
        # 130 AAA offer + 30 B
        assert checkout_solution.checkout("AABA") == 160

    def test_invalid_sku(self):
        assert checkout_solution.checkout("Z") == -1

    def test_offer_plus_extras(self):
        # 4A: 3A (130) + A (50) = 180
        assert checkout_solution.checkout("A" * 4) == 180

    def test_free_item(self):
        assert checkout_solution.checkout("EEB") == 80

    def test_free_item_disrupting_b_offer(self):
        assert checkout_solution.checkout("BBEE") == 110
