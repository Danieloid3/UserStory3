class Product:
    __idActual= 1
    def __init__(self, name: str, quantity: int, price: float, product_id: int | None = None):
        if product_id is None:
            self._productID = Product.__idActual
            Product.__idActual += 1
        else:
            self._productID = int(product_id)
            if self._productID >= Product.__idActual:
                Product.__idActual = self._productID + 1
        self._name = name
        self._quantity = quantity
        self._price = price

    @property
    def productID(self) -> int:
        return self._productID
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def quantity(self) -> int:
        return self._quantity
    @quantity.setter
    def quantity(self, value: int):
        self._quantity = value
    @property
    def price(self) -> float:
        return self._price
    @price.setter
    def price(self, value: float):
        self._price = value
    @property
    def total(self) -> float:
        return self._price * self._quantity