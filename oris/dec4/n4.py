import threading
from queue import Queue

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def thread_func(input_queue):
    while not input_queue.empty():
        number = input_queue.get()
        result = factorial(number)
        results.append((number, result))


num_threads = int(input("Введите количество потоков: "))
threads = []
results = []

for x in range(num_threads):
    numbers = list(map(int, input("Введите числа: ").split()))
    input_queue = Queue()

    for number in numbers:
        input_queue.put(number)

    thread = threading.Thread(target=thread_func, args=(input_queue, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for number, result in results:
    print(f"Факториал числа {number}: {result}")





