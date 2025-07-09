import datetime
from typing import List
from .models import Dish, Restaurant, CustomMenu, Order
from .storage import load_restaurants, save_restaurants, save_menu, save_order


def search_restaurants(restaurants: List[Restaurant], query: str = "", cuisine: str = "", location: str = "", min_rating: float = 0.0) -> List[Restaurant]:
    results = []
    for r in restaurants:
        if query and query.lower() not in r.name.lower():
            continue
        if cuisine and cuisine.lower() != r.cuisine.lower():
            continue
        if location and location.lower() not in r.location.lower():
            continue
        if r.rating < min_rating:
            continue
        results.append(r)
    return results


def show_restaurant(r: Restaurant):
    print(f"\n{r.name} ({r.cuisine}) - {r.location} - Rating {r.rating}")
    for dish in r.menu:
        print(f"  {dish.id}. {dish.name} - ${dish.price}")


def select_dishes(r: Restaurant) -> CustomMenu:
    menu = CustomMenu(restaurant=r)
    while True:
        show_restaurant(r)
        choice = input("Enter dish id to add (or 'done'): ").strip()
        if choice.lower() == 'done':
            break
        try:
            dish_id = int(choice)
        except ValueError:
            continue
        dish = next((d for d in r.menu if d.id == dish_id), None)
        if not dish:
            print("Invalid dish id")
            continue
        qty = input("Quantity: ").strip()
        try:
            qty = int(qty)
        except ValueError:
            qty = 1
        menu.add_item(dish, qty)
    return menu


def schedule_order(menu: CustomMenu) -> Order:
    delivery_choice = input("Delivery or pickup (d/p)? ").strip().lower()
    delivery = delivery_choice == 'd'
    address = ''
    if delivery:
        address = input("Delivery address: ").strip()
    dt_str = input("Date and time (YYYY-mm-dd HH:MM): ").strip()
    try:
        dt = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    except ValueError:
        dt = datetime.datetime.now()
    order = Order(menu=menu, delivery=delivery, address=address, datetime=dt.isoformat())
    save_order(order)
    print("Order scheduled!")
    return order


def main():
    restaurants = load_restaurants()
    if not restaurants:
        print("No restaurants data found. Initializing sample data.")
        from .init_data import restaurants as sample
        save_restaurants(sample)
        restaurants = load_restaurants()

    while True:
        query = input("Search restaurants (or leave blank): ").strip()
        cuisine = input("Filter by cuisine (or leave blank): ").strip()
        location = input("Filter by location (or leave blank): ").strip()
        try:
            rating = float(input("Minimum rating (0-5): ").strip() or 0)
        except ValueError:
            rating = 0
        results = search_restaurants(restaurants, query, cuisine, location, rating)
        if not results:
            print("No restaurants found.")
            continue
        for idx, r in enumerate(results, 1):
            print(f"{idx}. {r.name} ({r.cuisine}) - {r.location} - Rating {r.rating}")
        sel = input("Select restaurant number (or 'q' to quit): ").strip()
        if sel.lower() == 'q':
            break
        try:
            r_idx = int(sel) - 1
            restaurant = results[r_idx]
        except (ValueError, IndexError):
            print("Invalid selection")
            continue
        menu = select_dishes(restaurant)
        if not menu.items:
            print("No dishes selected.")
            continue
        print(f"Total price: ${menu.total_price():.2f}")
        save_menu(menu)
        schedule_order(menu)
        another = input("Create another order? (y/n): ").strip().lower()
        if another != 'y':
            break


if __name__ == "__main__":
    main()
