# Roulette CPT: Fixes & Additions

## Fixes

### Bugs
- [ ] **1. Repeat bet can crash after many repeats.** `bet()` calls `bet()` inside itself, so every "R" nests one level deeper. After about 1000 repeats Python gives up with a `RecursionError`. *Fix:* have `bet()` return whether the player wants to repeat, and loop in the main area instead of calling itself.
- [ ] **2. "Too big" message gets erased** when repeating a bet you can't afford anymore. It prints and then the screen clears. *Fix:* add a pause after it. Also, at 0 chips the game still offers "repeat" before ending, so check `chips > 0` before showing that option.
- [ ] **3. No way to quit except Ctrl+C.** Non-terminal users won't know that shortcut. *Fix:* add a "Q = cash out" option to the restart prompt that ends the loop and shows game over.

### CPT-related (do before writing the response)
- [ ] **4. Globals in `check_win`.** Pass `color` in as a parameter, make `won` local (or just `return True/False` directly), and stop using `result` as a global.
- [ ] **5. Dead code:** `print("Something went wrong")` and `bettypestr = "Error"` can never run. Delete them.
- [ ] **6. Rename `a, b, c`** in `check_win` to `bettype, spinnum, usernum` so graders can read it without the comment.

### Cleanup
- [ ] **7.** `clearscreen()` → `console.clear()` (fixes Windows), then delete `os`, `shutil`, `width` and `n`.
- [ ] **8.** `strwheel` duplicates `wheelnum`. Build it from the other list: `[str(n) for n in wheelnum]`.
- [ ] **9.** `return;` → `return`
- [ ] **10.** Delete the four `Spin = ...` prints (keep the `color =` lines).
- [ ] **11.** Plain prints that still need Rich: `You bet...`, `That bet is too big`, `GAME OVER`, and the restart `input`.
- [ ] **12.** History overflow: show `history[-15:]` and join with `" "` instead of `", "`.

## Additions

### Easy
- [ ] **1. Hot and cold numbers.** Go through `wheelnum`, count each with `history.count(num)`, and show the 3 most common (hot) and 3 least common (cold) under the history. Good list + iteration material for the CPT.
- [ ] **2. Streak line** (e.g. `Red ×4`). Look back through the history and count how many in a row were the same color.
- [ ] **3. Win sound.** `print("\a", end="")` makes the terminal beep.
- [ ] **4. Game over stats.** Total spins, biggest win and highest chip count. Track the last two the same way as `last_change`.

### Medium
- [ ] **5. Dozens and columns** (both pay 2:1). Dozens: 1–12, 13–24, 25–36. Columns: `num % 3 == 1`, `2` or `0`. Two new table rows + two new `check_win` branches.
- [ ] **6. Help screen.** Typing "H" at the bet prompt shows the intro panel and the table again.
- [ ] **7. Confirm all-in bets.** If `betamount == chips`, ask "Bet everything? (y/n)".

### Harder
- [ ] **8. Save a high score to a file.** Read it at startup and write it at game over (file I/O with `open()`).
- [ ] **9. Split, street and corner bets.** These need a table layout list or grid to know which numbers are next to each other.
- [ ] **10. Several bets on one spin.** Store bets in a list and check each one against the same `spinnum`.

---
**Suggested order:** Fixes #1 → Fixes #4 → Additions #1 (hot/cold)