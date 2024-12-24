import time
import threading as tr

def wite_words(word_count, file_name):
    start_time = time.time()
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(word_count):
            f.write(f"Какое-то слово №{i}\n")
            time.sleep(0.1)
    end_time = time.time()
    res_time = end_time - start_time

    print(f"Сохранено в файл {file_name}. Выполнили за {res_time:.2f} секунд")


wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

thread_start_time = time.time()
threads = [tr.Thread(target=wite_words, args=(10, 'example5.txt')),
           tr.Thread(target=wite_words, args=(30, 'example6.txt')),
           tr.Thread(target=wite_words, args=(200, 'example7.txt')),
           tr.Thread(target=wite_words, args=(100, 'example8.txt'))]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

thread_end_time = time.time() - thread_start_time
print(f"Общее время выполнения потоков: {thread_end_time - thread_start_time:.2f} секунд")