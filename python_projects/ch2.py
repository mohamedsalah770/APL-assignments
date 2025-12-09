class Vector3D:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        
        return self.x * other.x + self.y * other.y + self.z * other.z
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
# Test
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
print(f"Add: {v1 + v2}")       
print(f"Sub: {v1 - v2}")       
print(f"Dot: {v1 * v2}")

class Positive:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, owner):
        if instance is None: return self
        return instance.__dict__.get(self.name)
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name} must be non-negative")
        instance.__dict__[self.name] = value
class BankAccount:
    balance = Positive("balance")
    def __init__(self, amount):
        self.balance = amount
# Test
acc = BankAccount(100)
print(acc.balance)
class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Point(10, 20)
import dis
def calculate_sum(a, b):
    return a + b