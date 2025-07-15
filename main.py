from benz_factory import BenzFactory
from bmw_factory import BMWFactory
from client import client_code

if __name__ == "__main__":
    brand = input("Enter brand (benz/bmw): ").strip().lower()

    if brand == "benz":
        factory = BenzFactory()
    elif brand == "bmw":
        factory = BMWFactory()
    else:
        raise ValueError("Unsupported brand!")

    client_code(factory)