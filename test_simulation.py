import unittest
from rabbit import Rabbit
from garden import Garden
from carrot import Carrot

class TestRabbit(unittest.TestCase):
    def test_rabbit_eat(self):
        """Test the Rabbit's eat method."""
        rabbit = Rabbit(1, 'female')
        carrot = Carrot(5)

        rabbit.eat(carrot) # rabbit eats carrot
        self.assertEqual(rabbit.weeks_since_last_meal, 0) # rabbit has eaten
        self.assertEqual(carrot.quantity, 4) # carrot quantity has decreased

    def test_rabbit_can_reproduce(self):
        """Test the Rabbit's can_reproduce method."""
        young_female_rabbit = Rabbit(52, 'female') # 1 year old female
        old_female_rabbit = Rabbit(313, 'female') # 6 years old female
        male_rabbit = Rabbit(80, 'male') # 1.5 years old male

        self.assertTrue(young_female_rabbit.can_reproduce()) # True if they can reproduce
        self.assertFalse(old_female_rabbit.can_reproduce()) # False if they can't reproduce
        self.assertFalse(male_rabbit.can_reproduce()) # False if they can't reproduce

    def test_rabbit_age_one_week(self):
        """Test the Rabbit's age_one_week method."""
        rabbit = Rabbit(52, 'female') 
        rabbit.is_pregnant = True # rabbit is pregnant
        rabbit.weeks_pregnant = 3 # rabbit has been pregnant for 3 weeks

        rabbit.age_one_week() # rabbit ages one week
        self.assertEqual(rabbit.age, 53) # rabbit age has increased
 
class TestGarden(unittest.TestCase):
    def test_garden_add_rabbit(self):
        """Test the Garden's add_rabbit method."""
        garden = Garden() # create a new garden
        rabbit = Rabbit(1, 'male') # create a new rabbit

        garden.add_rabbit(rabbit) # add rabbit to garden
        self.assertIn(rabbit, garden.rabbits) # rabbit is in garden

    def test_garden_reproduce(self):
        """Test the Garden's reproduce method."""
        garden = Garden() # create a new garden
        female_rabbit = Rabbit(52, 'female') 
        male_rabbit = Rabbit(60, 'male') 

        new_rabbits = garden.reproduce(female_rabbit, male_rabbit) # reproduce rabbits
        self.assertTrue(all(isinstance(rabbit, Rabbit) for rabbit in new_rabbits)) # new rabbits are rabbits

    def test_garden_rabbit_has_died(self):
        """Test the Garden's rabbit_has_died method."""
        garden = Garden() # create a new garden
        starved_rabbit = Rabbit(1, 'male') 
        old_rabbit = Rabbit(312, 'female')
        fox_eaten_rabbit = Rabbit(100, 'female')

        starved_rabbit.weeks_since_last_meal = 3 # hasn't eaten in 3 weeks
        old_rabbit.age = 320 # 6 years old
        fox_eaten_rabbit.eaten_by_fox = True # eaten by fox

        self.assertTrue(garden.rabbit_has_died(starved_rabbit)) # rabbit has died
        self.assertTrue(garden.rabbit_has_died(old_rabbit)) # rabbit has died
        self.assertTrue(garden.rabbit_has_died(fox_eaten_rabbit)) # rabbit has died

    def test_garden_simulate(self):
        """Test the Garden's simulate method."""
        garden = Garden()
        initial_rabbit = Rabbit(0, 'male')  
        garden.add_rabbit(initial_rabbit) # add initial rabbit to garden

        self.assertEqual(len(garden.rabbits), 1) # 1 rabbit in garden
        self.assertEqual(garden.carrots.quantity, 200) # 200 carrots in garden

        garden.simulate(1) # simulate for 1 year

        self.assertGreaterEqual(len(garden.rabbits), 0) # at least 0 rabbits in garden
        self.assertGreaterEqual(garden.carrots.quantity, 0) # at least 0 carrots in garden

if __name__ == '__main__':
    unittest.main() # run unit tests
