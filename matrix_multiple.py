def mat_multiple(side,n):
	res = [([0] * n) for i in range(n)]
	cut = [([0] * n) for i in range(n)]
	for i in range(1,n):
		for j in range(n-i):
			begin = j
			end = j+i
			# print(begin,end)
			if i==1:
				res[begin][end] = side[j] * side[j+1] * side[j+2]
				cut[begin][end] = end
			else:
				temp = []
				for k in range(begin,end):
					temp.append(res[begin][k] + res[k+1][end] + side[begin] * side[k+1] * side[end+1])
				res[begin][end] = min(temp)
				point = temp.index(min(temp)) + begin
				cut[begin][end] = point

	return res,cut


side = [30,35,15,5,10,20,25]
n = 6

res, cut = mat_multiple(side,n)
for k in res:
	print(k)
print(' ')
for d in cut:
	print(d)