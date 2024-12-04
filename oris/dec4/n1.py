import threading

def function():
    print(f"Поток {threading.current_thread().name} запущен")

threads_num = int(input())
threads = []
for i in range(threads_num):
    thread = threading.Thread(target=function, name=f"Thread{i + 1}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
