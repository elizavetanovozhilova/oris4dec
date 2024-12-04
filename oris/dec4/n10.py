import threading
import time
import random

class Parking:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.semaphore = threading.Semaphore(total_spots)
        self.lock = threading.Lock()
        self.current_cars = 0

    def park(self, car_id):
        with self.semaphore:
            with self.lock:
                self.current_cars += 1
                print(f"Автомобиль {car_id} заехал на парковку. Занятых мест: {self.current_cars}/{self.total_spots}")

            parking_time = random.randint(1, 5)
            time.sleep(parking_time)

            with self.lock:
                self.current_cars -= 1
                print(f"Автомобиль {car_id} уехал с парковки. Занятых мест: {self.current_cars}/{self.total_spots}")


def simulate_parking(total_spots, num_cars):
    parking = Parking(total_spots)
    threads = []

    for car_id in range(1, num_cars + 1):
        thread = threading.Thread(target=parking.park, args=(car_id,))
        threads.append(thread)
        thread.start()
        time.sleep(random.uniform(0.1, 1))

    for thread in threads:
        thread.join()


total_parking_spots = 5
total_cars = 10
simulate_parking(total_parking_spots, total_cars)
