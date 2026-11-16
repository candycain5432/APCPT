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