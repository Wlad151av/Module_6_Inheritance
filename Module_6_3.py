class Horse:
    sound = "Frrr"
    x_distance = 0
    def run(self,dx):
        self.x_distance += dx

class Eagle:
    sound = "I train, eat, sleep, and repeat"
    y_distance = 0
    def fly(self,dy):
        self.y_distance += dy


class Pegasus(Eagle,Horse):
    def __init_(self):
        super().__init__()
    def move(self,dx,dy):
        super().run(dx)
        super().fly(dy)
    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()