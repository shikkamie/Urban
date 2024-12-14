from random import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER_ = 0
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self._speed = speed

    def move(self, dx, dy, dz):
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z
    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER_ <=5:
            print("Я не могу атаковать")
        elif self._DEGREE_OF_DANGER_ >=5:
            print("Я злой, я атакую тебя")

    def speak(self):
        print(self.sound)

    def __str__(self):
        return "Животное"



class Bird(Animal):
    beak = True
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Чирик"
    def __str__(self):
        return "Птица"
    def __repr__(self):
        return "Птица"
    def lay_eggs(self):
        print(f"Птица отложила {round(random() * 10)} яиц")


class AquaticAnimal(Animal):
    def __dir__(self):
        super()._DEGREE_OF_DANGER_ = 3
    def dive_in(self, dz):



bird = Bird(15)

print(bird.lay_eggs())