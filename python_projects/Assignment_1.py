products = [" LAPTOP ", "phone ", " Tablet", "CAMERA "]
print(list(map( lambda p : p.strip().title(), products)))

celsius = [0, 10, 20, 30, 40]
print(list(map(lambda c : (9 / 5) * c + 32 , celsius)))
 
nums = [1, 2, 3, 4, 5]
print(list(map(lambda n : n ** 2 + 10, nums)))
words = ["python", "lambda", "programming", "map", "function"]
print(list(map(lambda w : (w[0] , w[-1]) , words)))

marks = [[47, 84, 74], [95, 63, 105], [92, 80, 97]]

print(list(map(lambda row: list(map(lambda x: round(x * 1.05), row)), marks)))
numbers = [5, 10, 15, 20, 25]

min_val = min(numbers)
max_val = max(numbers)

normalized = list(map(lambda x: (x - min_val) / (max_val - min_val), numbers))

print(normalized)
sentences = ["I love python" , "coding is fun" , "painting is cool"]

res = list(
    map(
        lambda sentence: list(
            map(lambda word: len(word), sentence.split())
        ),
        sentences
    )
)
print(res)
