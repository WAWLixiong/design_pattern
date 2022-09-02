from dataclasses import dataclass


@dataclass(frozen=True)
class CreateProductRequest:
    name: str
    price: float
    qty: int
