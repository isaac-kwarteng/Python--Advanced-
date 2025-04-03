from shopping_cart import ShoppingCart

def test_setitem():
    cart = ShoppingCart({})
    cart["apple"] = 10
    assert cart.shopping_list["apple"] == 10

if __name__ == "__main__":
    test_setitem()
    print("test_setitem passed!")