import random
import sys
import pygame
from pygame.locals import*

FPS=32
SCREENWIDTH=289
SCREENHEIGHT=511
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY=SCREENHEIGHT*0.8
GAME_SPRITES={}
GAME_SOUND={}
PLAYER='gallery/sprites/bird.png'
BACKGROUND='gallery/sprites/bg.png'
PIPE='gallery/sprites/pipe.png'


def welcomscreen():
    """
    show welcome screen
    """
    playerx=int(SCREENWIDTH/5)
    playery=int(SCREENHEIGHT-GAME_SPRITES['player'].get_height())/2
    messagex=int(SCREENWIDTH-GAME_SPRITES['message'].get_width())/2
    messagey=int(SCREENHEIGHT*0.13)
    basex==0
    while True:
        for event in pygame.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type==KEYDOWN and (event.type==K_SPACE or event.type==K_UP):
                return
            else:
                screen.blit(GAME_SPRITES['BACKGROUND'],(0,0))
                screen.blit(GAME_SPRITES['PLAYER'],(playerx,playery))
                screen.blit(GAME_SPRITES['MESSAGE'],(messagex,messagey))
                screen.blit(GAME_SPRITES['BASE'],(basex,GROUNDY))
                pygam.dislay.update()
                FPSCLOCK.tick(FPS)

def main():
    score=0
    playerx=int(SCREENWIDTH/5)
    playery=int(SCREENWIDYH/2)
    basex=0

def getrandompipe():
    







    


if __name__=="__main__":
    pygame.init()
   # FPSCLOCK=pygame.time.clock(),
    pygame.display.set_caption("flappy bird by saurav")
    GAME_SPRITES['numbers']=(
        pygame.image.load(' gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallerry/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha()
    )

    GAME_SPRITES['message']=pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base']=pygame.image.load().convert_alpha()
    GAME_SPRITES['pipe']=(
    pygame.transform.rotate(pygame.image.load(PIPE).covert.alpha(),180),
    pygame.image.load(PIPE).convert_alpha()
    )

#GAME_SOUND['DIE']=pygame.mixer.sound(gallery)
#GAME_SOUND['hit']=pygame.mixer.sound(gallery)
#GAME_SOUND['point']=pygame.mixer.sound(gallery)
#GAME_SOUND['smooth']=pygame.mixer.sound(gallery)
#GAME_SOUND['wing']=pygame.mixer.sound(gallery)

GAME_SPRITES['background']=pygame.image.load(BACKGROUND).convert()
GAME_SPRITES['player']=pygame.image.load(PLAYER).convert_alpha()

while true:
    welcomescreen()
    maingame()