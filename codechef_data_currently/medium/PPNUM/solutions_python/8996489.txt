t = input()


def digits(n1):
	cnt = 0
	while(n1 != 0):
		cnt += 1
		n1 /= 10
	return cnt ; 


def res(n):
	result = 0
	dig = digits(n) 
	if (dig == 1):
		return (n*(n+1))/2 ; 
	ns = 0
	for i in range(1,dig):
		if (i == 0):
			ns = 0
			continue 
		else:
			ns = 9*(10**(i-1))


		st = 10**(i-1)
		en = 10**i -1 
		#print i , ns , st , en 
		result += ((ns*(st+en))/2)*i 
		#print result,i 
	stt = 10**(dig-1)
	enn = n
	nss = enn - stt +1
	result += ((nss*(enn+stt))/2)*dig
	return int(result) ; 




it = 0 
while (it < t):
	s = raw_input()
	s1 = s.split(" ")
	l = int(s1[0])
	r = int(s1[1]) 
	#print res(r)
	
	print ((res(r)-res(l-1))%1000000007)

	it += 1 