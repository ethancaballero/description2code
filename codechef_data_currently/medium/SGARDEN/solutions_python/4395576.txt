# GARDERN GAME
# Concept LCM, Prime factorization, MOD usage to prevent overflow
# Status = AC

import sys
MOD = 10 ** 9 + 7

def getCycles(order):
    
    visited = [0]*len(order)
    visited[0] = -1

    cycles = []

    i = 1 

    while i < len(order):

        if(visited[i] == 0):
            
            # we have a new cycle

            length = 1
            nxt = order[i]

            while(nxt != i):

                visited[nxt] = 1
                length = length + 1
                nxt = order[nxt]

            cycles.append(length)
        
        # we did not find a new cycle

        i = i + 1

    return cycles

def primeFact(N):

    factors = []
    i = 2

    while N > 1:

        while( N % i == 0):
            factors.append(i)
            N = N / i
        
        i = i + 1
        
        if i*i > N:
            if N > 1:
                factors.append(N)
            break

    primed = dict()

    for x in factors:

        if x not in primed:
            primed[x] = 1
        else:
            primed[x] = primed[x] + 1

    return primed

def lcm(l):
    
    assert len(l) >= 0
    
    lcm_d = dict()

    for cyc in l:    
        primed = primeFact(cyc)
        
        for p in primed:
            if p not in lcm_d:
                lcm_d[p] = primed[p]
            else:
                if(lcm_d[p] < primed[p]):
                    lcm_d[p] = primed[p]
    
    ans = 1
    for p in lcm_d:
        ans = ans * ((p ** lcm_d[p]) % MOD)  
    
    return ans % MOD

def solve(order):

    cycles = getCycles(order)
    return lcm(cycles)

T = int(raw_input())

while(T > 0):
    N = int(raw_input())
    l_in = raw_input()
    ls = l_in.split()
    order = []

    for x in ls:
        order.append(int(x))

    # to make it 1 indexed

    order = [-1] + order
    
    print solve(order)
    T = T - 1
