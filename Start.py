import pygame
import subprocess
import sys

pygame.init()

width = 1000
height = 770
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Start Frame")

background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (width, height))
background_rect = background_image.get_rect()

gamei=pygame.image.load("barelbreakouttext.png")
gamei_rect=gamei.get_rect()




board=pygame.image.load("board.png")
b12=520
b22=80
boardl=pygame.transform.scale(board,(b12,b22))

x=250
y=200
gamei_rect.topleft = (x, y)

x1=300//2
y1=250//2 + 100
mon=pygame.image.load("kong.png")
moni1=pygame.transform.scale(mon,(150,150))

start_image = pygame.image.load("startbutton.png")
button_x = width // 2
button_y = height // 2 + 100
image_rect = start_image.get_rect(center=(button_x, button_y))

exit=pygame.image.load("exit.png")
exit1=pygame.transform.scale(exit,(100,100))
exit_rect = exit.get_rect(topleft=(800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if image_rect.collidepoint(event.pos):
                subprocess.Popen(["python","MainGame.py"])
            elif exit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    screen.fill((0, 0, 0))

    
    screen.blit(background_image, background_rect)
    
    screen.blit(boardl,(250,210))
    screen.blit(moni1,(420,270))
    screen.blit(gamei,gamei_rect)
    screen.blit(start_image, image_rect)
    screen.blit(exit1,(800,600))
    
    pygame.display.flip()

pygame.quit()
