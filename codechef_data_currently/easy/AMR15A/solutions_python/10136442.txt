# Mahasena
# Problem code: AMR15A
# https://www.codechef.com/problems/AMR15A

t=int(raw_input())
a=[]
a=map(int,raw_input().split())
even=int(0)
odd=int(0)
for i in a:
	if i%2==0:
		even+=1
	else:
		odd+=1
if even>odd:
	print("READY FOR BATTLE")
else:
	print("NOT READY")