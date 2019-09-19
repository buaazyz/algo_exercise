def MCS(arraylist, left, right):
	length = right - left
	if length == 0:
		return arraylist[right]
	midL = length // 2 + left
	midR = midL + 1
	num1 = MCS(arraylist, left, midL)
	num2 = MCS(arraylist, midR, right)
	num3 = maxLnR(arraylist,midL,midR,left,right)
	return chose_max(num1,num2,num3)

def maxLnR(arraylist, midL, midR, left, right):
            maxL = arraylist[midL]
            maxR = arraylist[midR]
            tempsum = 0
            for i in range(midL,left-1,-1):
                tempsum += arraylist[i]
                maxL = tempsum if tempsum > maxL else maxL
            tempsum = 0
            for i in range(midR,right+1,1):
                tempsum += arraylist[i]
                maxR = tempsum if tempsum > maxR else maxR
            return maxR+maxL

def chose_max(n1, n2, n3):
	print(n1,n2,n3)
	if n1 > n2:
		if n1 > n3:
			return n1
		else:
			return n3
	elif n2 > n3:
		return n2
	else:
		return n3


# arraylist= [-2,1,-3,4,-1,2,1,-5,4]
# [0,-2,-1,-4,0,-1,1,2,-3,1]
arraylist = [6,-4,7,-4,0,1]



left = 0
right = len(arraylist)-1

# print(MCS(arraylist,left,right))


'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arraylist = nums
        temp_sum = arraylist[0]
        max_num = arraylist[0]
        for i in range(len(arraylist)):
            if i > 0:
                temp_sum += arraylist[i]
                if(temp_sum < arraylist[i]):
                    temp_sum = arraylist[i]
                if(temp_sum > max_num):
                    max_num = temp_sum
        return max_num


'''