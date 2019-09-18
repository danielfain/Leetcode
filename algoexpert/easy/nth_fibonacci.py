def getNthFib(n):
	nums = [0, 1]

	while n > 2:
		next_num = sum(nums)
		nums[0] = nums[1]
		nums[1] = next_num
		n -= 1

	return 0 if n == 1 else nums[1]
