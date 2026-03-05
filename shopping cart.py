

def add_to_cart():
    for k, v in products.items():
        print("Available products: \n")
        print(f"ID: {k}, Name: {v["name"]}")
        id = input("Please provide product id to add to cart: ")
        if id == v["name"]:
            cart.append(id)
        else:
            print("Item is not available")

def remove_from_cart():
    ...

def view_cart():
    ...

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

