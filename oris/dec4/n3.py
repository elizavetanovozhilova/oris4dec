import threading

def factorial(start, end):
    result = 1
    for x in range(start, end + 1):
        result *= x
    return result

def thread_function(start, end, results, index):
    results[index] = factorial(start, end)

num = int(input())
num_threads = int(input())

step = num // num_threads
threads = []
results = [1] * num_threads

for i in range(num_threads):
    thread_start = 1 + i * step
    thread_end = (i + 1) * step if i < num_threads - 1 else num
    thread = threading.Thread(target=thread_function, args=(thread_start, thread_end, results, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

result = 1
for x in results:
    result *= x

print(f"Факториал числа {num} : {result}")

