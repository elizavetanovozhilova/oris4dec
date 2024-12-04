import threading
import time
import random

class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def withdraw(self, client_id, amount):
        with self.condition:
            while amount > self.balance:
                print(f"Клиент {client_id} пытается снять {amount}. Недостаточно средств. Ожидание...")
                self.condition.wait()

            self.balance -= amount
            print(f"Клиент {client_id} снял {amount}. Остаток на счете: {self.balance}.")

            self.condition.notify_all()



def client(bank, client_id):
    for i in range(3):
        amount = random.randint(50, 150)
        bank.withdraw(client_id, amount)
        time.sleep(1)


balance = 500
bank = Bank(balance)

threads = []
clients = int(input('Введите количество клиентов: '))

for i in range(clients):
    thread = threading.Thread(target=client, args=(bank, i + 1))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
