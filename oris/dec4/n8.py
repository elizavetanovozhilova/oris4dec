import os
import threading
from queue import Queue

def search_files(directory, pattern, result_list, lock):
    for root, _, files in os.walk(directory):
        for file in files:
            if pattern in file:
                with lock:
                    result_list.append(os.path.join(root, file))

def worker(task_queue, pattern, result_list, lock):
    while not task_queue.empty():
        directory = task_queue.get()
        try:
            search_files(directory, pattern, result_list, lock)
        finally:
            task_queue.task_done()

def parallel_file_search(directories, pattern, max_threads):
    task_queue = Queue()
    for directory in directories:
        task_queue.put(directory)

    result_list = []
    lock = threading.Lock()

    threads = []
    for _ in range(min(max_threads, len(directories))):
        thread = threading.Thread(target=worker, args=(task_queue, pattern, result_list, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result_list

search_dirs = [
    "/Users/elizavetanovozilova/oris/dec4",
    "/Users/elizavetanovozilova/exam!!!!"
]
search_pattern = ".txt"
max_active_threads = 4

print(f"Ищем файлы с паттерном '{search_pattern}' в директориях: {search_dirs}")
found_files = parallel_file_search(search_dirs, search_pattern, max_active_threads)

print("\nНайденные файлы:")
for file in found_files:
    print(file)