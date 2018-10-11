import random
start = int(input('請輸入起始數字'))
end = int(input('請輸入結束數字'))
r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('please guess number: ')
	num = int(num)
	if num == r:
		print('猜對了!!')
		print('你總共猜了:', count,'次')
		break
	elif num > r:
		print('需比答案小')
	elif num < r:
		print('需比答案大')
