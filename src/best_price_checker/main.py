from best_price_checker.models import Listing

def main() -> None:
    listings = [
        Listing(store="bestbuy", title="iphone 15 case", tags=["iphone15", "case"], price=12.99, shipping=0.0),
        Listing(store="bestbuy", title="24-inch samsung tv", tags=["samsung", "tv", "24-inch"], price=399.99, shipping=0.0),
        Listing(store="bestbuy", title="blender", tags=["blender", "machine"], price=19.99, shipping=0.0),
        Listing(store="amazon", title="apples", tags=["fruit", "red"], price=1.9, shipping=2.99),
        Listing(store="amazon", title="blender", tags=["blender", "machine"], price=15.99, shipping=4.99),
        Listing(store="alibaba", title="blender", tags=["blender", "machine"], price=3.99, shipping=2.99)
    ]

    search_term = input("Please Enter a Search Term: ")
    terms = search_term.strip().lower().split() # search terms collected
    
    try:
        max_price = float(input("Please enter a max price (input 0 for no max price): ")) # max price collected
        if max_price == 0: 
            max_price = None
        elif max_price < 0:
            print("you entered an invalid value, defaulted to no max price as a result")
            max_price = None
    except ValueError:
        max_price = None
        print("you entered an invalid value, defaulted to no max price as a result")
    

    if not terms:
        print("Please enter an item to search")
    else:
        matches = []
        for listing in listings:
            matches_search = all(term in listing["title"] or term in listing["tags"] for term in terms) # a listing matches when every search word is in its title or its tags
            total = listing["price"] + listing["shipping"]
            if matches_search and (max_price is None or total <= max_price):
                matches.append(listing)
        if not matches:
            print("No matching items found")
        else:
            print("Sorting by: Total Price")
            print("-" * 84 + "|")
            print(f"{"Store:":<12} | {"Title:":<20} | {"Price:":<13} | {"Shipping:":<13} | {"Total:":<13} {"|":<12}") # if it ain't broke don't fix it
            print("-" * 84 + "|")

            sorted_matches = sorted(matches, key=lambda x: x['price'] + x['shipping'])
            for listing in sorted_matches:
                total = listing["price"] + listing["shipping"]
                print(f"{listing["store"]:<12} | {listing["title"]:<20} | ${listing["price"]:<12.2f} | ${listing["shipping"]:<12.2f} | ${total:<12.2f} {"|":<12}")
