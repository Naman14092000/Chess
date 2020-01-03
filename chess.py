import pygame
from pygame.locals import *
import re
pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height))

Board = pygame.image.load("images/chess2.jpeg")
cross = pygame.image.load("images/cross.png")
whiteoot = pygame.image.load("images/whiteoot.png")
whiteghoda = pygame.image.load("images/whiteghoda.png")
whitehathi = pygame.image.load("images/whitehathi.png")
whitewazir = pygame.image.load("images/whitewazir.png")
whiteraja = pygame.image.load("images/whiteraja.png")
whitepyada = pygame.image.load("images/whitepyada.png")
blackoot = pygame.image.load("images/blackoot.png")
blackghoda = pygame.image.load("images/blackghoda.png")
blackhathi = pygame.image.load("images/blackhathi.png")
gameover = pygame.image.load("images/gameover.png")
blackwazir = pygame.image.load("images/blackwazir.png")
blackraja = pygame.image.load("images/blackraja.png")
blackpyada = pygame.image.load("images/blackpyada.png")
check = pygame.mixer.Sound("images/check.wav")
check.set_volume(2)
tap = pygame.mixer.Sound("images/tap1.wav")
tap.set_volume(2)
pygame.mixer.music.load('images/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

res = [1] * 64
res1 = [2] * 64
whiteoot1pos = [150, 0]
whiteoot2pos = [375, 0]
whiteghoda1pos = [75, 0]
whiteghoda2pos = [450, 0]
whitehathi1pos = [0, 0]
whitehathi2pos = [525, 0]
whitewazirpos = [300, 0]
whiterajapos = [225, 0]
whitepyada1pos = [0, 75]
whitepyada2pos = [75, 75]
whitepyada3pos = [150, 75]
whitepyada4pos = [225, 75]
whitepyada5pos = [300, 75]
whitepyada6pos = [375, 75]
whitepyada7pos = [450, 75]
whitepyada8pos = [525, 75]

blackoot1pos = [150, 525]
blackoot2pos = [375, 525]
blackghoda1pos = [75, 525]
blackghoda2pos = [450, 525]
blackhathi1pos = [0, 525]
blackhathi2pos = [525, 525]
blackwazirpos = [225, 525]
blackrajapos = [300, 525]
blackpyada1pos = [0, 450]
blackpyada2pos = [75, 450]
blackpyada3pos = [150, 450]
blackpyada4pos = [225, 450]
blackpyada5pos = [300, 450]
blackpyada6pos = [375, 450]
blackpyada7pos = [450, 450]
blackpyada8pos = [525, 450]
players_pos = []
players_pos.append(["whitepyada", whitepyada1pos])
players_pos.append(["whitepyada", whitepyada2pos])
players_pos.append(["whitepyada", whitepyada3pos])
players_pos.append(["whitepyada", whitepyada4pos])
players_pos.append(["whitepyada", whitepyada5pos])
players_pos.append(["whitepyada", whitepyada6pos])
players_pos.append(["whitepyada", whitepyada7pos])
players_pos.append(["whitepyada", whitepyada8pos])
players_pos.append(["blackpyada", blackpyada1pos])
players_pos.append(["blackpyada", blackpyada2pos])
players_pos.append(["blackpyada", blackpyada3pos])
players_pos.append(["blackpyada", blackpyada4pos])
players_pos.append(["blackpyada", blackpyada5pos])
players_pos.append(["blackpyada", blackpyada6pos])
players_pos.append(["blackpyada", blackpyada7pos])
players_pos.append(["blackpyada", blackpyada8pos])
players_pos.append(["whiteoot", whiteoot1pos])
players_pos.append(["whiteoot", whiteoot2pos])
players_pos.append(["blackoot", blackoot1pos])
players_pos.append(["blackoot", blackoot2pos])
players_pos.append(["whiteghoda", whiteghoda1pos])
players_pos.append(["whiteghoda", whiteghoda2pos])
players_pos.append(["blackghoda", blackghoda1pos])
players_pos.append(["blackghoda", blackghoda2pos])
players_pos.append(["whitehathi", whitehathi1pos])
players_pos.append(["whitehathi", whitehathi2pos])
players_pos.append(["blackhathi", blackhathi1pos])
players_pos.append(["blackhathi", blackhathi2pos])
players_pos.append(["whiteraja", whiterajapos])
players_pos.append(["blackraja", blackrajapos])
players_pos.append(["whitewazir", whitewazirpos])
players_pos.append(["blackwazir", blackwazirpos])
turn = 0


def mark():
    for i in players_pos:
        block = int(int(int(i[1][1])/75)*8+int(i[1][0])/75)
        x = re.findall("^white", i[0])
        if (x):
            res[block] = 0
            res1[block] = 0
        else:
            res[block] = 0
            res1[block] = 1

playertype = ["ghoda", "hathi", "oot", "raja", "wazir"]
possiblemove = []
kingSafe = 1

def getmoves(i,position,block):
    possiblemove = []
    if i[0] == "whitepyada":
        if res[block+8] == 1:
            possiblemove.append([position[0], position[1]+75])
        if res[block+7] == 0 and res1[block+7] == 1:
            possiblemove.append([position[0]-75, position[1]+75])
        if res[block+9] == 0 and res1[block+9] == 1:
            possiblemove.append([position[0]+75, position[1]+75])
        #print(possiblemove)
    elif i[0] == "blackpyada":
        if res[block-8] == 1:
            possiblemove.append([position[0], position[1]-75])
        if res[block-7] == 0 and res1[block-7] == 0:
            possiblemove.append([position[0]+75, position[1]-75])
        if res[block-9] == 0 and res1[block-9] == 0:
            possiblemove.append([position[0]-75, position[1]-75])
        #print(possiblemove)
    elif i[0] == "blackghoda":
        if position[0]+75<600 and position[1]+150<600 and (res1[block+17] == 0 or res[block+17] == 1):
            possiblemove.append([position[0]+75, position[1]+150])
        if position[0]-75 >= 0 and position[1]+150<600 and (res1[block+15] == 0 or res[block+15] == 1):
            possiblemove.append([position[0]-75, position[1]+150])
        if position[0]+75<600 and position[1]-150 >= 0 and (res1[block-15] == 0 or res[block-15] == 1):
            possiblemove.append([position[0]+75, position[1]-150])
        if position[0]-75 >= 0 and position[1]-150 >= 0 and (res1[block-17] == 0 or res[block-17] == 1):
            possiblemove.append([position[0]-75, position[1]-150])
        if position[0]+150 < 600 and position[1]+75 < 600 and (res1[block+10] == 0 or res[block+10] == 1):
            possiblemove.append([position[0]+150, position[1]+75])
        if position[0]-150 >=0 and position[1]+75 < 600 and (res1[block+6] == 0 or res[block+6] == 1):
            possiblemove.append([position[0]-150, position[1]+75])
        if position[0]+150 < 600 and position[1]-75 >= 0 and (res1[block-6] == 0 or res[block-6] == 1):
            possiblemove.append([position[0]+150, position[1]-75])
        if position[0]-150 >= 0 and position[1]-75 >= 0 and (res1[block-10] == 0 or res[block-10] == 1):
            possiblemove.append([position[0]-150, position[1]-75])
        #print(possiblemove)
    elif i[0] == "whiteghoda":
        if position[0]+75<600 and position[1]+150<600 and (res1[block+17] == 1 or res[block+17] == 1):
            possiblemove.append([position[0]+75, position[1]+150])
        if position[0]-75 >= 0 and position[1]+150<600 and (res1[block+15] == 1 or res[block+15] == 1):
            possiblemove.append([position[0]-75, position[1]+150])
        if position[0]+75<600 and position[1]-150 >= 0 and (res1[block-15] == 1 or res[block-15] == 1):
            possiblemove.append([position[0]+75, position[1]-150])
        if position[0]-75 >= 0 and position[1]-150 >= 0 and (res1[block-17] == 1 or res[block-17] == 1):
            possiblemove.append([position[0]-75, position[1]-150])
        if position[0]+150 < 600 and position[1]+75 < 600 and (res1[block+10] == 1 or res[block+10] == 1):
            possiblemove.append([position[0]+150, position[1]+75])
        if position[0]-150 >=0 and position[1]+75 < 600 and (res1[block+6] == 1 or res[block+6] == 1):
            possiblemove.append([position[0]-150, position[1]+75])
        if position[0]+150 < 600 and position[1]-75 >= 0 and (res1[block-6] == 1 or res[block-6] == 1):
            possiblemove.append([position[0]+150, position[1]-75])
        if position[0]-150 >= 0 and position[1]-75 >= 0 and (res1[block-10] == 1 or res[block-10] == 1):
            possiblemove.append([position[0]-150, position[1]-75])
        #print(possiblemove)
    elif i[0] == "whitehathi":
        count = 1
        #print("a")
        while block+count*8 < 64:
            possiblemove.append([position[0], position[1]+count*75])
            if res[block+count*8] == 0:
                if res1[block+count*8] == 0:
                    possiblemove.pop()
                break
            count += 1
        count = 1

        while block-count*8 >= 0:
            possiblemove.append([position[0], position[1]-count*75])
            if res[block-count*8] == 0:
                if res1[block-count*8] == 0:
                    possiblemove.pop()
                break
            count += 1
        count = 1

        while position[0]+count*75 < 600:
            possiblemove.append([position[0]+count*75, position[1]])
            if res[block+count*1] == 0:
                if res1[block+count*1] == 0:
                    possiblemove.pop()
                break
            count += 1
        count = 1

        while position[0]-count*75 >= 0:
            possiblemove.append([position[0]-count*75, position[1]])
            if res[block-count*1] == 0:
                if res1[block-count*1] == 0:
                    possiblemove.pop()
                break
            count += 1

        #print(possiblemove)
    elif i[0] == "blackhathi":
        count = 1
        while block+count*8 < 64:
            possiblemove.append([position[0], position[1]+count*75])
            if res[block+count*8] == 0:
                if res1[block+count*8] == 1:
                    possiblemove.pop()
                break
            count += 1
        count = 1

        while block-count*8 >= 0:
            possiblemove.append([position[0], position[1]-count*75])
            if res[block-count*8] == 0:
                if res1[block-count*8] == 1:
                    possiblemove.pop()
                break
            count += 1
        count = 1

        while position[0]+count*75 < 600:
            possiblemove.append([position[0]+count*75, position[1]])
            if res[block+count*1] == 0:
                if res1[block+count*1] == 1:
                    possiblemove.pop()
                break
            count += 1
        count = 1

        while position[0]-count*75 >= 0:
            possiblemove.append([position[0]-count*75, position[1]])
            if res[block-count*1] == 0:
                if res1[block-count*1] == 1:
                    possiblemove.pop()
                break
            count += 1

        #print(possiblemove)
    elif i[0] == "whiteoot":
        count = 1
        while position[0]+count*75 < 600 and position[1]+count*75 < 600:
            possiblemove.append([position[0]+count*75,position[1]+count*75])                
            if res[block+count*9] == 0:
                if res1[block+count*9] == 0:
                    possiblemove.pop()
                break
            count+=1
        count = 1
        while position[0]-count*75>=0 and position[1]-count*75>=0:
            possiblemove.append([position[0]-count*75,position[1]-count*75])
            if res[block-count*9] == 0:
                if res1[block-count*9] == 0:
                    possiblemove.pop()
                break
            count+=1
        count = 1
        while position[0]+count*75 < 600 and position[1]-count*75>=0:
            possiblemove.append([position[0]+count*75,position[1]-count*75])                
            if res[block-count*7] == 0:
                if res1[block-count*7] == 0:
                    possiblemove.pop()
                break
            count+=1
        count = 1
        while position[0]-count*75>=0 and position[1]+count*75<600:
            possiblemove.append([position[0]-count*75,position[1]+count*75])
            if res[block+count*7] == 0:
                if res1[block+count*7] == 0:
                    possiblemove.pop()
                break
            count+=1
        #print(possiblemove)
    elif i[0] == "blackoot":
        count = 1
        while position[0]+count*75 < 600 and position[1]+count*75 < 600:
            possiblemove.append([position[0]+count*75,position[1]+count*75])                
            if res[block+count*9] == 0:
                if res1[block+count*9] == 1:
                    possiblemove.pop()
                break
            count+=1
        count = 1
        while position[0]-count*75>=0 and position[1]-count*75>=0:
            possiblemove.append([position[0]-count*75,position[1]-count*75])
            if res[block-count*9] == 0:
                if res1[block-count*9] == 1:
                    possiblemove.pop()
                break
            count+=1
        count = 1
        while position[0]+count*75<600 and position[1]-count*75>=0:
            possiblemove.append([position[0]+count*75,position[1]-count*75])                
            if res[block-count*7] == 0:
                if res1[block-count*7] == 1:
                    possiblemove.pop()
                break
            count+=1
        count = 1
        while position[0]-count*75>=0 and position[1]+count*75<600:
            possiblemove.append([position[0]-count*75,position[1]+count*75])
            if res[block+count*7] == 0:
                if res1[block+count*7] == 1:
                    possiblemove.pop()
                break
            count+=1
        #print(possiblemove)
    elif i[0] == "whitewazir":
        #print(i)
        count = 1
        while position[1]+count*75 < 600:
            possiblemove.append([position[0], position[1]+count*75])
            #print(possiblemove)
            if res[block+count*8] == 0:
                if res1[block+count*8] == 0:
                    possiblemove.pop()
                break
            count += 1
        count = 1

        while position[1]-count*75 >= 0:
            possiblemove.append([position[0], position[1]-count*75])
            if res[block-count*8] == 0:
                if res1[block-count*8] == 0:
                    possiblemove.pop()
                break
            count += 1
        count = 1
        while position[0]+count*75 < 600:
            possiblemove.append([position[0]+count*75, position[1]])
            if res[block+count*1] == 0:
                if res1[block+count*1] == 0:
                    possiblemove.pop()
                break
            count += 1
        count = 1

        while position[0]-count*75 >= 0:
            possiblemove.append([position[0]-count*75, position[1]])
            if res[block-count*1] == 0:
                if res1[block-count*1] == 0:
                    possiblemove.pop()
                break
            count += 1
        count = 1
        while position[0]+count*75 < 600 and position[1]+count*75 < 600:
            possiblemove.append([position[0]+count*75,position[1]+count*75])                
            #print(position[0]+count*75,position[1]+count*75,res[block+count*9],res1[block+count*9])
            if res[block+count*9] == 0:
                if res1[block+count*9] == 0:
                    possiblemove.pop()
                break
            count+=1
        count = 1
        while position[0]-count*75>=0 and position[1]-count*75>=0:
            possiblemove.append([position[0]-count*75,position[1]-count*75])
            if res[block-count*9] == 0:
                if res1[block-count*9] == 0:
                    possiblemove.pop()
                break
            count+=1
        count = 1
        while position[0]+count*75<600 and position[1]-count*75>=0:
            possiblemove.append([position[0]+count*75,position[1]-count*75])                
            if res[block-count*7] == 0:
                if res1[block-count*7] == 0:
                    possiblemove.pop()
                break
            count+=1
        count = 1
        while position[0]-count*75>=0 and position[1]+count*75<600:
            possiblemove.append([position[0]-count*75,position[1]+count*75])
            if res[block+count*7] == 0:
                if res1[block+count*7] == 0:
                    possiblemove.pop()
                break
            count+=1
        #print(possiblemove)
    elif i[0] == "blackwazir":
        count = 1
        while position[0]+count*75 < 600 and position[1]+count*75 < 600:
            possiblemove.append([position[0]+count*75,position[1]+count*75])                
            if res[block+count*9] == 0:
                if res1[block+count*9] == 1:
                    possiblemove.pop()
                break
            count+=1
        count = 1
        while position[0]-count*75>=0 and position[1]-count*75>=0:
            possiblemove.append([position[0]-count*75,position[1]-count*75])
            if res[block-count*9] == 0:
                if res1[block-count*9] == 1:
                    possiblemove.pop()
                break
            count+=1
        count = 1
        while position[0]+count*75<600 and position[1]-count*75>=0:
            possiblemove.append([position[0]+count*75,position[1]-count*75])                
            if res[block-count*7] == 0:
                if res1[block-count*7] == 1:
                    possiblemove.pop()
                break
            count+=1
        count = 1
        while position[0]-count*75>=0 and position[1]+count*75<600:
            possiblemove.append([position[0]-count*75,position[1]+count*75])
            if res[block+count*7] == 0:
                if res1[block+count*7] == 1:
                    possiblemove.pop()
                break
            count+=1
        count = 1
        while block+count*8 < 64:
            possiblemove.append([position[0], position[1]+count*75])
            if res[block+count*8] == 0:
                if res1[block+count*8] == 1:
                    possiblemove.pop()
                break
            count += 1
        count = 1

        while block-count*8 >= 0:
            possiblemove.append([position[0], position[1]-count*75])
            if res[block-count*8] == 0:
                if res1[block-count*8] == 1:
                    possiblemove.pop()
                break
            count += 1
        count = 1

        while position[0]+count*75 < 600:
            possiblemove.append([position[0]+count*75, position[1]])
            if res[block+count*1] == 0:
                if res1[block+count*1] == 1:
                    possiblemove.pop()
                break
            count += 1
        count = 1

        while position[0]-count*75 >= 0:
            possiblemove.append([position[0]-count*75, position[1]])
            if res[block-count*1] == 0:
                if res1[block-count*1] == 1:
                    possiblemove.pop()
                break
            count += 1
        #print(possiblemove)
    elif i[0] == "whiteraja":
        if position[0]+75<600 and (res[block+1]==1 or res1[block+1] == 1):
            possiblemove.append([position[0]+75,position[1]])
        if position[1]+75<600 and (res[block+8]==1 or res1[block+8] == 1):
            possiblemove.append([position[0],position[1]+75])
        if position[0]-75>=0 and (res[block+1]==1 or res1[block+1] == 1):
            possiblemove.append([position[0]-75,position[1]])
        if position[1]-75>=0 and (res[block+1]==1 or res1[block+1] == 1):
            possiblemove.append([position[0],position[1]-75])
        if position[0]+75<600 and position[1]+75<600 and (res[block+9]==1 or res1[block+9] == 1):
            possiblemove.append([position[0]+75,position[1]+75])
        if position[0]-75>=0 and position[1]-75>=0 and (res[block-9]==1 or res1[block-9] == 1):
            possiblemove.append([position[0]-75,position[1]-75])
        if position[0]-75>=0 and position[1]+75<600 and (res1[block+7]==1 or res[block+7] == 1):
            possiblemove.append([position[0]-75,position[1]+75])
        if position[0]+75<600 and position[1]-75>=0 and (res1[block-7]==1 or res[block-7] == 1):
            possiblemove.append([position[0]+75,position[1]-75])
        #print(possiblemove)
    elif i[0] == "blackraja":
        if position[0]+75<600 and (res[block+1]==1 or res1[block+1] == 0):
            possiblemove.append([position[0]+75,position[1]])
        if position[1]+75<600 and (res[block+8]==1 or res1[block+8] == 0):
            possiblemove.append([position[0],position[1]+75])
        if position[0]-75>=0 and (res[block+1]==1 or res1[block+1] == 0):
            possiblemove.append([position[0]-75,position[1]])
        if position[1]-75>=0 and (res[block+1]==1 or res1[block+1] == 0):
            possiblemove.append([position[0],position[1]-75])
        if position[0]+75<600 and position[1]+75<600 and (res[block+9]==1 or res1[block+9] == 0):
            possiblemove.append([position[0]+75,position[1]+75])
        if position[0]-75>=0 and position[1]-75>=0 and (res[block-9]==1 or res1[block-9] == 0):
            possiblemove.append([position[0]-75,position[1]-75])
        if position[0]-75>=0 and position[1]+75<600 and (res[block+7]==1 or res1[block+7] == 0):
            possiblemove.append([position[0]-75,position[1]+75])
        if position[0]+75<600 and position[1]-75>=0 and (res[block-7]==1 or res1[block-7] == 0):
            possiblemove.append([position[0]+75,position[1]-75])
        #print(possiblemove)
    return possiblemove
def ifcheck(p):
    p1 = [p[1][0],p[1][1]]
    position = tuple(p1)
    block = int(int(int(p[1][1])/75)*8+int(p[1][0])/75)
    possiblemove = getmoves(p,position,block)
    for k in possiblemove:
        for l in players_pos:
            if l[1][0] == k[0] and l[1][1]==k[1] and (l[0] == "whiteraja" or l[0] == "blackraja"):
                global turn
                if (turn == 1 and l[0] == "blackraja") or (turn == 0 and l[0] == "whiteraja"):
                    return 1
    return 0 
def showpossiblemoves(position,turn):
    #print(position)
    turn1 = turn
    for i in players_pos:
        possiblemoves = []
        if(i[1][0] == position[0] and i[1][1] == position[1]):
            block = int(int(int(i[1][1])/75)*8+int(i[1][0])/75)
            possiblemoves=getmoves(i,position,block)
            p = re.findall("^white",i[0])
            #print(p)
            
            if turn == 0 and (p):
                turn1 = turn
            elif turn == 0:                
                break
            p = re.findall("^black",i[0])
            if turn == 1 and (p):                
                turn1 = turn
            elif turn == 1:                
                break
            for j in possiblemoves:
                block = int(int(int(j[1])/75)*8+int(j[0])/75)
                if res[block] == 1:
                    pygame.draw.rect(screen,(80,150,200),(j[0],j[1],75,75))
                else:
                    pygame.draw.rect(screen,(220,69,20),(j[0],j[1],75,75))
                # screen.blit(cross,j)
            x = 0
            y = 0
            while x < 600:
                pygame.draw.line(screen,0,(x,0),(x,600))
                x+=75
            while y < 600:
                pygame.draw.line(screen,0,(0,y),(600,y))
                y+=75
            for p in players_pos:
                if p[0] == "whitepyada":
                    screen.blit(whitepyada, (p[1][0], p[1][1]))
                if p[0] == "blackpyada":
                    screen.blit(blackpyada, (p[1][0], p[1][1]))
                if p[0] == "whitehathi":
                    screen.blit(whitehathi, (p[1][0], p[1][1]))
                if p[0] == "blackhathi":
                    screen.blit(blackhathi, (p[1][0], p[1][1]))
                if p[0] == "whiteoot":
                    screen.blit(whiteoot, (p[1][0], p[1][1]))
                if p[0] == "blackoot":
                    screen.blit(blackoot, (p[1][0], p[1][1]))
                if p[0] == "whiteghoda":
                    screen.blit(whiteghoda, (p[1][0], p[1][1]))
                if p[0] == "blackghoda":
                    screen.blit(blackghoda, (p[1][0], p[1][1]))
                if p[0] == "whiteraja":
                    screen.blit(whiteraja, (p[1][0], p[1][1]))
                if p[0] == "blackraja":
                    screen.blit(blackraja, (p[1][0], p[1][1]))
                if p[0] == "whitewazir":
                    screen.blit(whitewazir, (p[1][0], p[1][1]))
                if p[0] == "blackwazir":
                    screen.blit(blackwazir, (p[1][0], p[1][1]))
            pygame.display.flip()
            #print(possiblemoves)
            while 1:
                flag = 0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit(0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = pygame.mouse.get_pos()
                        p1 = list(position)
                        p1[0] = int(int(p1[0])/75)*75
                        p1[1] = int(int(p1[1])/75)*75
                        position = tuple(p1)
                        for j in possiblemoves:
                            if j[0] == position[0] and j[1] == position[1]:
                                tap.play()
                                block = int(int(int(i[1][1])/75)*8+int(i[1][0])/75)
                                # print(block)
                                res[block] = 1
                                #print(position)
                                #print(players_pos)
                                for k in players_pos:
                                    if k[1][0] == position[0] and k[1][1] == position[1]:
                                        if k[0] == "whiteraja" or k[0] == "blackraja":
                                            pygame.font.init()
                                            font = pygame.font.Font(None, 40)
                                            text = font.render(k[0][0]+k[0][1]+k[0][2]+k[0][3]+k[0][4]+" team Lost", True, (255,0,0))
                                            textRect = text.get_rect()
                                            textRect.centerx = screen.get_rect().centerx
                                            textRect.centery = screen.get_rect().centery+24
                                            screen.fill(0)                                            
                                            screen.blit(gameover,(0,0))
                                            screen.blit(text, textRect)
                                            pygame.display.flip()
                                            global kingSafe
                                            kingSafe = 0
                                        else:
                                            # print(k[0],i[0])
                                            k[0] = i[0]
                                            # print(k[0],i[0])
                                        break
                                i[1][0] = position[0]
                                i[1][1] = position[1]
                                
                                block = int(int(int(i[1][1])/75)*8+int(i[1][0])/75)
                                # print(block)
                                turn1 = int(turn1+1)%2
                                x = re.findall("^white", i[0])
                                if (x):
                                    res[block] = 0
                                    res1[block] = 0
                                else:
                                    res[block] = 0
                                    res1[block] = 1

                                res[block] = 0
                                # print(players_pos)
                                # print(res)
                                break
                        flag = 1
                if (flag):
                    break
            break
            # print(players_pos)
    return turn1
# Python code to remove duplicate elements 
def Remove(duplicate): 
	final_list = [] 
	for num in duplicate: 
		if num not in final_list: 
			final_list.append(num) 
	return final_list 
	


exitcode = 0
while(kingSafe!=0):

    screen.fill(0)

    for x in range(int(width/Board.get_width())):
        for y in range(int(height/Board.get_height())):
            screen.blit(Board, (x*100, y*100))
    x = 0
    y = 0
    while x < 600:
        pygame.draw.line(screen,0,(x,0),(x,600))
        x+=75
    while y < 600:
        pygame.draw.line(screen,0,(0,y),(600,y))
        y+=75

    players_pos = Remove(players_pos)
    for p in players_pos:
        if p[0] == "whitepyada":
            screen.blit(whitepyada, (p[1][0], p[1][1]))
        if p[0] == "blackpyada":
            screen.blit(blackpyada, (p[1][0], p[1][1]))
        if p[0] == "whitehathi":
            screen.blit(whitehathi, (p[1][0], p[1][1]))
        if p[0] == "blackhathi":
            screen.blit(blackhathi, (p[1][0], p[1][1]))
        if p[0] == "whiteoot":
            screen.blit(whiteoot, (p[1][0], p[1][1]))
        if p[0] == "blackoot":
            screen.blit(blackoot, (p[1][0], p[1][1]))
        if p[0] == "whiteghoda":
            screen.blit(whiteghoda, (p[1][0], p[1][1]))
        if p[0] == "blackghoda":
            screen.blit(blackghoda, (p[1][0], p[1][1]))
        if p[0] == "whiteraja":
            screen.blit(whiteraja, (p[1][0], p[1][1]))
        if p[0] == "blackraja":
            screen.blit(blackraja, (p[1][0], p[1][1]))
        if p[0] == "whitewazir":
            screen.blit(whitewazir, (p[1][0], p[1][1]))
        if p[0] == "blackwazir":
            screen.blit(blackwazir, (p[1][0], p[1][1]))
    mark()
    pygame.display.flip()
    moves=[]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            #print(position)
            p1 = list(position)
            p1[0] = int(int(p1[0])/75)*75
            p1[1] = int(int(p1[1])/75)*75
            position = tuple(p1)
            turn=showpossiblemoves(position,turn)
            ch = 0
            for p in players_pos:                
                ch=ifcheck(p)
                if ch == 1 and kingSafe!=0:
                    check.play()
                    break
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
