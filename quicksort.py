def quicksort(nums,p,r):
	if p < r:
		mid = partition(nums,p,r)
		quicksort(nums,p,mid-1)
		quicksort(nums,mid+1,r)

def partition(nums,p,r):
	x = nums[r]
	i = p-1
	for j in range(p,r):
		if nums[j] < x:
			i += 1
			temp = nums[j]
			nums[j] = nums[i]
			nums[i] = temp
	temp = nums[i+1]
	nums[i+1] = x
	nums[r] = temp
	return i+1

list1 = [4,5,7,3,9,6,5]
quicksort(list1,0,len(list1)-1)
print(list1)