import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end, result):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    result += primes

start = int(input())
end = int(input())
num_threads = int(input())
step = (end - start) // num_threads

threads = []
results = [[] for x in range(num_threads)]

for i in range(num_threads):
    thread_start = start + i * step
    thread_end = start + (i + 1) * step if i < num_threads - 1 else end
    thread = threading.Thread(target=find_primes, args=(thread_start, thread_end, results[i]))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

all_primes = [prime for x in results for prime in x]
print(f"Простые числа в диапазоне от {start} до {end}: {all_primes}")