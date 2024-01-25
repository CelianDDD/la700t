from rabbit import Rabbit # Import the Rabbit class from the rabbit.py file
from fox import Fox # Import the Fox class from the fox.py file
from carrot import Carrot # Import the Carrot class from the carrot.py file
import matplotlib.pyplot as plt # Import the matplotlib.pyplot module to plot the population and carrot quantity evolution over time
import random # Import the random module to generate random numbers
import os # Import the os module to create the 'recap' folder if it doesn't already exist

class Garden:
    def __init__(self):
        """
        Initialize the Garden with initial values.

        Attributes:
        - rabbits: List of Rabbit objects in the garden.
        - carrots: Carrot object representing the quantity of carrots in the garden.
        - fox: Fox object representing the presence of a fox in the garden.
        - population_history: Dictionary to store the population and carrot quantity history.

        """
        self.rabbits = [] # List of Rabbit objects in the garden
        self.carrots = Carrot(200) # Carrot object representing the quantity of carrots in the garden
        self.fox = Fox() # Fox object representing the presence of a fox in the garden
        self.population_history = {'rabbits': [], 'carrots': [], 'fox_eaten': []} # Dictionary to store the population and carrot quantity history
        self.total_births = 0 # Total number of rabbit births
        self.total_deaths = 0 # Total number of rabbit deaths

    def add_rabbit(self, rabbit):
        """
        Add a Rabbit object to the garden.

        Parameters:
        - rabbit: Rabbit object to be added to the garden.

        """
        self.rabbits.append(rabbit) # Add the rabbit to the list of rabbits

    def reproduce(self, female_rabbit, male_rabbit):
        """
        Reproduce new rabbits based on the given female and male rabbits.

        Parameters:
        - female_rabbit: Rabbit object representing the female rabbit.
        - male_rabbit: Rabbit object representing the male rabbit.

        Returns:
        - List of new Rabbit objects representing the offspring.

        """
        new_rabbits = []
        female_rabbit.is_pregnant = True 
        for _ in range(random.randint(0, 6)): # 0 to 6 babies
            gender = 'female' if random.random() < 0.5 else 'male' # random gender
            new_rabbit = Rabbit(0, gender) # new rabbit
            new_rabbit.has_born = True
            new_rabbits.append(new_rabbit) # add new rabbit to list of new rabbits
            self.total_births += 1 # increment total births
        return new_rabbits # return list of new rabbits


    def rabbit_has_died(self, rabbit):
        """
        Check if a given rabbit has died based on certain conditions.

        Parameters:
        - rabbit: Rabbit object to check for death.

        Returns:
        - True if the rabbit has died, False otherwise.

        """
        if rabbit.weeks_since_last_meal > 2:
            self.total_deaths += 1 # increment total deaths
            return True # Rabbit has died
        elif rabbit.age >= 312: # 6 years
            self.total_deaths += 1 # increment total deaths
            return True # Rabbit has died
        elif rabbit.age >= 208 and random.random() < 0.5: # 4 years
            self.total_deaths += 1 # increment total deaths
            return True # Rabbit has died
        elif rabbit.eaten_by_fox:
            self.total_deaths += 1 # increment total deaths
            return True # Rabbit has died
        else:
            return False # Rabbit has not died


    def simulate(self, years):
        """
        Simulate the evolution of the garden over a specified number of years.

        Parameters:
        - years: Number of years to simulate.

        """
        print("------------------")
        for year in range(years):
            print("Year {}".format(year + 1)) # Print the current year
            print("Carrots: {}".format(self.carrots.quantity)) # Print the current carrot quantity

            for week in range(52):
                # Carrots replenished every June
                if week == 24:
                    self.carrots.quantity += 400 # 400 carrots added in June
                    self.carrots.update_history() # Update the carrot quantity history

                # Feed and age the rabbits
                for rabbit in self.rabbits:
                    rabbit.age_one_week() # Simulate aging by one week
                    rabbit.eat(self.carrots)  # Simulate eating once a week

                # Fox behavior
                if len(self.rabbits) > 10 and random.random() < 0.9:
                    rabbit_to_eat = random.choice(self.rabbits) # Choose a random rabbit to eat
                    self.fox.eat_rabbit(rabbit_to_eat) # Simulate the fox eating the rabbit

                # Reproduction
                if week == 13 or week == 26:
                    female_rabbits = [rabbit for rabbit in self.rabbits if rabbit.can_reproduce() and rabbit.gender == 'female'] 
                    male_rabbits = [rabbit for rabbit in self.rabbits if rabbit.gender == 'male']
                    if len(female_rabbits) >= 1 and len(male_rabbits) >= 1: 
                        for female_rabbit in female_rabbits:
                            if len(male_rabbits) > 0:
                                male_rabbit = random.choice(male_rabbits) 
                                new_rabbits = self.reproduce(female_rabbit, male_rabbit)
                                self.rabbits.extend(new_rabbits)

                self.rabbits = [rabbit for rabbit in self.rabbits if not self.rabbit_has_died(rabbit)] # Remove dead rabbits

                # Update population history
                self.population_history['rabbits'].append(len(self.rabbits)) # Add the current rabbit population to the population history
                self.population_history['carrots'].append(self.carrots.quantity) # Add the current carrot quantity to the population history
                self.population_history['fox_eaten'].append(self.fox.rabbits_eaten) # Add the current number of rabbits eaten by the fox to the population history

            print("Rabbits: {}".format(len(self.rabbits))) # Print the current rabbit population
            print("Eaten by fox: {}".format(self.fox.rabbits_eaten)) # Print the number of rabbits eaten by the fox
            print("------------------")

    def plot_population_history(self):
        """
        Plot the population and carrot quantity evolution over time.

        """
        plt.figure(figsize=(10, 6)) # Set the figure size
        plt.plot(range(len(self.population_history['rabbits'])), self.population_history['rabbits'], color='blue', label='Population de lapins') # Plot the rabbit population
        plt.plot(range(len(self.population_history['carrots'])), self.population_history['carrots'], color='green', label='Quantité de carottes') # Plot the carrot quantity
        plt.plot(range(len(self.population_history['fox_eaten'])), self.population_history['fox_eaten'], color='red', label='Lapins mangés par le renard', linestyle='dotted') # Plot the number of rabbits eaten by the fox
        plt.xlabel('Semaines') # Set the x-axis label
        plt.ylabel('Population / Quantité') # Set the y-axis label
        plt.title('Évolution de la population et de la quantité de carottes au fil du temps') # Set the title
        plt.legend() # Show the legend
        plt.show() # Show the plot


    def generate_summary(self):
        """
        Generate a summary of the simulation results.

        Returns:
        dict: A dictionary containing the following information:
            - 'total_deaths': Total number of rabbit deaths.
            - 'total_births': Total number of rabbit births.
            - 'total_carrots': List of carrot quantities over time.
            - 'fox_meals': Total number of rabbits eaten by the fox.

        The summary is also written to a text file in the 'recap' folder.
        """
        summary = {
            'total_deaths': self.total_deaths, # Total number of rabbit deaths
            'total_births': self.total_births, # Total number of rabbit births
            'total_carrots': self.carrots.quantity_history, # List of carrot quantities over time
            'fox_meals': self.fox.rabbits_eaten # Total number of rabbits eaten by the fox
        }
        
        # Convert the dictionary into a string to write it to the file
        summary_str = '\n'.join([f'{key}: {value}' for key, value in summary.items()]) # Convert the dictionary into a string to write it to the file

        # Create the 'recap' folder if it doesn't already exist
        if not os.path.exists('recap'): # Create the 'recap' folder if it doesn't already exist
            os.mkdir('recap') # Create the 'recap' folder

        # Write the summary to a text file
        with open('recap/summary.txt', 'w') as file: # Write the summary to a text file
            file.write(summary_str) # Write the summary to the text file