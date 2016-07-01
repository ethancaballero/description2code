# Tanu and Head-bob
# Problem code: HEADBOB
# https://www.codechef.com/problems/HEADBOB

t=int(raw_input())
for i in range(t):
	n=int(raw_input())
	s=raw_input()
	flag=int(0)
	for j in s:
		if j=='I':
			print("INDIAN")
			flag=1
			break
		elif j=='Y':
			print("NOT INDIAN")
			flag=1
			break
	if flag==0:
		print("NOT SURE")