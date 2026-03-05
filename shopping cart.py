

def add_to_cart():
    for k, v in products.items():
        print("Available products: \n")
        print(f"ID: {k}, Name: {v['name']}")
    pro_id = input("Please provide product id to add to cart: ")
    if pro_id == k:
        cart.append(pro_id)
    else:
        print("Item is not available")

def remove_from_cart():
    for item in cart:
        print(f"{item}")
    id_to_remove = input("Which product do you want to remove? type product ID ")
    if id_to_remove in cart:
        cart.pop(id_to_remove)
    else:
        print("There is no such product in cart")

def view_cart():
    for item in cart:
        print(f"{item["name"]}")
        print(f"{item["price"]}")


cart = []

products = {
    "prod1" : {
        "id": 1,
        "name": "sponge",
        "brand": "square",
        "country": "china",
        "year": 2026,
        "price": 1.15,
    },
    "prod2" : {
        "id": 2,
        "name": "brush",
        "brand": "square",
        "country": "china",
        "year": 2026,
        "price": 2.15,
    },
    "prod3" : {
        "id": 3,
        "name": "soap",
        "brand": "square",
        "country": "china",
        "year": 2026,
        "price": 3.15,
    }
}

