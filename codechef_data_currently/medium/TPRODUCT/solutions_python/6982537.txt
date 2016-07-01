
count = 0
glogarr = []

def gt(n):
	
	#print glogarr
	#print count
	if(n > count-1):
		return 1
	else:
		return globarr[n]*max( gt(2*n+1) , gt(2*n+2))

def main():

	t = raw_input()
	t = int(t)

	while(t > 0):
		
		arr = raw_input()
		arr = arr.split()
		global globarr 
		globarr = map(int,arr)
		global count
		count = len(arr)
		finans = int(gt(0) % 1000000007)
		print finans
		t =raw_input()		
		t = int(t)

if __name__ == '__main__':
	main()