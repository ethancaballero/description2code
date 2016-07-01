'''
Created on Feb 22, 2013

@author: anuvrat
'''

import sys

MODULATOR = 1000000007

class Memoize( object ):
    def __init__( self, f ):
        self.f, self.cache = f, {}

    def __call__( self, *args ):
        if not args in self.cache: self.cache[args] = self.f( *args )
        return self.cache[args]

@Memoize
def nCk( n, k ): return reduce( lambda acc, m:acc * ( n - k + m ) / m, range( 1, k + 1 ), 1 )

@Memoize
def winning_options( n ):
    if n % 2: return pow( 2, n - 1, MODULATOR )
    else:
        return ( pow( 2, n - 1 ) - nCk( n, n / 2 ) / 2 ) % MODULATOR

def main():
    for _ in  xrange( int( sys.stdin.readline() ) ):
        n = int( sys.stdin.readline() )
        colors = map( int, sys.stdin.readline().strip().split() )
        print winning_options( n )

main()
