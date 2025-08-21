def calculate_discount(price, discount_percent):
    if discount_percent < 20:
        return price
    else:
        discount_amount = price * (discount_percent / 100)
        price = price - discount_amount
        return price
price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

print(f"The price after discount is: {calculate_discount(price, discount_percent)}")
