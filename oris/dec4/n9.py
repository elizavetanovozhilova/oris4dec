import threading
from math import factorial
from scipy.integrate import quad
from queue import Queue

def calculate_factorial(n, result_queue):
    try:
        if n < 0:
            raise ValueError("Факториал определен только для неотрицательных чисел.")
        result = factorial(n)
        result_queue.put((f"Факториал({n})", result))
    except Exception as e:
        result_queue.put((f"Факториал({n})", f"Ошибка: {e}"))

def calculate_power(base, exponent, result_queue):
    try:
        result = base**exponent
        result_queue.put((f"{base} ^ {exponent}", result))
    except Exception as e:
        result_queue.put((f"{base} ^ {exponent}", f"Ошибка: {e}"))

def calculate_integration(func, a, b, result_queue):
    try:
        result, _ = quad(func, a, b)
        result_queue.put((f"Интеграл от {a} до {b}", result))
    except Exception as e:
        result_queue.put((f"Интеграл от {a} до {b}", f"Ошибка: {e}"))

def parallel_calculator(tasks):
    result_queue = Queue()
    threads = []

    for task in tasks:
        task_type, args = task

        if task_type == "factorial":
            thread = threading.Thread(target=calculate_factorial, args=(*args, result_queue))
        elif task_type == "power":
            thread = threading.Thread(target=calculate_power, args=(*args, result_queue))
        elif task_type == "integration":
            thread = threading.Thread(target=calculate_integration, args=(*args, result_queue))
        else:
            raise ValueError(f"Неизвестный тип задачи: {task_type}")

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    return results


tasks = [
    ("factorial", (5,)),
    ("power", (2, 10)),
    ("integration", (lambda x: x**2, 0, 1)),
    ("factorial", (-2,)),
]

results = parallel_calculator(tasks)

print("\nРезультаты вычислений:")
for task_desc, result in results:
    print(f"{task_desc}: {result}")