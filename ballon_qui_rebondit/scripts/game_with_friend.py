import sys
import pygame
import random
import tkinter as tk
from pygame.locals import QUIT, MOUSEBUTTONDOWN, VIDEORESIZE, MOUSEMOTION
from tkinter import messagebox

pygame.init()

size = width, height = 1200, 740
speed = [5, 5]
plage = pygame.image.load("../img/plage.jpg")

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Jeu de Volley")

ball = pygame.image.load("../img/intro_ball.gif")
ballrect = ball.get_rect(center=(width // 2, height // 2))

pygame.mixer.music.load("../music/musique.mp3")
pygame.mixer.music.play(-1)

sounds = [
    pygame.mixer.Sound("../music/ballon_1.mp3"),
    pygame.mixer.Sound("../music/ballon_2.mp3"),
    pygame.mixer.Sound("../music/ballon_3.mp3"),
]
lose_sound = pygame.mixer.Sound("../music/lose.mp3")
win_sound = pygame.mixer.Sound("../music/yeepee.mp3")

button_color = pygame.Color("deeppink2")
button_rect = pygame.Rect(width // 2 - 50, height // 2 - 25, 100, 50)
font = pygame.font.Font(None, 36)
countdown_font = pygame.font.Font(None, 120)
rules_font = pygame.font.Font(None, 48)
button_text = font.render("Stop", True, (255, 255, 255))
button_text_rect = button_text.get_rect(center=button_rect.center)

clock = pygame.time.Clock()
FPS = 60
slow_factor = 5

player_width = 100
player_height = 20
player_speed = 10

player1 = pygame.Rect(
    width // 2 - player_width // 2, height - 40, player_width, player_height
)
player2 = pygame.Rect(width // 2 - player_width // 2, 20, player_width, player_height)


def resize_elements():
    global button_rect, button_text_rect, width, height
    button_rect = pygame.Rect(width // 2 - 50, height // 2 - 25, 100, 50)
    button_text_rect = button_text.get_rect(center=button_rect.center)


def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


resize_elements()


def show_messagebox(message, win=False):
    root = tk.Tk()
    root.withdraw()
    if win:
        win_sound.play()
    else:
        lose_sound.play()
    result = messagebox.askyesno("Game Over", message + " Voulez-vous rejouer ?")
    if result:
        reset_game()
    else:
        pygame.quit()
        sys.exit()


def show_rules():
    global width, height, screen, game_started
    rules = [
        "Règles du Jeu :",
        "Le joueur 1 (en bas) utilise les flèches pour déplacer sa raquette.",
        "Le joureur 2 (en haut) utilise la souris pour déplacer sa raquette.",
        "Ne laissez pas la balle toucher votre zone !",
        "Le joueur qui laisse tomber la balle perd.",
        "Cliquez pour commencer...",
    ]
    rules_surface = pygame.Surface((width, height))
    rules_surface.set_alpha(230)
    rules_surface.fill("lightpink")
    screen.blit(rules_surface, (0, 0))

    y_offset = 100
    for rule in rules:
        rule_text = rules_font.render(rule, True, (255, 255, 255))
        rule_rect = rule_text.get_rect(center=(width // 2, y_offset))
        screen.blit(rule_text, rule_rect)
        y_offset += 60
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                waiting = False
                game_started = True
                reset_game()
            elif event.type == VIDEORESIZE:
                size = width, height = event.w, event.h
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)
                resize_elements()
                rules_surface = pygame.Surface((width, height))
                rules_surface.set_alpha(230)
                rules_surface.fill("lightpink")
                screen.blit(rules_surface, (0, 0))
                y_offset = 100
                for rule in rules:
                    rule_text = rules_font.render(rule, True, (255, 255, 255))
                    rule_rect = rule_text.get_rect(center=(width // 2, y_offset))
                    screen.blit(rule_text, rule_rect)
                    y_offset += 60
                pygame.display.flip()


def reset_game():
    global ballrect, speed, game_started, countdown_start
    ballrect.center = (width // 2, height // 2)
    speed = [5, 5]
    game_started = False
    countdown_start = pygame.time.get_ticks()


def move_ball():
    global ballrect, speed
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0:
        show_messagebox("Le joueur 1 gagne !", win=True)
    if ballrect.bottom > height:
        show_messagebox("Le joueur 2 gagne !")


def check_collision():
    global speed
    if ballrect.colliderect(player1) or ballrect.colliderect(player2):
        speed[1] = -speed[1]


game_started = False
countdown_start = pygame.time.get_ticks()

show_rules()

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
        elif event.type == MOUSEMOTION:
            player2.x = event.pos[0] - player_width // 2
            player2.x = max(player2.x, 0)
            player2.x = min(player2.x, width - player_width)

    if not game_started:
        current_time = pygame.time.get_ticks()
        countdown = 3 - (current_time - countdown_start) // 1000
        if countdown <= 0:
            game_started = True
        else:
            screen.blit(pygame.transform.scale(plage, (width, height)), (0, 0))
            countdown_text = countdown_font.render(str(countdown), True, (255, 0, 0))
            countdown_rect = countdown_text.get_rect(center=(width // 2, height // 2))
            screen.blit(countdown_text, countdown_rect)
            pygame.display.flip()
            clock.tick(FPS)
            continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player1.left > 0:
        player1.x -= player_speed
    if keys[pygame.K_RIGHT] and player1.right < width:
        player1.x += player_speed

    move_ball()
    check_collision()

    screen.blit(pygame.transform.scale(plage, (width, height)), (0, 0))
    pygame.draw.rect(screen, (0, 0, 255), player1)
    pygame.draw.rect(screen, (255, 0, 0), player2)
    screen.blit(ball, ballrect)

    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_text_rect)

    pygame.display.flip()
    clock.tick(FPS)
