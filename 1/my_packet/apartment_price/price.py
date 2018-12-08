def apartment_price(square, price_sqm, floor, discount):
    price = 0.01*floor*5000 + square * price_sqm - discount
    return price