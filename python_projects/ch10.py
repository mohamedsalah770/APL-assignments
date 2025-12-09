import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        print(f"Execution took {self.end - self.start:.2f} seconds")

with Timer():
    for i in range(1000000):
        pass

def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

for num in even_numbers(10):
    print(num)

def filter_positive():
    while True:
        num = yield
        if num > 0:
            print(f"Positive number: {num}")
co = filter_positive()
next(co)
co.send(-3)
co.send(5)
co.send(0)

class Circle:
    def draw(self):
        return "Drawing a Circle"

class Square:
    def draw(self):
        return "Drawing a Square"

def shape_factory(shape_type):
    if shape_type == "circle":
        return Circle()
    elif shape_type == "square":
        return Square()
    else:
        raise ValueError("Unknown shape")

shape = shape_factory("circle")
print(shape.draw())
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for obs in self.observers:
            obs.update(message)

class Observer:
    def update(self, message):
        print(f"Received update: {message}")

subject = Subject()
obs1 = Observer()
obs2 = Observer()
subject.attach(obs1)
subject.attach(obs2)
subject.notify("Update available!")
