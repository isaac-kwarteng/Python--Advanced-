from typing import Any


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
