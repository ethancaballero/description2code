import re
CHARACTER_MAP = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
ALLOWED_LENGTHS = [1,2]
ALLOWED_MOVES = [(1,2),(2,1)]
def move_checker(char1,int1,char2,int2):
    """
    Gets one of the component and gets number of moves in that direction
    """
    char1 = CHARACTER_MAP[char1]
    char2 = CHARACTER_MAP[char2]
    char_moves = 0
    int_moves = 0



    if abs(char1 - char2) in ALLOWED_LENGTHS:
        char_moves = abs(char1 - char2)

    if abs(int1 - int2) in ALLOWED_LENGTHS:
        int_moves = abs(int1 - int2)


    if (char_moves,int_moves) in ALLOWED_MOVES:
        return True
    
    return False
   
def main():
    pattern = re.compile("[a-h][1-8]-[a-h][1-8]")
    t = int(raw_input())
    for i in range(t):
        string = raw_input()
        if len(string) == 5 and pattern.match(string):
            if move_checker(string[0],int(string[1]),string[3],int(string[4])):
                print "Yes"
            else:
                print "No"
        else:
            print "Error"


if __name__ == '__main__':
    main()
