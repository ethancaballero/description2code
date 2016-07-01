from decimal import Decimal

def app(str , dict):
	str = list(str)
	newstr = str[:]
	for key , value in dict.iteritems():
		indices = [i for i, x in enumerate(str) if x == key]
		for i in indices :
			newstr[i] = value
	return "".join(newstr)

def main():

	t = int(raw_input())

	for i in range(t):
		dict = {}

		tes = int(raw_input())
		for j in range(tes):
			arr = raw_input()
			arr = arr.split()
			dict[arr[0]] = arr[1]
		passwd = raw_input()
		nonfinans = app(passwd , dict)
		ans = ""
		for i in range(len(nonfinans)) :
			if nonfinans[i] != '0' :
				ans = nonfinans[i:]
				break
		has_point = False
		for ch in ans :
			if ch == '.' :
				has_point = True
				break
		if has_point :
			end = len(ans)
			while ans[end - 1] == '0' :
				end -= 1
			if ans[end - 1] == '.' :
				end -= 1
			ans = ans[:end]
		if len(ans) == 0 :
			ans = "0"
		print ans



if __name__ == '__main__':
	main()