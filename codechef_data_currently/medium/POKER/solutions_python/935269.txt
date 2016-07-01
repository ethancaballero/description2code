"""
 Problem: Poker
 URL: http://www.codechef.com/problems/POKER
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"

n = int(raw_input())

for i in range(n):
    cards = raw_input().split()
    ranks = map(lambda r: r[:-1], cards)
    new_ranks = []
    for rank in ranks:
        if rank == 'T':
            new_ranks.append(10)
        elif rank == 'J':
            new_ranks.append(11)
        elif rank == 'Q':
            new_ranks.append(12)
        elif rank == 'K':
            new_ranks.append(13)
        elif rank == 'A':
            new_ranks.append(1)
        else:
            new_ranks.append(int(rank))
    ranks = new_ranks
    ranks_sorted = ranks[:]
    ranks_sorted.sort()
    suits = map(lambda s: s[-1], cards)
    suits_set = set(suits)
    ranks_set = set(ranks)

    #royal flush
    royal_ranks = set([1, 13, 12, 11, 10])
    if royal_ranks.difference(ranks_set) == set() and len(suits_set) == 1:
        print "royal flush"
        continue
    
    #straight flush
    before = 0
    is_straight = True
    for rank in ranks_sorted:
      
        if before == 0:
            before = rank
        else:
	    if (rank - before == 1):
                before = rank
		continue
            else:
                is_straight = False
    
    if is_straight and (((1 in ranks and (ranks.index(1) == 0 or ranks.index(1) == 4)) or (not 1 in ranks)) and len(suits_set) == 1 and len(ranks_set) == 5):
	print "straight flush"
        continue

    #four of a kind
    number_equals = [ranks.count(k) for k in ranks_set]
    if 4 in number_equals:
        print "four of a kind"
        continue
 
    #full house
    if (set([2, 3]).difference(set(number_equals)) == set()):
        print "full house"
        continue

    #flush
    if (len(suits_set) == 1):
        print "flush"
        continue

    #straight
    before = 0
    is_straight = True
    for rank in ranks_sorted:
        if before == 0:
            before = rank
        else:
            if (rank - before == 1):
                before = rank
                continue
            else:
                is_straight = False
  

    if is_straight and (((1 in ranks and (ranks.index(1) == 0 or ranks.index(1) == 4)) or (not 1 in ranks)) and len(suits_set) > 1):
        print "straight"
        continue
 
    #three of a kind
    if 3 in number_equals:
        print "three of a kind"
        continue

    #two pairs
    if number_equals.count(2) == 2:
        print "two pairs"
        continue

    #pair
    if number_equals.count(2) == 1:
        print "pair"
	continue

    #high card
    print "high card"
