from shopping_cart import ShoppingCart

def test_getitem():
    cart = ShoppingCart({"apple": 10})
    assert cart["apple"] == "apple"
    assert cart["banana"] == "Not Found"

if __name__ == "__main__":
    test_getitem()
    print("test_getitem passed!")