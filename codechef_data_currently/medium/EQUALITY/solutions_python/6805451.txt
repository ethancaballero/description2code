#! /usr/bin/env python

def main():
    t=input()
    
    while t:
    	n=input()
    	a=map(int, raw_input().split())
    	s=sum(a)
    	for i in range(0,n):
    		print s/(n-1)-a[i],
    			
    	print 
    	t-=1
    
if __name__=="__main__":
    main()
