from .models import Dish, Restaurant
from .storage import save_restaurants

restaurants = [
    Restaurant(
        id=1,
        name="Pasta Palace",
        cuisine="Italian",
        location="Downtown",
        rating=4.5,
        menu=[
            Dish(id=1, name="Spaghetti Bolognese", price=12.0),
            Dish(id=2, name="Fettuccine Alfredo", price=11.0),
            Dish(id=3, name="Margherita Pizza", price=10.0),
        ],
    ),
    Restaurant(
        id=2,
        name="Sushi Central",
        cuisine="Japanese",
        location="Uptown",
        rating=4.7,
        menu=[
            Dish(id=1, name="California Roll", price=8.0),
            Dish(id=2, name="Salmon Nigiri", price=9.5),
            Dish(id=3, name="Tempura", price=7.0),
        ],
    ),
]

if __name__ == "__main__":
    save_restaurants(restaurants)
    print("Sample restaurants saved.")
