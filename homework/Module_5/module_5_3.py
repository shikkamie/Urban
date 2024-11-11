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

	def __eq__(self, other):
		return self.number_of_flors == other

	def __lt__(self, other):
		return self.number_of_flors < other.number_of_flors
	def __gt__(self, other):
		return self.number_of_flors > other.number_of_flors
	def __le__(self, other):
		return self.number_of_flors <= other.number_of_flors
	def __ge__(self, other):
		return self.number_of_flors >= other.number_of_flors
	def __ne__(self, other):
		return self.number_of_flors != other.number_of_flors

	def __add__(self, value):
		self.number_of_flors = self.number_of_flors + value
		return self
	def __radd__(self, value):
		self.number_of_flors = value + self.number_of_flors
		return self
	def __iadd__(self, value):
		self.number_of_flors += value
		return self


h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)



print(h1)

print(h2)



print(h1 == h2) # __eq__



h1 = h1 + 10 # __add__

print(h1)

print(h1 == h2)



h1 += 10 # __iadd__

print(h1)



h2 = 10 + h2 # __radd__

print(h2)



print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__