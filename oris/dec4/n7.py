import threading
from collections import Counter

def word_counter(text, result_dict, index):
    words = text.split()
    word_count = Counter(words)
    result_dict[index] = word_count

def split_file(filename, num_parts):
    with open(filename, 'r') as file:
        text = file.read()

        part_size = len(text) // num_parts
        parts = [text[i:i + part_size] for i in range(0, len(text), part_size)]

        if len(text) % num_parts != 0:
            parts[-1] += text[len(parts) * part_size:]

    return parts

filename = 'n7file.txt'
num_threads = int(input("Введите количество потоков: "))

parts = split_file(filename, num_threads)
threads = []
result_dict = {}

for i, part in enumerate(parts):
    thread = threading.Thread(target=word_counter, args=(part, result_dict, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

total_counts = Counter()
for count in result_dict.values():
    total_counts += count

for word, count in total_counts.items():
    print(f"{word}: {count}")
