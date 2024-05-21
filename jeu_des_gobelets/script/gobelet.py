import pygame
import random


pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu des Trois Gobelets")

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

image_gobelet = pygame.image.load("../img/gobelet.png")
image_etoile = pygame.image.load("../img/etoile.png")
image_gobelet_renverse = pygame.image.load("../img/gobelet_renverse.png")

largeur_gobelet = image_gobelet.get_width()
hauteur_gobelet = image_gobelet.get_height()

positions = [
    (largeur_fenetre // 4 - largeur_gobelet // 2, hauteur_fenetre // 2 - hauteur_gobelet // 2),
    (largeur_fenetre // 2 - largeur_gobelet // 2, hauteur_fenetre // 2 - hauteur_gobelet // 2),
    (3 * largeur_fenetre // 4 - largeur_gobelet // 2, hauteur_fenetre // 2 - hauteur_gobelet // 2)
]

gobelets = ["Vide", "Vide", "Objet"]
random.shuffle(gobelets)

def dessiner_gobelets():
    fenetre.fill(BLANC)
    for i in range(3):
        fenetre.blit(image_gobelet, positions[i])
    pygame.display.flip()

def animer_melange():
    for _ in range(10):
        random.shuffle(positions)
        dessiner_gobelets()
        pygame.time.delay(500)

def reset_game():
    random.shuffle(gobelets)
    dessiner_gobelets()

def afficher_victoire():
    font = pygame.font.Font(None, 74)
    text = font.render("Félicitations !", True, NOIR)
    fenetre.fill(BLANC)
    fenetre.blit(text, (largeur_fenetre // 4, hauteur_fenetre // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)

def afficher_defaite():
    font = pygame.font.Font(None, 74)
    text = font.render("Dommage !", True, NOIR)
    fenetre.fill(BLANC)
    fenetre.blit(text, (largeur_fenetre // 3, hauteur_fenetre // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)

reset_game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i in range(3):
                rect = pygame.Rect(positions[i][0], positions[i][1], largeur_gobelet, hauteur_gobelet)
                if rect.collidepoint(x, y):
                    if gobelets[i] == "Objet":
                        fenetre.blit(image_etoile, positions[i])
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        afficher_victoire()
                    else:
                        fenetre.blit(image_gobelet_renverse, positions[i])
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        afficher_defaite()
                    animer_melange()
                    reset_game()

pygame.quit()
