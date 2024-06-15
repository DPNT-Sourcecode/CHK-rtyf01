# keys are the SKUs and the values are the prices.
# Each price is a tuple of (quantity, total_price), sorted in descending order of quantity.
prices = {
    "A": [(3, 130), (1, 50)],
    "B": [(2, 45), (1, 30)],
    "C": [(1, 20)],
    "D": [(1, 15)],
}

# set of valid SKUs
catalogue = set(prices.keys())


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    raise NotImplementedError()

