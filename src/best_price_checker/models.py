from dataclasses import dataclass

@dataclass
class Listing:
    store: str
    title: str
    tags: list
    price: float
    shipping: float

    @property
    def total_cost(self):
        self.total_cost = self.price + self.shipping