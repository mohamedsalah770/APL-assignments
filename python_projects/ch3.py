#----------------------
#----  problem 1  -----
#----------------------

# def remove_vowels(str):
#     vowels = "aeiouAEIOU"
#     return "".join([char for char in str if char not in vowels])

###########################################
#----------------------
#----  problem 2  -----
#----------------------

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_nums = filter(lambda x: x % 2 != 0, nums)
# squared_odds = list(map(lambda x: x**2, odd_nums))

###########################################
#----------------------
#----  problem 3  -----
#----------------------

# import functools
# import time

# @functools.lru_cache(maxsize=None)
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# start_time = time.time()
# print(f"Fibonacci(35) = {fibonacci(35)}")
# end_time = time.time()
# print(f"Time taken: {end_time - start_time:.5f} seconds")

###########################################
#----------------------
#----  problem 4  -----
#----------------------

# def make_adder(n):
#     def adder(x):
#         return x + n
#     return adder

###########################################
#----------------------
#----  problem 5  -----
#----------------------

# def apply_twice(func, value):
#     return func(func(value))
# print(apply_twice(lambda x: x + 1, 5))

###########################################
#----------------------
#----  problem 6  -----
#----------------------

# def etl_pipeline(texts):
#     stopwords = {"the", "a", "is", "in", "at", "of", "on", "and", "to", "for"}
#     all_Words = [word.lower() for text in texts for word in text.split()]
#     filtered_Words = filter(lambda word: word and word not in stopwords, all_Words)
    
#     word_Frequencies  = {}
#     for word in filtered_Words:
#         word_Frequencies[word] = word_Frequencies.get(word, 0) + 1
#     return word_Frequencies

###########################################
#----------------------
#----  problem 7  -----
#----------------------

# def my_reduce(func, iterable, initializer=None):
#     iterator = iter(iterable)
#     if initializer is None:
#         try:
#             value = next(iterator)
#         except StopIteration:
#             raise TypeError("Empty sequence with no initial value")
#     else:
#         value = initializer
    
#     for element in iterator:
#         value = func(value, element)
    
#     return value

###########################################
#----------------------
#----  problem 8  -----
#----------------------

# def log_call(func):
#     def nestedFunc(*args, **kwargs):
#         print(f"--- Calling function: {func.__name__} ---")
#         result = func(*args, **kwargs)
#         print(f"--- Finished function: {func.__name__} ---")
#         return result
#     return nestedFunc