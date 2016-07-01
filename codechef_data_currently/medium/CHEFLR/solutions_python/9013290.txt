import sys
 
 
def update_odd( direction , value ) :
    if direction == 'l' :
       value = (value * 2) 
    else :
       value  = (2 *value + 2) 
    return value
 
def update_even(direction , value) :
    if direction == 'l' :
       value = (2*value - 1)
    else :
       value = (2*value + 1) 
    return value 
 
t = int(raw_input())
for i in range(0,t) :
    list = raw_input()
    value = 1
    flag = True
    for character in list :
        if character in ('l','r'):
            value = update_odd(character,value) if ( flag ) else update_even(character,value)
            flag = not (flag) 
    print value  % (10**9 + 7)