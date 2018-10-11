import random

r = random.randint(1,100)
while True:
	num = input('please guess number: ')
	num = int(num)
	if num == r:
		print('猜對了!!')
		break
	elif num > r:
		print('需比答案小')
	elif num < r:
		print('需比答案大')
