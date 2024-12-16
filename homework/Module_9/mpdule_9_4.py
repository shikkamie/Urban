first = 'Мама мыла раму'

second = 'Рамена мало было'
res = list(map(lambda x,y: x == y, first, second))

def get_advanced_writer(file_name):


    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as f:
            for data in data_set:
                f.write(f"{data}\n")
    return write_everything
write = get_advanced_writer('./test_files_txt/test.txt')

write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

print(write)
class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        import random
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())

print(first_ball())

print(first_ball())
print(first_ball())