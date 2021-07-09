class Pet:
  age = 0
  hunger = 0
  fitness = 10

  growUpEffect = {
    'age': +1,
    'hunger': +5,
    'fitness': -3
  }

  walkEffect = {
    'fitness': +4
  }

  feedEffect = {
    'hunger': -3
  }

  minHunger = 0
  maxFitness = 10

  feedTrigger = 4
  walkTrigger = 4

  death = {
    'age': 30,
    'hunger': 10,
    'fitness': 0
  }

  messages = {
    'fitness': 'I need a walk',
    'hunger': 'I am hungry',
    'fitnessAndHunger': 'I am hungry AND I need a walk',
    'death': 'Your pet has kicked the bucket',
    'default': 'I feel great'
  }

  def __init__(self, name = "Dave"):
    self.name = name

  @property
  def isAlive(self):
    return self.age < self.death['age'] and self.hunger < self.death['hunger'] and self.fitness > self.death['fitness']

  def growUp(self):
    if not self.isAlive: raise ValueError(self.messages['death'])
    self.age += self.growUpEffect['age']
    self.hunger += self.growUpEffect['hunger']
    self.fitness += self.growUpEffect['fitness']

  def walk(self):
    if not self.isAlive: raise ValueError(self.messages['death'])
    self.fitness += self.walkEffect['fitness']
    if self.fitness > self.maxFitness: self.fitness = self.maxFitness

  def feed(self):
    if not self.isAlive: raise ValueError(self.messages['death'])
    self.hunger += self.feedEffect['hunger']
    if self.hunger < self.minHunger: self.hunger = self.minHunger

  def checkUp(self):
    print(
      self.age,
      self.hunger,
      self.fitness
    )
    if not self.isAlive: return self.messages['death']
    if self.fitness < self.walkTrigger and self.hunger > self.feedTrigger: return self.messages['fitnessAndHunger']
    if self.fitness < self.walkTrigger: return self.messages['fitness']
    if self.hunger > self.feedTrigger: return self.messages['hunger']
    return self.messages['default']
