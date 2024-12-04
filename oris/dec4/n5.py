import threading
from heapq import merge
import random

def sort_array(array, result, index):
    result[index] = sorted(array)

def thread_sort(array, num_threads):
    sub_size = len(array) // num_threads
    subarrays = [array[i * sub_size:(i + 1) * sub_size] for i in range(num_threads)]
    if len(array) % num_threads != 0:
        subarrays[-1].extend(array[num_threads * sub_size:])

    result_list = [0] * num_threads

    threads = []
    for index, subarray in enumerate(subarrays):
        thread = threading.Thread(target=sort_array, args=(subarray, result_list, index))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    result = list(merge(*result_list))
    return result

array = [random.randint(1, 100) for i in range(30)]
print("Исходный массив:", array)
num_threads = 4

sorted_array = thread_sort(array, num_threads)
print("Отсортированный массив:", sorted_array)