from rabbit import Rabbit

class Fox:
    def __init__(self) -> None:
        """
        Initialize a Fox object.

        Attributes:
        - rabbits_eaten: Integer representing the number of rabbits eaten by the fox.
        """
        self.rabbits_eaten: int = 0 # number of rabbits eaten by the fox

    def eat_rabbit(self, rabbit: Rabbit) -> None:
        """
        Simulate the fox eating a rabbit.

        Parameters:
        - rabbit: Rabbit object representing the rabbit being eaten.

        Returns:
        - None
        """
        rabbit.eaten_by_fox = True # rabbit is eaten by the fox
        self.rabbits_eaten += 1 # increment the number of rabbits eaten by the fox
