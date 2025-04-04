class ShoppingCart:
    def __init__(self, shopping_list: dict[str, int]) -> None:
        self.shopping_list = shopping_list

    def __setitem__(self, item: str, price: int) -> None:
        self.shopping_list[item] = price

    def __getitem__(self, item: str) -> str:
        return item if item in self.shopping_list else "Not Found"

    def __len__(self) -> int:
        return len(self.shopping_list)

    def __call__(self) -> int:
        return sum(self.shopping_list.values())


if __name__=="__main__":
    shopping_list = {"Lighter" : 40, "Sardine" : 10}
    shopping_cart = ShoppingCart(shopping_list)
    print(shopping_cart.__getitem__("Sardine"))
    shopping_cart.__setitem__("Fridge", 2000)
    print(shopping_cart.__len__())
    print(shopping_cart.__call__())
