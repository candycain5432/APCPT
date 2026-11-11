'''
make a list of all the RED numbers on a roulette wheel (rednum)

make a list of every number on a roulette wheel (wheelnum)

let the user choose what number, color, etc to bet on
choose how much to bet from starting chip stack

remove chips that were bet from total chip stack

Press enter or smt

using the random library take a random number from (wheelnum) and assign it to a variable(x)

if the number(x) is in the (rednum) then its red if its 0 or 00 its green and if its else its black

**Must check for green numbers first or else when checking for even and odds "00" will error**

check if number or color matches what the user bet on

using actual roulette odds add to total chip stack was was earned 

repeat procces until keyboard interupt
'''

'''
Additions:
    colorama
    spinning anim
    good formating
    history
    hot and cold numbers
'''

'''
Payouts:

Straight up | 1 number   | 35 to 1
split       | 2 numbers  | 17 to 1
street      | 3 numbers  | 11 to 1
corner      | 4 numbers  | 8 to 1
six line    | 6 numbers  | 5 to 1
column      | 12 numbers | 2 to 1
dozen       | 12 numbers | 2 to 1
red/black   | 18 numbers | 1 to 1
odd/even    | 18 numbers | 1 to 1
low/high    | 18 numbers | 1 to 1
'''

'''
AP CPT:
    list = (rednum) and (wheelnum)
    procedure with perameter = check_win(bet_type, result) **example**
    Itteration = just some loop
'''


import random
#import colorama

rednum = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
wheelnum = [00,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
history = []
starting_chips = 5000

chips = starting_chips

while chips > 0:
    bet = 0
    print(chips)

    try:
    
        bet = int(input("""(1) RED or BLACK
(2) ODD or EVEN
(3) LOW or HIGH
(4) Number
"""))
    
    except ValueError:
        print("please enter a valid number")
    
    if bet == 1:
        try:
            color = int(input("""(1) RED
(2) BLACK
"""))

        except ValueError:
            print("Please enter a valid number")

    elif bet == 2:
        print("odd or even")
    elif bet == 3:
        print("low or high")
    elif bet == 4:
        print("number")
    else:
        print("Please enter a valid number")

