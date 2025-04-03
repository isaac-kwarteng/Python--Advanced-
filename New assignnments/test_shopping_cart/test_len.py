from shopping_cart import ShoppingCart

def test_len():
    cart = ShoppingCart({"apple": 10, "banana": 5})
    assert len(cart) == 2

if __name__ == "__main__":
    test_len()
    print("test_len passed!")