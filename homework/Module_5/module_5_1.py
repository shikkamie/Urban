class House:
	def __init__(self, name, number_of_flors):
		self.name = name
		self.number_of_flors = number_of_flors
	def go_to(self, new_floor):
		if 1 > new_floor or new_floor > self.number_of_flors:
			print(f"Такого этажа не существует")
		else:
			print(f"Гость перешел на этаж {new_floor}")

h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(10)

h2.go_to(2)