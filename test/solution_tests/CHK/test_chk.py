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
        assert checkout_solution.checkout("E") == -1

