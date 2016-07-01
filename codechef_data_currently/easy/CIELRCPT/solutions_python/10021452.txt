# Codechef Beginner Problem CIELRCPT

t = int(raw_input())

while t>0:
    p = int(raw_input())
    count = 0
    c = 0

    while (p-2048) > 0:
        p = p - 2048
        c = c + 1

    binary = bin(2048)[2:]
    count = count + (binary.count('1') * c);

    binary = bin(p)[2:]
    count = count + binary.count('1')

    t = t -1
    print count