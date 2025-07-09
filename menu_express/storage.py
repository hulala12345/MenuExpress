import json
from pathlib import Path
from typing import Any, Dict, List
from .models import Restaurant, Dish, CustomMenu, MenuItem, Order

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)

RESTAURANTS_FILE = DATA_DIR / "restaurants.json"
MENUS_FILE = DATA_DIR / "menus.json"
ORDERS_FILE = DATA_DIR / "orders.json"


def load_json(path: Path, default: Any) -> Any:
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default


def save_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_restaurants() -> List[Restaurant]:
    data = load_json(RESTAURANTS_FILE, [])
    restaurants = []
    for r in data:
        dishes = [Dish(**d) for d in r.get("menu", [])]
        restaurants.append(Restaurant(id=r["id"], name=r["name"], cuisine=r["cuisine"],
                                      location=r["location"], rating=r["rating"], menu=dishes))
    return restaurants


def save_restaurants(restaurants: List[Restaurant]) -> None:
    data = []
    for r in restaurants:
        data.append({
            "id": r.id,
            "name": r.name,
            "cuisine": r.cuisine,
            "location": r.location,
            "rating": r.rating,
            "menu": [{"id": d.id, "name": d.name, "price": d.price} for d in r.menu]
        })
    save_json(RESTAURANTS_FILE, data)


def save_menu(menu: CustomMenu) -> None:
    data = load_json(MENUS_FILE, [])
    entry = {
        "restaurant": menu.restaurant.id,
        "items": [
            {"dish": item.dish.id, "quantity": item.quantity} for item in menu.items
        ]
    }
    data.append(entry)
    save_json(MENUS_FILE, data)


def save_order(order: Order) -> None:
    data = load_json(ORDERS_FILE, [])
    entry = {
        "restaurant": order.menu.restaurant.id,
        "items": [
            {"dish": item.dish.id, "quantity": item.quantity} for item in order.menu.items
        ],
        "delivery": order.delivery,
        "address": order.address,
        "datetime": order.datetime,
        "status": order.status
    }
    data.append(entry)
    save_json(ORDERS_FILE, data)
