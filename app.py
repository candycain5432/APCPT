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
from colorama import Fore, Back, Style

rednum = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
wheelnum = ["00",0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
history = []
starting_chips = 5000
betamount = 0
chips = starting_chips
usernum = None
won = None
header = Fore.BLUE

def check_win(a,b,c):
    global won
    if a == 1:
        if color == "red":
            won = 1
        else:
            won = 0
    
    elif a == 2:
        if color == "black":
            won = 1
        else:
            won = 0
    
    elif a == 3:
        if b % 2 == 0:
            won = 0
        else:
            won = 1
    
    elif a == 4:
        if b % 2 == 0:
            won = 1
        else:
            won = 0
    
    elif a == 5:
        if b <= 18:
            won = 1
        else:
            won = 0
    
    elif a == 6:
        if b >= 19:
            won = 1
        else:
            won = 0

    elif a == 7:
        if c == b:
            won = 1
        else:
            won = 0
    
    else:
        print("Something went wrong")

    if won == 1:
        return True
    else:
        return False








while chips > 0: 
    #SHOW CHIPS
    print(Fore.YELLOW + f"--Chips:{chips}")
    print(Style.RESET_ALL)
    print(Fore.GREEN + f"--History:{history}")
    print(Style.RESET_ALL)
    bettype = int(input("""(1) RED
(2) BLACK
(3) ODD
(4) EVEN
(5) LOW
(6) HIGH
(7) NUMBER\n"""))

    if bettype == 7:
        usernum = input(header + "-Choose a number 0-36 or 00:\n")
        print(Style.RESET_ALL)

    validity = 0
    while validity == 0:
        betamount = int(input(header + "-Enter a valid bet amount: (minimum of 1)\n"))
        
        print(Style.RESET_ALL)
        if betamount > chips:
            print(Back.RED + Fore.YELLOW+ "That is too high of a bet please enter a valid bet")
        elif betamount < 1:
            print(Back.RED + Fore.YELLOW + "That is too low of a bet please enter a valid bet")
        else:
            validity = 1


    ready = input(header + "-press enter to spin or type 'cancel' to cancel\n")
    if ready == "cancel":
        continue
    
    print(Style.RESET_ALL)
    spinnum = random.choice(wheelnum)
    print(spinnum) # REMOVE
    history.append(spinnum)
    
    if spinnum == 0:
        color = "green"
        print(Fore.GREEN + f"Spin = 0")
        print(Style.RESET_ALL)

    elif spinnum == "00":
        color = "green"
        print(Fore.GREEN + f"Spin = 00")
        print(Style.RESET_ALL)
    elif spinnum in (rednum):
        color = "red"
        print(Fore.RED + f"Spin = {spinnum}")
        print(Style.RESET_ALL)
    else:
        color = "black"
        print(Fore.BLACK + Back.WHITE + f"Spin = {spinnum}")
        print(Style.RESET_ALL)

    print(color) # remove

    result = check_win(bettype, spinnum, usernum)

    if result == True:
        print(Fore.GREEN + "- - - - -YOU WON!\n")
    else:
        print(Fore.RED + "- - - - - You lost\n")
    
    
    print(Style.RESET_ALL)

    if result == True and bettype <= 6:
        chips += betamount
    elif result == True and bettype == 7:
        chips += betamount * 35
    else:
        chips -= betamount
