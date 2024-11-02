class Vehicle:
    __COLOR_VARIANTS = ["BLACK","WHITE"]

    def __init__(self,v_name,v_mod,v_col,v_p):
        self.__owner = v_name
        self.__model = v_mod
        self.__engine_horsepower = v_p
        self.__color = v_col

    def get_model(self):
        return f"Модель: {self.__model}"
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_horsepower}"
    def get_color(self):
        return f"Цвет: {self.__color}"
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")


    def set_color(self,new_color):
        __vehicle_has_authentic_color = True
        for cl in self._Vehicle__COLOR_VARIANTS:
            if cl.upper() == new_color.upper():
                self.__color = new_color.upper()
                __vehicle_has_authentic_color = False
                break
        if __vehicle_has_authentic_color:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5 # only 5 passengers can be placed in sedan
    def Vehicle.__init__():
        pass

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
