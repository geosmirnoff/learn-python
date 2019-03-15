#сумма всех четных элементов ряда Фибоначчи, которые <= 4M

row = [1, 2]
summ = 0

while row[-1] < 4000000:
    last = row[-1] + row[-2]
    row.append(last)

for item in row:
    if item % 2 == 0 and item != row[-1]:
        summ += item
print(row)
print("Cумма всех четных элементов ряда Фибоначчи больше 4 000 000:")
print(summ)
