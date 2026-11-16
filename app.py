




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
    import os
    from rich.console import Console
    from rich.theme import Theme
    from rich.live import Live
    from rich.rule import Rule
    import time
    from rich.table import Table
    from rich.align import Align
    from rich.panel import Panel
    import questionary

    rednum = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    wheelnum = ["00",0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    strwheel = ["00","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36"]
    history = []
    starting_chips = 5000
    betamount = 0
    chips = starting_chips
    usernum = 0
    won = None
    console = Console(theme=Theme({"header": "blue", "error": "yellow on red"}), highlight=False)
    betv = None
    bettype = 0
    n = None
    last_change = 0
    casino_style = questionary.Style([
    ("qmark", "fg:#BE1A1A bold"),        # the symbol before the question
    ("question", "bold"),                # the question text
    ("pointer", "fg:#60C1E5 bold"),      # the arrow next to the current option
    ("highlighted", "fg:#60C1E5 bold underline italic"),  # the option the arrow is on
    ("answer", "fg:#60C1E5 bold"),       # what they picked, shown after Enter
    ("instruction", "fg:#808080 italic"),# the "(Use arrow keys)" hint
    ])

    def clearscreen():
        os.system('clear')
    '''
    def show_menu():
        t = Table(title="Place your bet")
        t.add_column("#", justify="right", style="bold")
        t.add_column("Bet")
        t.add_column("Pays", justify="right", style="gold3")

        t.add_row("1", "[white on red] Red [/]", "1:1")
        t.add_row("2", "[white on black] Black [/]", "1:1")
        t.add_row("3", " Odd", "1:1")
        t.add_row("4", " Even", "1:1")
        t.add_row("5", " Low (1–18)", "1:1")
        t.add_row("6", " High (19–36)", "1:1")
        t.add_row("7", " Single number", "35:1")

        console.print(Align.center(t))
        console.print()
    '''

# This segment was made with Claude AI with tweaks by me
    def color_number(num):
        if num in (0, "00"):
            return f"[white on green] {num} [/]"
        elif num in rednum:
            return f"[white on red] {num} [/]"
        else:
            return f"[white on black] {num} [/]"

    def print_history(history):
        console.print("History: " + ", ".join(color_number(n) for n in history))
# This segment was made with Claude AI with tweaks by me


    def check_win(bettype,spinnum, usernum): #bettype, spinnum, usernum
        global won, color
        if spinnum in (0, "00"):
            if bettype == 7:
                if str(b) == c:
                    won = 1
                else:
                    won = 0
            else:
                won = 0
        else:

            if bettype == 1:
                if color == "red":
                    won = 1
                else:
                    won = 0
            
            elif bettype == 2:
                if color == "black":
                    won = 1
                else:
                    won = 0
            
            elif bettype == 3:
                if spinnum % 2 == 0:
                    won = 0
                else:
                    won = 1
            
            elif bettype == 4:
                if spinnum % 2 == 0:
                    won = 1
                else:
                    won = 0
            
            elif bettype == 5:
                if spinnum <= 18:
                    won = 1
                else:
                    won = 0
            
            elif bettype == 6:
                if spinnum >= 19:
                    won = 1
                else:
                    won = 0

            elif bettype == 7:
                if usernum == str(spinnum):
                    won = 1
                else:
                    won = 0
            

        if won == 1:
            return True
        else:
            return False

    def chips_header():
        if last_change > 0:
            suffix = f"[green]({last_change:+})[/]"
        elif last_change < 0:
            suffix = f"[red]({last_change:+})[/]"
        else:
            suffix = ""
        console.rule(f"[gold3]Chips: {chips}[/] {suffix}", style="gold3")

    def game_over():
        print("GAME OVER, The house always wins")
        print_history(history)


    def check_betamount(text):
        if not text.isdigit():
            return "Please enter a whole number"
        if int(text) < 1:
            return "Minimum bet is 1"
        if int(text) > chips:
            return f"You only have {chips:,} chips"
        return True

    def check_usernum(text):
        if text.strip() in strwheel:
            return True
        return "Enter a number 0-36 or 00"

    def bet():
        global chips, result, color, last_change
        delay = 0.05
        if betamount > chips:
            print("That bet is too big")
            return;
        else:
            clearscreen()
            chips_header()
            
            print(f"You bet {betamount} on {bettypestr}")
            console.input("[dim]Press Enter to spin...[/]")
            spinnum = random.choice(wheelnum)
            history.append(spinnum)
            with Live(refresh_per_second=20) as live:
                for i in range(random.randrange(15, 20)):
                    n = random.choice(wheelnum)  
                    live.update(Rule(color_number(n), characters="="))
                    time.sleep(delay)
                    delay *= 1.15
                live.update(Rule(color_number(spinnum), characters="=")) 

            if spinnum == 0:
                color = "green"
                console.print(f"[green]Spin = 0[/]")
                

            elif spinnum == "00":
                color = "green"
                console.print(f"[green]Spin = 00[/]")
                
            elif spinnum in (rednum):
                color = "red"
                console.print(f"[white on red]Spin = {spinnum}-Red[/]")
                
            else:
                color = "black"
                console.print(f"[white on black]Spin = {spinnum}-Black[/]")
                

            result = check_win(bettype, spinnum, usernum)

            if result == True and bettype <= 6:
                change = betamount
            elif result == True and bettype == 7:
                change = betamount * 35
            else:
                change = -betamount

            chips += change
            last_change = change

            if change > 0:
                outcome = f"[bold green]YOU WON +{change}[/]"
                border = "green"
            else:
                outcome = f"[bold red]You lost {-change}[/]"
                border = "red"
            
            text = f"You bet [gold3]{betamount}[/] on {bettypestr}\nLanded on {color_number(spinnum)}\n{outcome}" 
            console.print(Panel.fit(text, title="Result", border_style=border))                              
            
            restart = input("Press enter to play again or 'r' or 'R' to repeat your bet: ")
            if restart.lower().strip() == "r":
                bet()
    console.clear()
    console.print()
    console.print(Panel("1. Pick what to bet on\n2. Choose how many chips\n3. Press Enter to spin", title="How to play", expand=False))
    console.input("[dim]Press Enter to start...[/]")
    while chips > 0: 
        clearscreen()
        #SHOW CHIPS
        chips_header()
        print_history(history)
        
       # show_menu()
        print()
        choices = [
            questionary.Choice("Red", value=1),
            questionary.Choice("Black", value=2),
            questionary.Choice("Odd", value=3),
            questionary.Choice("Even", value=4),
            questionary.Choice("Low (1-18)", value=5),
            questionary.Choice("High (19-36)", value=6),
            questionary.Choice("Single number", value=7),
    ]
        print()
        bettype = questionary.select("Place your bet", choices=choices, style=casino_style).unsafe_ask()
    
    
                

        #Asks user for number if picked 7 for bettype
        if bettype == 7:
            print()
            usernum = questionary.text("Pick a number (0-36 or 00):", validate=check_usernum, style=casino_style).unsafe_ask()
        

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


        print()
        answer = questionary.text(f"Bet amount (you have {chips:,}):",validate=check_betamount, style=casino_style).unsafe_ask()

        if answer is None:
            print("Cancelled")
        else:
            betamount = int(answer)
            print(f"You bet {betamount}")
        
        bet()
    
    else:
        game_over()















except KeyboardInterrupt:
    print("\nExiting")
