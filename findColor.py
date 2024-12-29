import pygame, sys
from pygame.locals import *
from random import *
pygame.init()
#==========색상코드==========#
WHITE = (255,255,255)
BLACK = (0,0,0)
color = (0,0,0)
answercolor = (0,0,0)
#==========폰트==========#
defaultFont = pygame.font.SysFont(None,25)

DISPLAY = pygame.display.set_mode([600,400])
pygame.display.set_caption("FindColor")
clock = pygame.time.Clock()
running = True
bigFont = pygame.font.Font('NanumBarunGothicBold.otf', 100)
font = pygame.font.Font('NanumBarunGothicBold.otf', 20)
scene = "lobby"
levelconst = 0
start = 1
answer = (0,0)

def drawRect():
    global color
    global answercolor
    x = 155
    y = 55
    for i in range(5):
        X = x + i*60
        for j in range(5):
            Y = y + j*60
            pygame.draw.rect(DISPLAY,color,[X,Y,50,50])
    global answer
    X = x + answer[0]*60
    Y = y + answer[1]*60
    pygame.draw.rect(DISPLAY,answercolor,[X,Y,50,50])

score = 0

while running:
    if scene == "lobby":
        DISPLAY.fill(WHITE)
        DISPLAY.blit(bigFont.render("다른 색깔 찾기", True, (0, 0, 0)), (15, 50))
        DISPLAY.blit(font.render("시작->", True, (0, 0, 0)), (200, 190))
        DISPLAY.blit(font.render("<-시작", True, (0, 0, 0)), (340, 190))
        DISPLAY.blit(font.render("시간제한 : 30초", True, (0, 0, 0)), (230, 300))
        a = randint(50,200)
        b = randint(50,200)
        c = randint(50,200)
        color = (a,b,c)
        pygame.draw.rect(DISPLAY,color,[275,175,50,50])
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONUP:
                if event.button == 1 and pygame.Rect(275,175,50,50).collidepoint(x,y):
                    pygame.time.set_timer(USEREVENT,1000)
                    counter, text = 30, " 남은 시간: ".rjust(1)+'30'.rjust(1)
                    scene = "inGame"
                    stage = 0
                    gameStart = True
                    scene = "gameplay"
    elif scene == "gameplay":
        DISPLAY.fill(WHITE)
        if start:
            level = 0
            score = 0
            start = 0
            levelUp = 1
        if levelUp:
            if level == 10:
                None
            else:
                level += 1
            a = randint(50,200)
            b = randint(50,200)
            c = randint(50,200)
            color = (a,b,c)
            levelconst = ((10-level)*3+5)*choice([1,-1])
            answercolor = (a+levelconst,b+levelconst,c+levelconst)
            levelUp = 0
            answer = (randint(0,4),randint(0,4))
            rect = pygame.Rect(155+answer[0]*60,55+answer[1]*60,50,50)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONUP and event.button == 1 and rect.collidepoint(event.pos):
                levelUp = True
                score += 1
            elif event.type == USEREVENT:
                counter -= 1
                text = " 남은 시간: ".rjust(1) + str(counter).rjust(1)
        if int(counter)%2 == 0:
            text_color = (200,0,0)
        else:
            text_color = (0,0,0)
        text_score = " 맞춘 개수: ".rjust(1) + str(score).rjust(1)
        DISPLAY.blit(font.render(text, text_color, (0, 0, 0)), (5, 5))
        DISPLAY.blit(font.render(text_score, True, (0, 0, 0)), (5, 30))
        drawRect()
        if counter == 0:
            scene = "result"
    elif scene == "result":
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        DISPLAY.fill(WHITE)
        DISPLAY.blit(bigFont.render("게임 종료", True, (0, 0, 0)), (100, 100))
        DISPLAY.blit(font.render(text_score, True, (0, 0, 0)), (240, 250))
    pygame.display.update()

