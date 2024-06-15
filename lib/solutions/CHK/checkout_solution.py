from collections import Counter
import functools

# keys are the SKUs and the values are the prices.
# Each price is a tuple of (quantity, total_price), sorted in descending order of quantity.
prices = {
    "A": [(5, 200), (3, 130), (1, 50)],
    "B": [(2, 45), (1, 30)],
    "C": [(1, 20)],
    "D": [(1, 15)],
    "E": [(1, 40)],
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
    # NOTE: This euristic works with the current pricelist prices, but it doesn't work in the general case:
    #       for example, if we had A = 90, 3A = 130, 5A = 200
    #       * two bundles of 3A (130 * 2) -> 260
    #       * one bundle of 5A (200) + one individual A (90) ->  290
    #       so it would be cheaper to skip the largest offer
    pricelist_iterator = iter(prices[product_sku])
    current_offer = next(pricelist_iterator)
    while remaining > 0:
        (per_pack, pack_price) = current_offer
        # print(
        #     "sku: ",
        #     product_sku,
        #     "per_pack: ",
        #     per_pack,
        #     "pack_price: ",
        #     pack_price,
        #     "remaining: ",
        #     remaining,
        #     "total: ",
        #     total,
        # )
        if per_pack > remaining:
            current_offer = next(pricelist_iterator)
            continue
        n_packs = remaining // per_pack
        total += n_packs * pack_price
        remaining -= n_packs * per_pack
    return total


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    products_by_sku = Counter(skus)
    if set(products_by_sku.keys()) - catalogue:
        return -1
    return sum([product_subtotal(sku, count) for (sku, count) in Counter(skus).items()])
