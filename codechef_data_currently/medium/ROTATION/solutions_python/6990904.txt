import math

def main():

	arr = raw_input()
	arr = arr.split()
	arr = map(int , arr)
	size = arr[0]
	t = arr[1]
	arr = raw_input()
	arr = arr.split()
	arr = map(int , arr)

	iniindex = 1

	for i in range (t):
		q = raw_input()

		q = q.split()
		if(q[0] == 'C'):
			iniindex -= int(q[1])

		if(q[0] == 'A'):
			iniindex += int(q[1])
		
#		print "iniindex =", iniindex

		if(q[0] == 'R'):
			print arr[(int(q[1]) - iniindex)%size]

if __name__ == '__main__':
	main()