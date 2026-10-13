from dataclasses import dataclass

@dataclass
class Listing:
    store: str
    title: str
    tags: list[str]
    price: float
    shipping: float

    @property
    def total_cost(self) -> float:
        return self.price + self.shipping