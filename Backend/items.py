class Item:
    """
    A blueprint for all items presented in the company 
    that can be identifed according to description - price of single item - total quantity in the item 
    """

    def __init__(self, description: str, price: float, quantity: int) -> None:
        self.description = description
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        return self.quantity * self.price

class Book(Item):
    def __init__(self, description: str, price: float, quantity: int, author_name: str) -> None:
        super().__init__(description, price, quantity)
        self.author_name = author_name

class NoteBook(Item):
    
    def __init__(self, description: str, price: float, quantity: int, number_of_pages: int) -> None:
        super().__init__(description, price, quantity)
        self.number_of_pages = number_of_pages

"TODO: Add Other items"


