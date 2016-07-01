'''Problem name - KGOOD'''
'''Correct Solution'''
'''
test_case = int(raw_input())
for t in xrange(test_case):
    word, k = map(str, raw_input().split())
    k = int(k)
    number = []
   	s = ''
    for w in word:
    	if not w in s:
    		number.append(word.count(w))
    		s += w
    cost = []
   	for m in number:
    	temp = 0
    	for i in number:
   			if m + k < i:
    			temp += i - m - k
    		if m > i:
   				temp += i
   		cost.append(temp)
   	# print number
    # print cost
   	print min(cost) 
'''

import collections
from collections import OrderedDict
'''
def find(counter):

	temp = {}
	for j in xrange(len(counter.keys())):

		for k in xrange(j+1, len(counter.keys())):
			temp[counter.keys()[j], counter.keys()[k]] = abs(counter[counter.keys()[j]] - counter[counter.keys()[k]])
	
	return temp

def tot(a):
	
	b = list(a[0])
	c = int(a[1])
	got = 0
	counter = OrderedDict(collections.Counter(b))
	temp = find(counter)
	#print temp
	#print counter, type(counter)
	if bool(temp) is False:
		if counter.values()[0] <= c:
			return 0

		else:
			return counter.values()[0] - counter

	mi = min(counter.values())
	#print mi, counter.values(), counter, counter.keys()[counter.values().index(mi)], counter.keys()
	for i in xrange(len(counter.values())):

		if counter.values()[i] - mi > c:
			
			z = counter.values()[i] - (mi + c)
			got += z
	
	return got 		


def hel(a):

	b = list(a[0])
	c = int(a[1])
	got = 0
	temp = find(counter)
	#last = {}
	if bool(temp) is False:
		if counter.values()[0] <= c:
			return 0

		else:
			return counter.values()[0] - c

	
	for key in counter.keys():
		last[key] = []			 
	
	print temp
	while True:
		a = 0
		for key, value in temp.items():
			
			if value <= c:
				continue

			else:
				a = 1
				
				print lol
				if counter[lol[0]] > counter[lol[1]]:
					temp[lol[0]] -= i - c
					for l in temp.keys():
						if lol[0] in l:
							temp[lol[0]] -lol= i - c 
				else:
					temp[lol[1]] -= i - c	
					for l in temp.keys():
						if lol[1] in l:
							temp[lol[1]] -= i - c
				
				#print key
				
				if counter[key[0]] > counter[key[1]]:
					last[key[0]].append(counter[key[0]] - counter[key[1]] - c)

				else:
					last[key[1]].append(counter[key[1]] - counter[key[0]] - c)
				
				if counter[key[0]] > counter[key[1]]:
					counter[key[0]] -= value - c
					got += value - c
					#print counter, a, temp
					temp = find(counter)
					break

				else:
					counter[key[1]]	-= value - c
					temp = find(counter)
					got += value - c
					#print counter, a, temp
					break

		if a == 0:
			break				
	
	#print last
	#sol.append(sum(last.values()))
	#last = list(set(last))
	#print last	
	#sol.append(len(last))
	print counter
	return got
'''

def last(a):
	b = list(a[0])
	c = int(a[1])
	counter = OrderedDict(collections.Counter(b))
	got = 10**9
	for i in counter.values():

		temp = 0
		for j in counter.values():
			if i + c < j:
				temp += j - i - c

			if i > j:
				temp += j

		if temp < got:
			got = temp		
	
	return got					 

sol = []
tt = int(raw_input())
for i in xrange(tt):
	a = raw_input().split()
	sol.append(last(a))

for i in xrange(tt):
	print sol[i]








