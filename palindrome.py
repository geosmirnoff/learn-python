def is_pal(x):
    pal = False
    num = str(x)
    arr = []

    for char in num:
        arr.append(char)

    arr2 = []
    index = -1

    while index >= -len(arr):
        arr2.append(arr[index])
        index -= 1

    if arr == arr2:
        pal = True

    return pal

x = 100
pal = 0

while x <= 999:
    y = 100
    while y <= 999:
        number = x * y
        y += 1
        ispal = is_pal(number)
        
        if ispal == True:
            pal = number
    x += 1

print(pal)
