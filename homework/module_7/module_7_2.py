def custom_write(file_name, strings):
    strings_positions = {}
    line_number = 1  # Инициализация счетчика строк

    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            byte_position = file.tell()  # Получаем текущую позицию в байтах
            file.write(string + '\n')  # Записываем строку в файл
            strings_positions[(line_number, byte_position)] = string  # Сохраняем в словарь
            line_number += 1  # Увеличиваем номер строки

    return strings_positions

info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]



result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)