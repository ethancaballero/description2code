'''
Created on Feb 7, 2013

@author: anuvrat
'''

import sys

MAX_N = 1000000
MODULATOR = 1000000007

class Memoize( object ):
    def __init__( self, f ):
        self.f, self.cache = f, {}

    def __call__( self, *args ):
        if not args in self.cache: self.cache[args] = self.f( *args )
        return self.cache[args]

@Memoize
def generate_fib( upper_index, modulated = 1 ):
    fibs = [1] * ( upper_index + 1 )
    for idx in xrange( 2, upper_index + 1 ):
        fibs[idx] = ( fibs[idx - 1] + fibs[idx - 2] ) % modulated

    return fibs

def ways_of_climbing( steps ):
    '''
        We need to solve the equation a + 2b = steps
    '''
    return bin( generate_fib( MAX_N, MODULATOR )[steps] ).count( "1" )


def main():
    for _ in  xrange( int( sys.stdin.readline() ) ):
        steps, guess = map( int, sys.stdin.readline().strip().split() )
        print "CORRECT" if ways_of_climbing( steps ) == guess else "INCORRECT"

main()
