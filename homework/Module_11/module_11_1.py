
import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data


if __name__ == "__main__":
    file_names = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']

    start_time = time.time()
    for file_name in file_names:
        data = read_info(file_name)
        print(f"Содержимое {file_name}: {data}")
    linear_time = time.time() - start_time
    print(f"Время выполнения линейного считывания: {linear_time:.2f} секунд")

    start_time = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(read_info, file_names)

    for file_name, data in zip(file_names, results):
        print(f"Содержимое {file_name}: {data}")
    parallel_time = time.time() - start_time
    print(f"Время выполнения многопроцессного считывания: {parallel_time:.2f} секунд")
