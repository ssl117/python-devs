def factorial(num):
	arr = [x for x in range(1,num+1)]
	cant = len(arr)
	result = 1
	for k in range(cant):
		last = arr.pop()
		result = result * last
	return result

print(factorial(13))

a = int(3 *2 / 11)

print(a)


