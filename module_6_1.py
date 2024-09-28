class Animal():
    alive = True
    fed = False
    name = "Animal"
class Plant():
    edible = False
    name = "Plant"
class Mammal(Animal):
    def eat(self,food):
        if food.edible():
            self.fed = True
            return "f{self.name} съел {food.name}"
        else:
            self.alive = False
            return "f{self.name} не стал есть {food.name}"
class Flower(Plant):
    self.name = "Flower"
class Fruit(Plant):
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
