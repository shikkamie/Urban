class Vehicle:
    __COLOR_VARIANTS= ['red', 'green', 'blue']
    def __init__(self, owner, model, color, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        print(f"Модель: {self.__model}")
    def get_engine_power(self):
        print(f"Мощность двигателя: {self.__engine_power}")
    def get_color(self):
        print(f"Цвет: {self.__color}")
    def print_info(self):
        self.get_model()
        self.get_engine_power()
        self.get_color()
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)



# Изначальные свойства

vehicle1.print_info()



# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')

vehicle1.set_color('blue')

vehicle1.owner = 'Vasyok'



# Проверяем что поменялось

vehicle1.print_info()