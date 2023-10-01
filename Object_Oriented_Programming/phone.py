from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #call to super function to have access to all attributes instead of copying and pasting from class
        super().__init__(
            name, price, quantity
        )
        #validate inputs are okay
        assert broken_phones >= 0, f"Broken_Phones {broken_phones} is not greater than 0!"
        
        #assign to self object
    
        self.broken_phones = broken_phones
