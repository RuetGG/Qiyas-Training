# =====================================================
# Exercise 3: Product Inventory Analyzer
# =====================================================

products = [
    ("Laptop", 15, 70000),
    ("Mouse", 50, 1200),
    ("Keyboard", 30, 2500),
    ("Monitor", 10, 15000),
    ("USB", 100, 500)
]


def total_inventory_value(product_list):
    """
    Calculate total inventory value.
    quantity * price
    """
    return list(map(lambda x: (x[0], x[1]*x[2]), product_list))
    
   


def most_expensive_product(product_list):
    """
    Return most expensive product.
    """
    mep = max(price for name, quantity, price in product_list)
    return mep


def low_stock_products(product_list):
    """
    Return products with quantity < 20.
    """
    lsp = min(quantity for name, quantity, price in product_list)
    return lsp


def increase_prices(product_list):
    """
    Increase prices by 15% using map().
    """
    ip = list(map(lambda x: (x[0], x[1], x[2] + x[2] * 0.15), product_list))
    return ip


def sort_products_by_quantity(product_list):
    """
    Sort products by quantity.
    """
    sort_products = sorted(product_list, key=lambda x: x[1])
    return sort_products


def process_quantities(product_list):
    """
    Square even quantities.
    Cube odd quantities.
    """
    ans = [q ** 2 if q % 2 == 0 else q ** 3 for name, q, price in product_list]
    return ans


def expensive_products(product_list):
    """
    Use filter() to get products costing above 5000.
    """
    ep = filter(lambda x: x[2] > 5000, product_list)
    return ep


print(total_inventory_value(products))
print(most_expensive_product(products))
print(low_stock_products(products))
print(increase_prices(products))
print(sort_products_by_quantity(products))
print(process_quantities(products))
print(list(expensive_products(products)))