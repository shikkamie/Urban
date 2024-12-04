import os
import time

for root, dirs, files in os.walk(r"E:\pythonUni\pythonProject\homework/module_7"):
    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file_path)
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_time))
        files_ize = os.stat(file_path).st_size
        parent_dir = os.path.dirname(file_path)
    print(f"Обнаружен файл: {file}, Путь: {file_path}, Размер: {files_ize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}")
