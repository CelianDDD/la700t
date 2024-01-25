class Carrot:
    def __init__(self, quantity: int) -> None:
        """
        Initialize a Carrot object with a given quantity.

        Parameters:
        - quantity: Integer representing the quantity of carrots.

        Attributes:
        - quantity: Integer representing the quantity of carrots.
        """
        self.quantity: int = quantity # quantity of carrots
        self.quantity_history: list = [quantity] # list of carrot quantities over time


    def update_history(self):
        self.quantity_history.append(self.quantity) # add the current quantity to the history