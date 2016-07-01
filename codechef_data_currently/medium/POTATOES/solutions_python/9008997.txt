import math
for i in range(int(raw_input())):
	num = map(int, raw_input().split())
	sum1 = sum(num)
	if sum1 == 0:
		print 2
	else:
		flag = True
		last = sum1 + sum1/2+1
		for i in range(sum1+1,last+1):
			for j in range(2,int(math.sqrt(i))+1):
				if i % j == 0:
					flag = False
					break
			else:
				print i - sum1
				break
