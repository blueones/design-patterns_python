class Move:
    def __init__(self):
        pass
    def move(self):
        pass
class Fly(Move):
    def move(self):
        print("fly with wings")
class Swim(Move):
    def move(self):
        print("swim with tails")
class Run(Move):
    def move(self):
        print("run with legs")


class Eat:
    def __init__(self):
        pass
    def eat(self):
        pass
class EatGrass(Eat):
    def eat(self):
        print("eat grass")
class EatFish(Eat):
    def eat(self):
        print("eat fish")
class EatMeat(Eat):
    def eat(self):
        print("eat other meaty mammals")


class Mammal:
    def __init__(self, eatingbehavior, movingbehavior):
        self.movingbehavior = movingbehavior
        self.eatingbehavior = eatingbehavior
    def eat_mammal(self):
        self.eatingbehavior().eat()
    def move_mammal(self):
        self.movingbehavior().move()
    def set_eating(self, eatingbehavior):
        self.eatingbehavior = eatingbehavior
    def set_moving(self, movingbehavior):
        self.movingbehavior = movingbehavior
whale = Mammal(EatFish, Swim)
whale.eat_mammal()
whale.set_eating(EatMeat)
whale.eat_mammal()