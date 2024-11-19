


class Animal:
	alived = True # Живой
	fed = False # Накормленный
	def __init__(self, name):
		self.name = name

	def eat(self, food):
		if not food.edible:
			print(f"{self.name} не стал есть {food.name}")
			self.alived = False
		elif food.edible:
			print(f"{self.name} сьел {food.name}")
			self.fed = True



class Plant:
	edible = False
	def __init__(self, name):
		self.name = name

class Mammal(Animal):
	pass

class Predator(Animal):
	pass

class Flower(Plant):
	pass

class Fruit(Plant):
	edible = True


a1 = Predator('Волк с Уолл-Стрит')

a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')



print(a1.name)

print(p1.name)



print(a1.alived)

print(a2.fed)

a1.eat(p1)

a2.eat(p2)

print(f"живой {a1.name}: {a1.alived} ")

print(f"{a2.name} сытый: {a2.fed}")
