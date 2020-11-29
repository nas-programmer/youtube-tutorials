"""Smooth Jumping"""

#imports
import pygame, sys

WIDTH, HEIGHT = 500, 350

pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(30, 30, 32, 32)
player_speed = 5


def move(rect, x, y):
    rect.x += x
    rect.y += y

#Add gravity
def grav(rect, g_force= 6):
    rect.y += g_force
    if rect.y + rect.h >= HEIGHT:
        rect.y = HEIGHT - rect.h


x, y = 0,0

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = -player_speed
            if event.key == pygame.K_RIGHT:
                x = player_speed
            if event.key == pygame.K_UP:
                y = -20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x = 0
            if event.key == pygame.K_RIGHT:
                x = 0
            if event.key == pygame.K_UP:
                y = 0
        
        
    #Draw
    win.fill((0, 0, 20))
    pygame.draw.rect(win, (255, 24, 10), player)

    #move
    move(player, x= x, y=y)
    grav(player)

    pygame.display.flip()





































































































# """Smooth Jumping in pygame"""

# #Imports
# import pygame, sys


# pygame.init()

# #Screen
# WIDTH, HEIGHT = 500, 350
# win = pygame.display.set_mode((WIDTH, HEIGHT))

# #FPS
# clock = pygame.time.Clock()

# #Player Initialization
# player = pygame.Rect(30, 30, 32, 32)
# player_speed = 5

# #Movement Functions
# def move(rect, x= 0, y= 0):
#     rect.x += x
#     rect.y += y

# def jump(rect):
#     rect.y -= 20 + rect.h

# def calc_grav(rect):
#     rect.y += 6
#     if rect.y+32 >= HEIGHT:
#         rect.y = HEIGHT - 32

# x = 0
# y = 0
# while True:
#     clock.tick(120)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 x = -player_speed
#             if event.key == pygame.K_RIGHT:
#                 x = player_speed
#             if event.key == pygame.K_UP:
#                 y = -20
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT:
#                 x = 0
#             if event.key == pygame.K_RIGHT:
#                 x = 0
#             if event.key == pygame.K_UP:
#                 y = 0

    
        
#     if player.x < -32:
#         player.x = WIDTH
#     elif player.x >= WIDTH:
#         player.x = 0
        
    
#     win.fill((0, 0, 20))
#     pygame.draw.rect(win, (255, 20, 10), player)

#     move(player, x, y)
#     calc_grav(player)
#     pygame.display.flip()

    