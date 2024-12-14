first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


first_result = [x for x in first_strings if len(x) >= 5]

print(f"First result: {first_result}")

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(f"Second result: {second_result}")

third_result = {x: len(x) for x in first_strings + second_strings if len(x) % 2 == 0}

print(f"Third result: {third_result}")

#