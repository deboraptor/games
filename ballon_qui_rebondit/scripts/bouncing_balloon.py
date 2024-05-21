import sys
import pygame
import random
import tkinter as tk
from pygame.locals import QUIT, MOUSEBUTTONDOWN, VIDEORESIZE
from tkinter import messagebox

pygame.init()

size = width, height = 1200, 740
speed = [1, 1]
plage = pygame.image.load("../img/plage.jpg")

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Ne faites pas tomber le ballon !")

ball = pygame.image.load("../img/intro_ball.gif")
ballrect = ball.get_rect()

pygame.mixer.music.load("../music/musique.mp3")
pygame.mixer.music.play(-1)

sounds = [
    pygame.mixer.Sound("../music/ballon_1.mp3"),
    pygame.mixer.Sound("../music/ballon_2.mp3"),
    pygame.mixer.Sound("../music/ballon_3.mp3"),
]
lose_sound = pygame.mixer.Sound("../music/lose.mp3")

button_color = pygame.Color("deeppink2")
button_rect = pygame.Rect(width // 2 - 50, height // 2 - 25, 100, 50)
font = pygame.font.Font(None, 36)
button_text = font.render("Stop", True, (255, 255, 255))
button_text_rect = button_text.get_rect(center=button_rect.center)

clock = pygame.time.Clock()
FPS = 60
slow_factor = 5

def resize_elements():
    global button_rect, button_text_rect
    button_rect = pygame.Rect(width // 2 - 50, height // 2 - 25, 100, 50)
    button_text_rect = button_text.get_rect(center=button_rect.center)

def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

resize_elements()

def show_messagebox():
    root = tk.Tk()
    root.withdraw()  
    result = messagebox.askyesno("Game Over", "Le ballon a touché le sol. Voulez-vous rejouer ?")
    if result:
        reset_game()
    else:
        pygame.quit()
        sys.exit()

def reset_game():
    global ballrect, speed
    ballrect.topleft = (width // 2, height // 2)
    speed = [1, -1]  

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
        elif event.type == VIDEORESIZE:
            size = width, height = event.w, event.h
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            resize_elements()

    mouse_pos = pygame.mouse.get_pos()
    if distance(mouse_pos, ballrect.center) < 50: 
        if mouse_pos[0] < ballrect.center[0]:
            speed[0] = abs(speed[0])
        else:
            speed[0] = -abs(speed[0])
        
        if mouse_pos[1] < ballrect.center[1]:
            speed[1] = abs(speed[1])
        else:
            speed[1] = -abs(speed[1])
        
        random.choice(sounds).play()

    for _ in range(slow_factor):
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0:
            speed[1] = -speed[1]
        if ballrect.bottom > height:
            lose_sound.play()  
            show_messagebox()

    screen.blit(pygame.transform.scale(plage, (width, height)), (0, 0))
    screen.blit(ball, ballrect)

    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_text_rect)

    pygame.display.flip()
    clock.tick(FPS)
