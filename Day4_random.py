import random
# import my_module
random_intiger = random.randint(1,5)
print(random_intiger)
# print(my_module.pi)

#random float always between 0.000000 - 0.99999999
random_float = random.random()
print(random_float)
random_decimal = random_float + random_intiger
print(random_decimal)

love_score = random.randint(1,100)
print(f"your love score is {love_score}")