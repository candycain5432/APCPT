'''
ERRORS:
1. "Too big" message gets erased
   If you repeat a bet you can no longer afford, bet() prints the message and
   returns, then clearscreen() at the top of the main loop wipes it. Add an
   input() pause after the message. Same at 0 chips: the game still offers
   "repeat" before ending.

2. Dead code
   `else: print("Something went wrong")` in check_win and the
   `bettypestr = "Error"` branch can't run now that the bet type is validated.
   Delete them.

3. Not portable
   os.system('clear') doesn't work on Windows.

4. Style
   - Stray semicolon in `return;`
   - strwheel duplicates wheelnum (build one from the other)
   - won, result and color are globals; pass color into check_win as a
     parameter and return results instead
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
    strwheel = ["00","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36"]
    history = []
    starting_chips = 5000
    betamount = 0
    chips = starting_chips
    usernum = 0
    won = None
    header = Fore.BLUE
    betv = None
    bettype = 0

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
        if b in (0, "00"):
            if a == 7:
                if str(b) == c:
                    won = 1
                else:
                    won = 0
            else:
                won = 0
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
                if c == str(b):
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

    def game_over():
        print("GAME OVER, The house always wins")
        print_history(history)


    def bet():
        global chips, result, color
        if betamount > chips:
            print("That bet is too big")
            return;
        else:
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
            
            restart = input("Press enter to play again or 'r' or 'R' to repeat your bet: ")
            if restart.lower().strip() == "r":
                bet()
        
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
        betv = 0
        while betv == 0:
            try:
                bettype = int(input(header + "-Enter the number of the bet type you wish to bet on: "))
            except ValueError:
                print("Please enter a valid number")
                continue
            
            if (bettype >= 1) and (bettype <= 7):
                betv = 1
            else:
                print("Please enter a number 1-7")

        #Asks user for number if picked 7 for bettype
        if bettype == 7:
            unv = 0
            while unv == 0:
                usernum = input(header + "-Choose a number 0-36 or 00: ")
                print(Style.RESET_ALL)

                if usernum in strwheel:
                    unv = 1
                else:
                    print("Please enter a number 0-36 or 00")


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
            try:
                betamount = int(input(header + "-Enter a valid bet amount: (minimum of 1): "))
            except ValueError:
                print("Please enter a valid number")
                continue


            print(Style.RESET_ALL)
            if betamount > chips:
                print(Back.RED + Fore.YELLOW+ "That is too high of a bet please enter a valid bet")
            elif betamount < 1:
                print(Back.RED + Fore.YELLOW + "That is too low of a bet please enter a valid bet")
            else:
                validity = 1
        
        
        bet()
    
    else:
        game_over()















except KeyboardInterrupt:
    print("\nExiting")
