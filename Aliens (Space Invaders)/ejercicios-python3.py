word = 'Hello'
arr_word = []
arr_word_final = []

for x in word:
	arr_word.append(x)

length = len(arr_word)

new_word = ''

for k in arr_word:
	new_word = new_word + k
	arr_word_final.append(new_word)

last_word = ''

while length > 1:
	length = len(arr_word)
	if length == 1:
		break
	else:
		arr_word.pop()
		last_word = ''
		for j in arr_word:
			last_word = last_word + j
		arr_word_final.append(last_word)

#print(arr_word_final)

def binary_conversion(num):
	arr_bin_num = []
	cuota = num
	while cuota > 0:
		remainder = cuota % 2
		cuota = int(cuota / 2)
		print(cuota)
		print(remainder)
		arr_bin_num.append(remainder)

	count_ones = 0
	for i in arr_bin_num:
		if i == 1:
			count_ones = count_ones + 1

	return arr_bin_num

#print(binary_conversion(101))


def relation_to_luke(name):
	if name == 'Darth Vader':
		family = 'father.'
	elif name == 'Leia':
		family = 'sister.'
	elif name == 'Han':
		family = 'brother in law.'
	elif name == 'R2D2':
		family = 'droid.'

	return (f'Luke, I am your {family}')

#print(relation_to_luke('Han'))

def number_length(num):
	num_str = str(num)
	arr_num = []
	count = 0
	for x in num_str:
		arr_num.append(x)
		count += 1

	print(arr_num)

	return count

#print(number_length(123456))

import math
def line_length(dot1, dot2):
	x1 = dot1[0]
	x2 = dot1[1]
	y1 = dot2[0]
	y2 = dot2[1]

	distance = math.sqrt( (x1 - y1) ** 2 + (x2 - y2) ** 2 )

	return round(float(distance),2)


def number_split(n):
	if n % 2 == 0:
		num = n / 2
		arr = [int(num), int(num)]

	else:
		num1 = int(n / 2)
		num2 = n - num1
		if n > 0:
			arr = [int(num1), int(num2)]
		else:
			arr = [int(num2), int(num1)]

	return arr

#print(number_split(13))

class Calculator:
	def __init__(num1, num2):
		num1 = num1
		num2 = num2

	def add(num1,num2):
		return num1 + num2

	def subtract(num1,num2):
		return num1 - num2

	def multiply(num1,num2):
		return num1 * num2

	def divide(num1,num2):
		return num1 / num2


print(Calculator.add(2,3))
print(Calculator.subtract(2,3))
print(Calculator.multiply(2,3))
print(Calculator.divide(2,3))