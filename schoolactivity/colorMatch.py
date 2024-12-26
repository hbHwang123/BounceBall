import sys, pygame
import random
from pygame.locals import *

pygame.init()

display = pygame.display.set_mode((1280,720))
running = True
game_started = False

#==========폰트==========#
defaultFont = pygame.font.SysFont(None,25)
#==========이미지 모음==========#
image_start = pygame.image.load("C:\PythonProject\schoolactivity\colorMatch_image\start.png")
image_start_getPressed = pygame.image.load("C:\PythonProject\schoolactivity\colorMatch_image\start_pressed.png")
#==========색상 모음==========#
white = (255,255,255)

#====================게임 코드====================#
def randomRGBCode():
    R,G,B = random.randint(1,255),random.randint(1,255),random.randint(1,255)
    return (R,G,B)

#==========실행 코드==========#
while running:
    #==========배경 색칠==========#
    display.fill(white)
    #==========게임 종료==========#
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    #==========로비 화면==========#
    if not game_started:
        #==========버튼 출력==========#
        x,y = pygame.mouse.get_pos()
        display.blit(image_start,(320,120))
        if pygame.Rect(531,313,205,96).collidepoint(x,y):
            display.blit(image_start_getPressed,(320,120))
        #==========이벤트 감지==========#
        for event in pygame.event.get():
            #==========버튼 클릭 감지==========#
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    game_started = True
    #==========게임 화면==========#
    else:
        None
    #==========출력(개발용)==========#
    display.blit(defaultFont.render(str(pygame.mouse.get_pos()),True,(0,0,0)),(0,20)) #마우스 좌표#
    #==========화면 업데이트==========#
    pygame.display.update()
    pygame.time.Clock().tick(60)
