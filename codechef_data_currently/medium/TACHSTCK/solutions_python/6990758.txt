import math

def main():

	arr = raw_input()
	arr = arr.split()
	arr = map(int , arr)
	num = arr[0]
	diff = arr[1]
	arr = []
	for i in range(num):
		arr.append(int(raw_input()))

	arr.sort()
	i=0
	count = 0
	while i < num-1 :
		if(arr[i+1]-arr[i] <= diff):
			count += 1
			i += 2
		
		else :
			i += 1

	print count

if __name__ == '__main__':
	main()