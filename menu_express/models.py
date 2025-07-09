from dataclasses import dataclass, field
from typing import List

@dataclass
class Dish:
    id: int
    name: str
    price: float

@dataclass
class Restaurant:
    id: int
    name: str
    cuisine: str
    location: str
    rating: float
    menu: List[Dish] = field(default_factory=list)

@dataclass
class MenuItem:
    dish: Dish
    quantity: int

@dataclass
class CustomMenu:
    restaurant: Restaurant
    items: List[MenuItem] = field(default_factory=list)

    def add_item(self, dish: Dish, quantity: int = 1):
        for item in self.items:
            if item.dish.id == dish.id:
                item.quantity += quantity
                return
        self.items.append(MenuItem(dish=dish, quantity=quantity))

    def remove_item(self, dish_id: int):
        self.items = [i for i in self.items if i.dish.id != dish_id]

    def total_price(self) -> float:
        return sum(item.dish.price * item.quantity for item in self.items)

@dataclass
class Order:
    menu: CustomMenu
    delivery: bool
    address: str
    datetime: str
    status: str = "Pending"
