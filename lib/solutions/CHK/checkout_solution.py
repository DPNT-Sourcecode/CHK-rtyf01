from collections import Counter
import functools

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


def product_subtotal(product_sku: str, count: int) -> int:
    """
    Returns the total price for 'count' items of product with SKU 'sku'.
    """
    total = 0
    remaining = count
    # we assume that larger quantities imply best per-unit price,
    # therefore we iterate over "offers" in order, largest quantities to lowest
    # (we assumed the pricelist is ordered in descending order of quantity)
    # NOTE: there should always be one final "offer" with quantity 1, i.e. the basic unic price
    pricelist_iterator = iter(prices[product_sku])
    current_offer = next(pricelist_iterator)
    while remaining > 0:
        (per_pack, pack_price) = current_offer
        if per_pack > remaining:
            current_offer = next(pricelist_iterator)
            continue
        n_packs = remaining // per_pack
        total += per_pack * n_packs
        remaining -= n_packs * pack_price
    return total


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    return sum([product_subtotal(sku, count) for (sku, count) in Counter(skus)])
