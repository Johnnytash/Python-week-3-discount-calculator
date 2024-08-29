# Create a function named calculate_discount(price, discount_percent)
# that calculates the final price after applying a discount.


def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompting user for input of original price and discount %

original_price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))


# Calculating the final price

final_price = calculate_discount(original_price, discount_percent)


# Printing the result
if final_price == original_price:
    print(f"No discount applied. The price remains ${final_price:.2f}")
else:
    print(f"The final price after applying the {discount_percent}% discount is ${final_price:.2f}")