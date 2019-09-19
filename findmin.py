def findmin(nums, p, r):
	if r-p >= 2:
		a = (p+r) // 2
		mid = nums[a]
		left = nums[a-1]
		right = nums[a+1]
		if mid > left:
			return findmin(nums, p, a)
		elif mid > right:
			return findmin(nums, a, r)
		else:
			return mid

# nums = [9,3,7,2,1,4,5]
nums = [9,8,6,4,3,7]
length = len(nums)

print(findmin(nums,0,length-1))