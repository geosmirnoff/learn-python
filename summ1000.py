#Сумма всех чисел меньше 1000, кратных 3 или 5

count = 3
summ = 0

while count < 1000:
    if count % 3 == 0 or count % 5 == 0:
        summ += count
        count += 1
    else:
        count += 1
print("Сумма всех чисел меньше 1000, кратных 3 или 5, равна", summ)
