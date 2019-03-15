#Наибольший простой делитель
def simple(x):
    y = 1
    is_simple = True
    while y != x:
        if x % y != 0 and y != 1:
            is_simple = True
        elif x % y == 0 and y != 1:
            is_simple = False
        if is_simple == False:
            break
        y += 1
    return is_simple

#print(simple(20143))

def divider(x, num):
    is_divider = False
    if num % x == 0:
        is_divider = True
    return is_divider


div = []
count = 1
number = int(input("Введите число: "))

while count < number:
    simp = simple(count)
    if simp == True:
        divide = divider(count, number)
        if divide == True:
            div.append(count)
    count += 1

print(div[-1])
