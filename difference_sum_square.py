def sum_of_squares(x):
    count = 1
    summ = 0
    while count <= x:
        summ += count ** 2
        count += 1
    return summ

def square_of_summ(x):
    summ = ((1 + x) / 2) * x
    square = summ ** 2
    return round(square)

summ = sum_of_squares(100)
square = square_of_summ(100)

x = square - summ

print(x)
