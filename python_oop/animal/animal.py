class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def display_info(self):
        print "Animal name is ", self.name
        print "Health is ", self.health
        return self

    def walk(self):
        print "Walking ", self.name
        self.health -= 1
        print "Health is now", self.health
        return self 

    def run(self):
        print self.name, "is going for a run"
        self.health -= 5
        print "Health is now ", self.health
        return self     

class Dog(animal):
    def __init__(self, name, health): 
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        print "Petting the dog"
        self.health += 5
        print "Health is now ", self.health
        return self
class Dragon(animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170

    def fly(self):
        print "flying the dragon"
        self.health -= 5
        print "Health is now ", self.health
        return self

    def display_info(self):
        print "I am a Dragon"
        super(Dragon,self).display_info()
        return self

Walrus = animal("walrus", 500)

#Walrus.walk().walk().walk().run().run().display_info()

Poodle = Dog("poodle", 300)

#Poodle.walk().walk().walk().run().run().pet().display_info()

Charizard = Dragon("charizard", 1000)

Charizard.display_info().fly().walk()
