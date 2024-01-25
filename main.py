from rabbit import Rabbit # import Rabbit class from rabbit.py
from garden import Garden # import Garden class from garden.py

if __name__ == '__main__':
    # Initialize Garden 
    garden = Garden()

    # Add initial rabbits
    initial_rabbit1 = Rabbit(0, 'male') # 1 rabbit male, 0 month old
    initial_rabbit2 = Rabbit(0, 'female') # 1 rabbit female, 0 month old

    # Add rabbits to garden
    garden.add_rabbit(initial_rabbit1) 
    garden.add_rabbit(initial_rabbit2) 

    # Simulate for 6 years
    garden.simulate(6) 

    # Générer le récapitulatif
    garden.generate_summary()

    # Plot the population evolution
    garden.plot_population_history() 