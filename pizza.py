def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza witht the following toppings:")
    for topping in toppings:
        print(f"-{topping}")