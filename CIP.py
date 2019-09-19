def CIP(nums, left, right, record):
	mid = (left + right) // 2
	if mid == right:
		return [nums[mid]], 0, record
	midR = mid + 1

	nums_left, count_L, record = CIP(nums, left, mid, record)
	nums_right, count_R, record = CIP(nums, midR, right, record)

	count_M = 0
	i = j= 0
	templist = []
	while i < len(nums_left) and j < len(nums_right):
		if nums_left[i] < nums_right[j]:
			templist.append(nums_left[i])
			i += 1
		else:
			templist.append(nums_right[j])
			for k in range(i,len(nums_left)):
				record[q] += 1
			count_M += len(nums_left)-i
			j += 1
	if i < len(nums_left):
		for k in range(i, len(nums_left)):
			templist.append(nums_left[k])
	if j < len(nums_right):
		for k in range(j, len(nums_right)):
			templist.append(nums_right[k])

	count = count_M + count_L + count_R
	return templist, count, record


arraylist = [1,2,3,4,5,6,7,0]
left = 0
right = len(arraylist) - 1
record = {}
for q in arraylist:
	record[q] = 0
_, num, record = CIP(arraylist,left, right, record)

temp = []
for q in arraylist:
	temp.append(record[q])

print(temp)