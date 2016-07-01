# Chef and Feedback
# Problem code: ERROR
# https://www.codechef.com/problems/ERROR

t=int(raw_input())
for i in range(t):
	s=raw_input()
	l=len(s)
	flag=int(0)
	for j in range(l-2):
		if s[j:j+3]=="101" or s[j:j+3]=="010":
			flag=1
			break
	if flag==1:
		print("Good")
	else:
		print("Bad")