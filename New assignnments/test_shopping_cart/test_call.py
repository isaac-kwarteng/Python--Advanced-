from shopping_cart import ShoppingCart

def test_call():
    cart = ShoppingCart({"apple": 10, "banana": 5})
    assert cart() == 15

if __name__ == "__main__":
    test_call()
    print("test_call passed!")