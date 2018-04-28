print("""
        ++++++++++++++++++++++++++
        +                        +
        +   Это бинарный поиск   +
        +                        +
        ++++++++++++++++++++++++++
        """)

import random

my_num = int(input("Введи число от 1 до 100, а прога его угадает: "))

minim = 1
maxim = 100
attempt = 0 #счетчик попыток

scs = random.randint(minim, maxim) #вариант проги

while scs != my_num:
    if my_num < scs:
        maxim = scs - 1
        scs = random.randint(minim, maxim)
        attempt += 1
        print("\nПопытка", str(attempt) + ":", scs)
    elif my_num > scs:
        minim = scs + 1
        scs = random.randint(minim, maxim)
        attempt += 1
        print("\nПопытка", str(attempt) + ":", scs)

print("\nПрога угадала число за", attempt, "попыток")

input("\nЖмякни Enter")
