# AP CPT


## 1. Setup

```
make a list of all the RED numbers (rednum)

make a list of every pocket: 0, "00", 1-36 (wheelnum)

make an empty list for spin history (history)

set starting chips
```


## 2. Main loop

```
repeat while chips > 0:


    --- BETTING ---

    show chips

    user picks bet type
        (red/black, odd/even, low/high, number)

    if bet type is number:
        user picks which number

    user picks bet amount
        keep asking until valid:
            - it is a number
            - it is greater than 0
            - it is no more than chips


    --- SPIN ---

    press Enter to spin

    x = random choice from (wheelnum)

    add x to (history)


    --- COLOR ---

    if x is 0 or "00":
        color = green
    elif x is in (rednum):
        color = red
    else:
        color = black


    --- RESULT ---

    won = check_win(bet type, user's pick, x)

    if won:
        chips = chips + (bet * payout)
    else:
        chips = chips - bet

    show x, color, and new chips


    --- END CHECK ---

    if chips == 0:
        game over, exit loop
```


## 3. CPT procedure

```
check_win(bet_type, pick, x):

    if x is 0 or "00":
        outside bets lose

    if bet_type is red/black:
        compare color

    if bet_type is odd/even:
        compare x % 2

    if bet_type is low/high:
        compare x to 18

    if bet_type is number:
        compare pick to x

    return True or False
```


## 4. Additions

- colorama
- spinning animation
- good formatting
- history
- hot and cold numbers


## 5. Payouts

| Bet | Covers | Pays |
|---|---|---|
| Straight up | 1 number | 35 to 1 |
| Split | 2 numbers | 17 to 1 |
| Street | 3 numbers | 11 to 1 |
| Corner | 4 numbers | 8 to 1 |
| Six line | 6 numbers | 5 to 1 |
| Column | 12 numbers | 2 to 1 |
| Dozen | 12 numbers | 2 to 1 |
| Red / Black | 18 numbers | 1 to 1 |
| Odd / Even | 18 numbers | 1 to 1 |
| Low / High | 18 numbers | 1 to 1 |


## 6. CPT checklist

- [ ] List (`rednum`) used meaningfully
- [ ] Student-developed procedure with at least one parameter that affects what it does
- [ ] Call to the procedure
- [ ] Selection (if/elif)
- [ ] Iteration (main loop)
- [ ] Video shows input, functionality, and output
- [ ] PPR: screenshots of list and procedure (definition + call)
- [ ] Comments crediting any code I didn't write
