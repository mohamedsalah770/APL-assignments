import dis
def square(x):
    return x * x
# dis.dis(square) 
def multiply(a, b):
    return a * b
# dis.dis(multiply)
data = 10
print(type(data))

data = [1, 2, 3]
print(type(data))

def my_func(): pass
data = my_func
print(type(data))
import ast

code = "y = (4 * 5) - 3"
tree = ast.parse(code)
print(ast.dump(tree, indent=4))

my_list = [10, 20, 30]
print(id(my_list))
 
my_list.append(40)
print(id(my_list))
