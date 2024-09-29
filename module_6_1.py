class Animal:
    def eat(self,food):
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")
            
class Plant:
    pass
class Mammal(Animal):
    def __init__(self,nam):
        self.name = nam
        self.fed = False
class Predator(Animal):
    def __init__(self,man):
        self.name = man
        self.alive = True
class Flower(Plant):
    def __init__(self,poo):
        self.name = poo
        self.edible = False
class Fruit(Plant):
    def __init__(self,oop):
        self.name = oop
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
