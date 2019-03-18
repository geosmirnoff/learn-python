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

simples = []
number = 2
while len(simples) <= 10001:
    simp = simple(number)
    
    if simp == True:
        simples.append(number)
    number += 1
    
print(simples[10000]) #104743
