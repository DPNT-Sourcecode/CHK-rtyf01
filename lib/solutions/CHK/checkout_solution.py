from collections import Counter
import sys

# keys are the SKUs and the values are the prices.
# Each price is a tuple of (quantity, total_price), sorted in descending order of quantity.
prices = {
    "A": [(5, 200), (3, 130), (1, 50)],
    "B": [(2, 45), (1, 30)],
    "C": [(1, 20)],
    "D": [(1, 15)],
    "E": [(1, 40)],
    "F": [(1, 10)],
    "G": [(1, 20)],
    "H": [(10, 80), (5, 45), (1, 10)],
    "I": [(1, 35)],
    "J": [(1, 60)],
    "K": [(2, 120), (1, 70)],
    "L": [(1, 90)],
    "M": [(1, 15)],
    "N": [(1, 40)],
    "O": [(1, 10)],
    "P": [(5, 200), (1, 50)],
    "Q": [(3, 80), (1, 30)],
    "R": [(1, 50)],
    "S": [(1, 30)],
    "T": [(1, 20)],
    "U": [(1, 40)],
    "V": [(3, 130), (2, 90), (1, 50)],
    "W": [(1, 20)],
    "X": [(1, 90)],
    "Y": [(1, 10)],
    "Z": [(1, 50)],
}

# set of valid SKUs
catalogue = set(prices.keys())

free_items = [
    ("E", 2, "B"),
    ("F", 3, "F"),
    ("N", 3, "M"),
    ("R", 3, "Q"),
    ("U", 4, "U"),
]

group_discounts = [
    # (skus, quantity, pack_price)
    ("STXYZ", 3, 45)
]


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
    # I assume this is part of the
    # "All the offers are well balanced so that they can be safely combined."
    # constraint. (though I am veryfing such cases manually anyway)
    pricelist_iterator = iter(prices[product_sku])
    current_offer = next(pricelist_iterator)
    while remaining > 0:
        (per_pack, pack_price) = current_offer
        if per_pack > remaining:
            current_offer = next(pricelist_iterator)
            continue
        n_packs = remaining // per_pack
        total += n_packs * pack_price
        remaining -= n_packs * per_pack
    print(f"product_subtotal({product_sku}, {count}) = {total}", file=sys.stderr)
    return total


def remove_free_items(all_items_counter: Counter) -> Counter:
    free_items_counter = Counter()
    for required_item, required_quantity, free_item in free_items:
        free_items_counter[free_item] = (
            all_items_counter.get(required_item, 0) // required_quantity
        )
    return all_items_counter - free_items_counter


def group_discount(items: Counter) -> tuple[Counter, int]:
    """
    Returns an updated counter where, and the total price of the items in the group discount
    """
    # the next line exploits Counter intersection to build a counter of just the group skus,
    # with the quantity of each sku coming from the nonfree_items counter
    group_items = nonfree_items & Counter({sku: sys.maxsize for sku in skus})
    # we sort all the items in the group by price, descending
    # (again we rely on group discount skus not belonging to any other offers and thus having only
    # a single price in the price list)
    sorted_candidates = sorted(group_items.elements(), key=lambda sku: prices[sku][0][1], reverse=True)
    # we take as many as possible of the most expensive items in order to maximize the discount
    n_packs = len(sorted_candidates) // per_pack
    used = sorted_candidates[:n_packs * per_pack]


def handle_group_discounts(nonfree_items: Counter) -> tuple[Counter, int]:
    # we rely on the skus in the group discounts not having or interacting with any other offer type,
    # which makes calculations easier as we can just consider each group independently
    # and adopt a simple heuristic: we choose all the most expensive products to
    # We also assume that
    remaining_items = nonfree_items.copy()
    groups_total
    for skus, per_pack, pack_price in group_discounts:
    return (nonfree_items, 0)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    products_by_sku = Counter(skus)
    if set(products_by_sku.keys()) - catalogue:
        return -1
    nonfree_products_by_sku = remove_free_items(products_by_sku)
    return sum(
        [
            product_subtotal(sku, count)
            for (sku, count) in nonfree_products_by_sku.items()
        ]
    )

