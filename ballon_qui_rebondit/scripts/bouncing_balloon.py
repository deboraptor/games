import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, VIDEORESIZE

pygame.init()

size = width, height = 1200, 740
speed = [1, 1]
plage = pygame.image.load("../img/plage.jpg")

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Balle qui rebondit !")

ball = pygame.image.load("../img/intro_ball.gif")
ballrect = ball.get_rect()

pygame.mixer.music.load("../music/musique.mp3")
pygame.mixer.music.play(-1)

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

resize_elements()

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

    for _ in range(slow_factor):
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

    screen.blit(pygame.transform.scale(plage, (width, height)), (0, 0))
    screen.blit(ball, ballrect)

    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_text_rect)

    pygame.display.flip()
    clock.tick(FPS)
