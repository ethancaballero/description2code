# Chef and his Sequence
# Problem code: CHEFSQ
# https://www.codechef.com/problems/CHEFSQ

t=int(raw_input())
for i in range(t):
	n=[]
	f=[]
	ln=int(raw_input())
	n=map(int,raw_input().split())
	lf=int(raw_input())
	f=map(int,raw_input().split())
	flag=int(0)
	for j in f:
		if j in n:
			flag+=1
	if flag==lf:
		print("Yes")
	else:
		print("No")