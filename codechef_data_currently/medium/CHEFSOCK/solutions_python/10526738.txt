arr=map(int,raw_input().split())
Mremain=arr[2]-arr[0]
Psocks=arr[1]
socks=0
while(Mremain>=Psocks):
	socks+=Mremain/Psocks
	Mremain=Mremain%Psocks
if(socks%2==0):
	print "Lucky Chef"
else:
	print "Unlucky Chef"