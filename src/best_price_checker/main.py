def main() -> None:
    listings = [
        {"store": "bestbuy", "title": "iphone 15 case", "tags": ["iphone15", "case"], "price": 12.99, "shipping": 0.0},
        {"store": "bestbuy", "title": "24-inch samsung tv", "tags": ["samsung", "tv", "24-inch"], "price": 399.99, "shipping": 0.0},
        {"store": "bestbuy", "title": "blender", "tags": ["blender", "machine"], "price": 19.99, "shipping": 0.0},
        {"store": "amazon", "title": "apples", "tags": ["fruit", "red"], "price": 1.9, "shipping": 2.99},
        {"store": "amazon", "title": "blender", "tags": ["blender", "machine"], "price": 15.99, "shipping": 4.99},
        {"store": "alibaba", "title": "blender", "tags": ["blender", "machine"], "price": 3.99, "shipping": 2.99}
    ]

    search_term = input("Please Enter a Search Term: ")
    terms = search_term.strip().lower().split()

    if not terms:
        print("Please enter an item to search")
    else:
        matches = []
        for listing in listings:
            # a listing matches when every search word is in its title or its tags
            if all(term in listing["title"] or term in listing["tags"] for term in terms):
                matches.append(listing)

        if not matches:
            print("No matching items found")
        else:
            print("Sorting by: Total Price")
            print(f"{"Store:":<12} | {"Title:":<15} | {"Price:":<12} | {"Shipping:":>8}") # if it ain't broke don't fix it
            print("-" * 55)

            sorted_matches = sorted(matches, key=lambda x: x['price'] + x['shipping'])
            for listing in sorted_matches:
                print(f"{listing["store"]:<12} | {listing["title"]:<15} | ${listing["price"]:<12.2f} | ${listing["shipping"]:>8.2f}")
