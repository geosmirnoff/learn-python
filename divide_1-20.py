def divide(x):
	divider = 1
	while divider <= 20:
		if x % divider == 0:
			do_divide = True
		else:
			do_divide = False
		if do_divide == False:
			break
		divider += 1
	return do_divide

num = 1

while True:
	min_num = divide(num)
	if min_num == True:
		break
	num += 1

print(num) #232792560
