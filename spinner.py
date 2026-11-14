import random
import time
import shutil
from rich.live import Live
from rich.rule import Rule
width = shutil.get_terminal_size().columns
delay = 0.05
strwheel = ["00","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36"]
with Live(refresh_per_second=20) as live:
    for i in range(random.randrange(15, 20)):
        n = random.choice(wheelnum)     # fake frame
        live.update(Rule(color_number(n), characters="="))
        time.sleep(delay)
        delay *= 1.15
input()
