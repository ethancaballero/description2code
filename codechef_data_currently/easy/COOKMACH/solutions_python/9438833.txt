## To check if a number is power of 2:
#  Bitwise AND n and n-1, result should be zero
#  Example: 8 = 0b1000, 8-1 = 7 = 0b0111
#  So,      0b1000 & 0b0111 = 0b0000, hence is power of 2

T = int(raw_input())

for it in range(T):
    A, B = map(int, raw_input().split())
    count = 0
    while( A & A-1):
        A = A >> 1      # Divide by 2
        count += 1
    while (A != B):
        if A < B :
            A = A << 1  # Multiply by 2
        else:
            A = A >> 1  # Divide by 2
        count += 1
    print count
