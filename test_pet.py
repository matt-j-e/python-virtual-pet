import unittest
from pet import Pet


class TestPetSetup(unittest.TestCase):
  """Test case for Pet setup"""

  def setUp(self):
    self.fido = Pet("Fido")

  def test_pet_instatiation(self):
    """Pet object is instantiated"""
    self.assertIsInstance(self.fido, Pet)

  def test_pet_name(self):
    """pet is called Fido"""
    self.assertEqual(self.fido.name, "Fido")

  def test_pet_age(self):
    """pet start age = 0"""
    self.assertEqual(self.fido.age, 0) 

  def test_pet_hunger(self):
    """pet start hunger = 0"""
    self.assertEqual(self.fido.hunger, 0)

  def test_pet_fitness(self):
    """pet start fitness = 10"""
    self.assertEqual(self.fido.fitness, 10)


class TestGrowUp(unittest.TestCase):
  """Test case for Pet's GrowUp method"""
  def setUp(self):
    self.fido = Pet("Fido")
    self.fido.growUp()

  def test_age_increment(self):
    """Pet age = 1 after one growUp()"""
    self.assertEqual(self.fido.age, 1)

  def test_hunger_increment(self):
    """Pet hunger = 5 after one growUp()"""
    self.assertEqual(self.fido.hunger, 5)

  def test_fitness_decrement(self):
    """Pet fitness = 7 after one growUp()"""
    self.assertEqual(self.fido.fitness, 7)

  def test_death_guard_clause(self):
    """Throws an exception if called when the Pet is dead"""
    self.fido.age = 30
    with self.assertRaises(ValueError):
      self.fido.growUp()
  


class TestWalk(unittest.TestCase):
  """Test case for Pet's walk method"""
  def setUp(self):
    self.fido = Pet("Fido")

  def test_fitness_increase(self):
    """Increments Pet fitness by 4 every walk"""
    self.fido.fitness = 3
    self.fido.walk()
    self.assertEqual(self.fido.fitness, 7)

  def test_fitness_maximum(self):
    """Increments Pet fitness to max of 10"""
    self.fido.fitness = 9
    self.fido.walk()
    self.assertEqual(self.fido.fitness, 10)

  def test_death_guard_clause(self):
    """Throws an exception if called when the Pet is dead"""
    self.fido.age = 30
    with self.assertRaises(ValueError):
      self.fido.walk()  


class TestFeed(unittest.TestCase):
  """Test case for Pet's feed method"""
  def setUp(self):
    self.fido = Pet("Fido")

  def test_hunger_decrease(self):
    """Decrease pet hunger by 3 every feed"""
    self.fido.hunger = 6
    self.fido.feed()
    self.assertEqual(self.fido.hunger, 3)

  def test_fitness_maximum(self):
    """Decrease pet hunger to a minimum of 0"""
    self.fido.hunger = 2
    self.fido.feed()
    self.assertEqual(self.fido.hunger, 0)

  def test_death_guard_clause(self):
    """Throws an exception if called when the Pet is dead"""
    self.fido.age = 30
    with self.assertRaises(ValueError):
      self.fido.feed()


class TestCheckup(unittest.TestCase):
  """Test case for pet's checkUp() method"""
  def setUp(self):
    self.fido = Pet("Fido")

  def test_need_a_walk(self):
    """Returns I need a walk where fitness > walk trigger"""
    self.fido.fitness = self.fido.walkTrigger - 1
    self.assertEqual(self.fido.checkUp(), "I need a walk")

  def test_i_am_hungry(self):
    """Returns I am hungry where hunger > feed trigger"""
    self.fido.hunger = self.fido.feedTrigger + 1
    self.assertEqual(self.fido.checkUp(), "I am hungry")

  def test_hungry_and_need_a_walk(self):
    """Returns I am hungry AND I need a walk where 
    hunger > feed trigger and fitness < walk trigger"""
    self.fido.fitness = self.fido.walkTrigger - 1
    self.fido.hunger = self.fido.feedTrigger + 1
    self.assertEqual(self.fido.checkUp(), "I am hungry AND I need a walk")

  def test_kicked_the_bucket(self):
    """Returns kicked the bucket message when not alive"""
    self.fido.growUp()
    self.fido.growUp()
    self.assertEqual(self.fido.checkUp(), "Your pet has kicked the bucket")


class TestIsAlive(unittest.TestCase):
  """Test case for isAlive @property"""
  def setUp(self):
    self.fido = Pet("Fido")

  def test_is_alive(self):
    """Returns True when none of the death triggers reached"""
    self.assertEqual(self.fido.isAlive, True)

  def test_is_dead_from_hunger(self):
    """Returns False when hunger trigger reached"""
    self.fido.hunger = self.fido.death['hunger']
    self.assertEqual(self.fido.isAlive, False)

  def test_is_dead_from_unfitness(self):
    """Returns False when fitness trigger reached"""
    self.fido.fitness = self.fido.death['fitness']
    self.assertEqual(self.fido.isAlive, False)

  def test_is_dead_from_old_age(self):
    """Returns False when age trigger reached"""
    self.fido.age = self.fido.death['age']
    self.assertEqual(self.fido.isAlive, False)


if __name__ == '__main__':
  unittest.main()