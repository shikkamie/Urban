class House:
	def __init__(self, name, number_of_flors):
		self.name = name
		self.number_of_flors = number_of_flors
	def go_to(self, new_floor):
		if 1 > new_floor or new_floor > self.number_of_flors:
			print(f"Такого этажа не существует")
		else:
			print(f"Гость перешел на этаж {new_floor}")

	def __len__(self):
		return self.number_of_flors
	def __str__(self):
		return f"Название: {self.name}, кол-во этажей: {self.number_of_flors}"

h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__

print(len(h1))

print(len(h2))