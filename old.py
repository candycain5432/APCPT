'''
ERRORS:
1. Line 77, color_number: "00" == 0 is False, so "00" shows as black/white in history instead of green.

2. Lines 104, 116, 122, check_win: b % 2, b <= 18, and b >= 19 crash with a TypeError when b is "00".

3. Lines 104-124, check_win: 0 counts as even and low, so it wins those bets. 0 and 00 should lose them.

4. Line 128, check_win: usernum is a string from input() and spinnum is an int, so "5" == 5 is False. Number bets can only ever win on "00".

5. Lines 92 and 98, check_win: it reads the global `color` instead of getting it as a parameter. In redo_bet, `color` is local, so check_win sees the previous spin's color.

7. redo_bet: no check that betamount <= chips, so chips can go negative.

8. Lines 207 and 231: bet type isn't validated. Entering 0, 8, etc. gives bettypestr "Error", and the game continues. check_win then prints "Something went wrong" and returns the stale `won` value.

9. Lines 207, 237, 212: int(input()) crashes with ValueError on non-numbers. The number bet (usernum) isn't validated either, so "abc" or 37 is accepted.

11. redo_bet: it recurses into itself and duplicates the main loop's spin logic.

13. Line 73 and imports: os.system('clear') doesn't work on Windows, and colorama's init() is never called.
'''




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
try:

    import random
    from colorama import Fore, Back, Style
    import os

    rednum = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    wheelnum = ["00",0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    history = []
    starting_chips = 5000
    betamount = 0
    chips = starting_chips
    usernum = 0
    won = None
    header = Fore.BLUE

    def clearscreen():
        os.system('clear')
        print(Style.RESET_ALL)

# This segment was made with Claude AI with tweaks by me
    def color_number(num):
        if num in (0, "00"):
            return f"{Fore.GREEN}{num}{Style.RESET_ALL}"
        elif num in rednum:
            return f"{Fore.RED}{num}{Style.RESET_ALL}"
        else:
            return f"{Fore.CYAN}{num}{Style.RESET_ALL}"

    def print_history(history):
        print("History: " + ", ".join(color_number(n) for n in history))
# This segment was made with Claude AI with tweaks by me


    def check_win(a,b,c): #bettype, spinnum, usernum
        global won, color
        
        if (a == 7) and (b in (0, "00")):
            if c in (0, "00"):
                won = 1
        else:
                    
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


    def win_lose():
        global result
        if result == True:
            print(Fore.GREEN + "YOU WON!\n")
        else:
            print(Fore.RED + "You lost\n")


    def redo_bet():
        global chips, result, color
        clearscreen()
        print(Fore.YELLOW + f"--Chips:{chips}")
        print(Style.RESET_ALL)
        print(f"You bet {betamount} on {bettypestr}")
        spinnum = random.choice(wheelnum)
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
            print(Fore.RED + f"Spin = {spinnum}-Red")
            print(Style.RESET_ALL)
        else:
            color = "black"
            print(Fore.BLACK + Back.WHITE + f"Spin = {spinnum}-Black")
            print(Style.RESET_ALL)

        result = check_win(bettype, spinnum, usernum)

        win_lose()

        if result == True and bettype <= 6:
            chips += betamount
        elif result == True and bettype == 7:
            chips += betamount * 35
        else:
            chips -= betamount
        
        print(Style.RESET_ALL)

        restart = input("Press enter to play again or 'redo' to redo your bet: ")
        if restart == "redo":
            redo_bet()

        
    while chips > 0: 
        clearscreen()
        #SHOW CHIPS
        print(Fore.YELLOW + f"--Chips:{chips}")
        print(Style.RESET_ALL)
        print_history(history)
        print(Style.RESET_ALL)
        print("""(1) RED
(2) BLACK
(3) ODD
(4) EVEN
(5) LOW
(6) HIGH
(7) NUMBER\n""")

        bettype = int(input(header + "-Enter the number of the bet type you wish to bet on: "))


        #Asks user for number if picked 7 for bettype
        if bettype == 7:
            usernum = int(input(header + "-Choose a number 0-36 or 00: "))
            print(Style.RESET_ALL)

        # Turns the bet type into a string so it can be printed
        if bettype == 1:
            bettypestr = "Red"
        elif bettype == 2:
            bettypestr = "Black"
        elif bettype == 3:
            bettypestr = "Odd"
        elif bettype == 4:
            bettypestr = "Even"
        elif bettype == 5:
            bettypestr = "Low"
        elif bettype == 6:
            bettypestr = "High"
        elif bettype == 7:
            bettypestr = usernum
        else:
            bettypestr = "Error"



        validity = 0
        while validity == 0:
            betamount = int(input(header + "-Enter a valid bet amount: (minimum of 1): "))
            
            print(Style.RESET_ALL)
            if betamount > chips:
                print(Back.RED + Fore.YELLOW+ "That is too high of a bet please enter a valid bet")
            elif betamount < 1:
                print(Back.RED + Fore.YELLOW + "That is too low of a bet please enter a valid bet")
            else:
                validity = 1
        clearscreen()
        print(f"You bet {betamount} on {bettypestr}")
        ready = input(header + "-press enter to spin or type 'cancel' to cancel\n")
        if ready == "cancel":
            continue
        
        print(Style.RESET_ALL)
        spinnum = random.choice(wheelnum)
        history.append(spinnum)
        clearscreen()
        
        print(Fore.YELLOW + f"--Chips:{chips}")
        print(Style.RESET_ALL)
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
            print(Fore.RED + f"Spin = {spinnum}-Red")
            print(Style.RESET_ALL)
        else:
            color = "black"
            print(Fore.BLACK + Back.WHITE + f"Spin = {spinnum}-Black")
            print(Style.RESET_ALL)


        result = check_win(bettype, int(spinnum), usernum)

        win_lose()
        
        
        print(Style.RESET_ALL)

        

        if result == True and bettype <= 6:
            chips += betamount
        elif result == True and bettype == 7:
            chips += betamount * 35
        else:
            chips -= betamount

        restart = input("Press enter to play again or 'redo' to redo your bet: ")
        if restart == "redo":
            redo_bet()
        else:
            continue
    
    else:
        print("GAME OVER, The house always wins")















except KeyboardInterrupt:
    print("\nExiting")
