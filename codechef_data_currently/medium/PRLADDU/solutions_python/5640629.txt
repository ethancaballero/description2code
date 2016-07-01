# http://www.codechef.com/problems/PRLADDU

def calculate(arr):
	# Not gonna lie, I was stuck on this one. I was trying a long
	# winded solution where you found the closest "villager" and then connected
	# him to the dino, reducing one from that point. But even I knew that that
	# was gonna be really slow.

	# Thank god for the editorial, though.
	# http://discuss.codechef.com/questions/52939/prladdu-editorial
	# Seems pretty simple now. Probably should have thought of it like that.
	a = 0; tmp = 0
	for i in arr:
		tmp += i
		a += abs(tmp)
	return a


def main():
	t = int(raw_input())
	while t:
		n = raw_input()
		ls = map(int, raw_input().split())
		print calculate(ls)
		t -= 1

if __name__ == '__main__':
	main()