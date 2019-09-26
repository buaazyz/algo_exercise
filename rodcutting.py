def rodcutting(length, profit, rod):
	values = dict()
	values[0] = 0
	cut = dict()
	for i in range(1, rod+1):
		tempV = []
		cnt = 0
		for j in length:
			if j <= i:
				valuej = values[i-j] + profit[cnt]
				tempV.append(valuej) 
			else:
				break
			cnt += 1
		valuei = max(tempV)
		values[i] = valuei
		cut[i] = length[tempV.index(valuei)]

	return values,cut





length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
profit = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


v, c = rodcutting(length,profit,10000)
print(v[4])