num = 0
nums = []
while True:#bool_val == False:
	num = input('Enter num (enter \'ok\' to exit): ')
	try:
		if num == 'ok':
			break
		elif float(num) and float(num) not in nums:
			nums.append(float(num))
	except ValueError:
		print('invalid input')
  
operator = input('Enter operator(\'+\', \'-\', \'*\', and \'\\\'): ')
print(f'The numbers you entered are {nums}')
sorted_nums = (sorted(nums, reverse=True))

#different functions for different operators
def multiply(n):
		if n < 0:
			return 1
		return multiply(n-1) * nums[n]

def add(n):
	if n < 0:
		return 0
	return add(n -1) + nums[n]
	
def subtract(n):
	if n < 0:
		return sorted_nums[0] * 2
	return subtract(n - 1) - sorted_nums[n]
	
def divide(n):
	if n < 0:
		return sorted_nums[0] ** 2
	return divide(n - 1) / sorted_nums[n]
	
	
#Run calculations based on operator given
n = (len(nums) - 1)
if operator == '*':
	print(multiply(n))
elif operator == '+':
	print(add(n))
elif operator == '-':
	print(subtract(n))
elif operator == '\\':
    print(divide(n))