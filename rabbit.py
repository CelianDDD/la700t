class Rabbit:
    def __init__(self, age: int, gender: str) -> None:
        """
        Initialize a Rabbit object with age, gender, and other attributes.

        Parameters:
        - age: Integer representing the age of the rabbit.
        - gender: String representing the gender of the rabbit ('male' or 'female').

        Attributes:
        - age: Integer representing the age of the rabbit.
        - gender: String representing the gender of the rabbit ('male' or 'female').
        - weeks_since_last_meal: Integer representing the number of weeks since the rabbit's last meal.
        - is_pregnant: Boolean indicating whether the rabbit is pregnant.
        - weeks_pregnant: Integer representing the number of weeks the rabbit has been pregnant.
        - eaten_by_fox: Boolean indicating whether the rabbit has been eaten by a fox.
        """
        self.age: int = age # age of the rabbit
        self.gender: str = gender # gender of the rabbit
        self.weeks_since_last_meal: int = 0 # number of weeks since the rabbit's last meal
        self.is_pregnant: bool = False # whether the rabbit is pregnant
        self.weeks_pregnant: int = 0 # number of weeks the rabbit has been pregnant
        self.eaten_by_fox: bool = False # whether the rabbit has been eaten by a fox

    def eat(self, carrots) -> None:
        """
        Simulate the rabbit eating carrots.

        Parameters:
        - carrots: Carrot object representing the available carrots.

        Returns:
        - None
        """
        if carrots.quantity > 0: # if there are carrots available
            carrots.quantity -= 1 # decrement the quantity of carrots
            self.weeks_since_last_meal = 0 # reset the number of weeks since the rabbit's last meal
            #print("Rabbit ate a carrot!")
        else:
            self.weeks_since_last_meal += 1 # increment the number of weeks since the rabbit's last meal
            #print("Rabbit couldn't find a carrot to eat.")

    def can_reproduce(self) -> bool:
        """
        Check if the rabbit can reproduce based on age, gender, and pregnancy status.

        Returns:
        - True if the rabbit can reproduce, False otherwise.
        """
        return 52 <= self.age < 312 and self.gender == 'female' and not self.is_pregnant # Age 1 to 6 years

    def age_one_week(self) -> None:
        """
        Simulate the rabbit aging by one week.

        Returns:
        - None
        """
        self.age += 1 # increment the age of the rabbit
        if self.is_pregnant:
            self.weeks_pregnant += 1 # increment the number of weeks the rabbit has been pregnant
            if self.weeks_pregnant == 4: # 4 weeks of pregnancy
                self.is_pregnant = False # reset the pregnancy status
                self.weeks_pregnant = 0 # reset the number of weeks the rabbit has been pregnant
