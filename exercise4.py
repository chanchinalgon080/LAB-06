import random
from collections import deque
import time

class Vehicle:
    def __init__(self, id, arrival_time):
        self.id = id
        self.arrival_time = arrival_time

    def __str__(self):
        return f"Car-{self.id}"

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = deque(maxlen=capacity)

    def enqueue(self, vehicle):
        if len(self.queue) < self.capacity:
            self.queue.append(vehicle)
            return True
        return False

    def dequeue(self):
        return self.queue.popleft() if not self.is_empty() else None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __str__(self):
        return "[" + ", ".join(str(v) for v in self.queue) + "]"

class TrafficLightSimulation:
    def __init__(self, sim_time=60, cycle_length=10, arrival_probability=0.7):
        self.sim_time = sim_time
        self.cycle_length = cycle_length
        self.arrival_probability = arrival_probability
        self.queues = {
            'NS': CircularQueue(10),
            'EW': CircularQueue(10)
        }
        self.current_light = 'NS'
        self.vehicle_id = 0
        self.time = 0
        self.wait_times = []
        self.max_queue_lengths = {'NS': 0, 'EW': 0}

    def run(self):
        while self.time < self.sim_time:
            if random.random() < self.arrival_probability:
                direction = random.choice(['NS', 'EW'])
                vehicle = Vehicle(self.vehicle_id, self.time)
                added = self.queues[direction].enqueue(vehicle)
                if added:
                    print(f"[{self.time}s] {vehicle} arrived at {direction} light")
                    self.vehicle_id += 1

            car = self.queues[self.current_light].dequeue()
            if car:
                wait = self.time - car.arrival_time
                self.wait_times.append(wait)
                print(f"[{self.time}s] {car} passed through {self.current_light} (waited {wait}s)")

            if self.time % self.cycle_length == 0:
                self.current_light = 'EW' if self.current_light == 'NS' else 'NS'
                print(f"[{self.time}s] Light switched to {self.current_light}")

            for dir in ['NS', 'EW']:
                self.max_queue_lengths[dir] = max(self.max_queue_lengths[dir], self.queues[dir].size())

            self.time += 1
            time.sleep(0.1)  # puedes comentar esta línea si quieres ejecución rápida

        self.print_summary()

    def print_summary(self):
        avg_wait = sum(self.wait_times) / len(self.wait_times) if self.wait_times else 0
        print("\n--- Simulation Summary ---")
        print(f"Total vehicles passed: {len(self.wait_times)}")
        print(f"Average wait time: {avg_wait:.2f}s")
        print(f"Max queue length NS: {self.max_queue_lengths['NS']}")
        print(f"Max queue length EW: {self.max_queue_lengths['EW']}")

# ----------------------------
# Test Cases
# ----------------------------

def test_case_normal():
    print("\n=== Test Case 1: Comportamiento normal ===")
    sim = TrafficLightSimulation(sim_time=30, cycle_length=10, arrival_probability=0.7)
    sim.run()

def test_case_high_traffic():
    print("\n=== Test Case 2: Alta congestión ===")
    sim = TrafficLightSimulation(sim_time=30, cycle_length=10, arrival_probability=1.0)
    sim.run()

def test_case_no_traffic():
    print("\n=== Test Case 3: Sin tráfico ===")
    sim = TrafficLightSimulation(sim_time=30, cycle_length=10, arrival_probability=0.0)
    sim.run()

# Ejecutar todos los casos de prueba
if __name__ == "__main__":
    test_case_normal()
    test_case_high_traffic()
    test_case_no_traffic()
