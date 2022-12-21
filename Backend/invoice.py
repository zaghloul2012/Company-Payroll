from Backend.items import Item

class Invoice:
    """
    Invoice is a set of items in the company where each invoice can be identifed with its id
    """
    def __init__(self, id: int) -> None:
        self.id = id
        self.items = list()
    
    def __str__(self) -> str:
        return f"Invoice - Id: {self.id}"

    def __repr__(self) -> str:
        return f"Inovice(Id: {self.id}"
    
    def __lt__(self, other):
        """
        A way of comparing inovices first by its type
        and if they have the same type they will be ordered based on length of elements inside it

        Args:
            self (Invoice): First Invoice
            other (Invoice): Second Invoice
            

        Returns:
            Boolean: Whether the first invoice must come first or not based on our standards
        """
        if type(self) is not type(other):
            return self.__class__.__name__ < other.__class__.__name__

        return (self.id, len(self.items)) < (other.id, len(other.items))

    def add_item(self, item: Item) -> None:
        self.items.append(item)
    
    def total_payment(self) -> float:
        return sum([item.total_price() for item in self.items])

