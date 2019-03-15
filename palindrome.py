def is_pal(x):
    pal = False
    if str(x) == reversed(str(x)):
        pal = True
    return pal

x = 100
y = 100
pal = 0

while x <= 999:
    while y <= 999:
        num = x * y
        y += 1
        ispal = is_pal(num)
        if ispal == True:
            pal = num
    x += 1

print(pal)
