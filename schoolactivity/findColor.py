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


while running:
    if scene == "lobby":
        DISPLAY.fill(WHITE)
        pygame.draw.rect(DISPLAY,BLACK,[275,175,50,50])
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONUP:
                if event.button == 1 and pygame.Rect(275,175,50,50).collidepoint(x,y):
                    scene = "gameplay"
    elif scene == "gameplay":
        DISPLAY.fill(WHITE)
        if start:
            level = 0
            life = 3
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
        DISPLAY.blit(defaultFont.render(str(levelconst),True,(0,0,0)),(0,20)) #마우스 좌표#
        drawRect()
    elif scene == "result":
        None
    pygame.display.update()

