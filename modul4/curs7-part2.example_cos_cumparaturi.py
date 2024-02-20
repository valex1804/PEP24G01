cart = {'apple': 10, 'plums': 15, 'bananas': 5}   # quantity

shop_k = {'apple': 1.2, 'plums': 4, 'bananas': 5.5}   # price
shop_p = {'apple': 1.3, 'plums': 3, 'bananas': 8}        # price
shop_l = {'apple': 1.4, 'plums': 2, 'bananas': 10}         # price

shops = {'pro': shop_p, 'lil': shop_l, 'kau': shop_k}    # name for shop

result = {}
for cart_product, cart_quantity in cart.items():
    # print(cart_product, cart_quantity)  # just for print  , useful for debug and to see if we are on the good road
    for shop_name, shop_products in shops.items():
        # print(shop_name, shop_products[cart_product] * cart_quantity)  # just for print
        result[shop_name] = result.get(shop_name, 0) + (shop_products[cart_product] * cart_quantity)
print(result)

# min_price = 99999    # var 1
# shop_name = ''
# for name, price in result.items():
#     # print(name, price)
#     if price < min_price:
#         min_price = price
#         shop_name = name
# print(shop_name)

min_price = None  # var 2
shop_name = ''
for name, price in result.items():
    # print(name, price)
    if min_price is None or price < min_price:
        min_price = price
        shop_name = name
print(shop_name)

