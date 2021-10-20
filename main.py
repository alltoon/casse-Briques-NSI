# importer les librairies
import pygame
from raquette import Raquette
from brique import Brique
from balle import Balle

pygame.init()  # initialisation de PyGame

# Définition des couleurs

couleurs = [(0, 0, 0), (255, 0, 0), (255, 255, 0), (255, 255, 255), (255, 100, 0),
            (121, 28, 248), (108, 2, 119), (223, 128, 255)]
# couleurs[0] = noir, couleurs[1] = rouge, couleurs[2] = jaune, couleurs[3] = blanc, couleurs[4] = orange,
# couleurs[5] = bleu, couleurs[6] = zinzolin, couleurs[7] = rose

# Mise en place de la fenêtre & de quelques détails

taille = (800, 600)  # taille de la fenêtre
# détermine la taille initiale de la fenêtre et sa possibiliée de redimentionement
# fenetre = pygame.display.set_mode(taille, pygame.RESIZABLE)
# détermine la taille initiale de la fenêtre
fenetre = pygame.display.set_mode(taille)

jeu = True  # Permettre au joueur de quitter le jeu par la suite
score, vies = 0, 5  # initialisation de la variable score et vie

temps = pygame.time.Clock()  # contrôle de la vitesse de refresh

# Liste contenant nos sprites (classes) qu'on va utiliser

liste_sprites = pygame.sprite.Group()

# Création de la raquette

raquette = Raquette(couleurs[7], 100, 10)  # création de notre raquette (couleur + taille)
raquette.rect.x = 350  # emplacement de spawn de la raquette
raquette.rect.y = 560  # emplacement de spawn de la raquette

# Création de la balle

balle = Balle(couleurs[3], 20)  # création de notre balle (couleur, diametre)
balle.rect.x = 345
balle.rect.y = 195

briques = pygame.sprite.Group()
for y in range(3):
    for i in range(7):
        brique = Brique(couleurs[6], 80, 30)
        brique.rect.x = 60 + i * 100
        brique.rect.y = 60 + y * 50
        liste_sprites.add(brique)
        briques.add(brique)
liste_sprites.add(raquette)  # on ajoute notre raquette à notre liste de sprites
liste_sprites.add(brique)
liste_sprites.add(balle)

# Programme principal

while jeu:

    # Ouverture de la fenêtre Pygame
    # fenetre = pygame.display.set_mode((800, 600))

    # Chargement et collage du fond
    fond = pygame.image.load("ressources/bgg.jpg").convert()
    fenetre.blit(fond, (0, 0))

    # écouter le joueur
    for event in pygame.event.get():  # écouter les events
        if event.type==pygame.QUIT:  # si l'event = quitter le jeu
            jeu = False  # permet au joueur de quitter le jeu

    # bouger notre raquette
    touches = pygame.key.get_pressed()  # écouter la pression d'une touche
    if touches[pygame.K_LEFT]:  # si la touche gauche est pressée
        raquette.gauche(7)  # aller à gauche de 5 pixels
    if touches[pygame.K_RIGHT]:  # si la touche droite est pressée
        raquette.droite(7)  # aller à droite de 5 pixels

    liste_sprites.update()  # update notre liste de sprites

    # Vérifie si la balle touche un des murs (4)
    if balle.rect.x >= 760:  # mur de droite
        balle.velocity[0] = -balle.velocity[0]
    if balle.rect.x <= 0:  # mur du haut
        balle.velocity[0] = -balle.velocity[0]
    if balle.rect.y > 590:  # mur du bas
        balle.velocity[1] = -balle.velocity[1]
        vies -= 1
        if vies==0:
            police = pygame.font.Font(None, 74)  # Gère la police du texte de fin
            texte = police.render("PERDU", 1, couleurs[3])
            texte_score = police.render("Votre Score :" + str(score), 1, couleurs[3])  # Affiche le texte de fin
            fenetre.blit(texte, (275, 300)), fenetre.blit(texte_score, (220, 400))  # Positione le texte de fin
            pygame.display.flip()
            pygame.time.wait(3000)

            jeu = False  # arrète le jeux
    if balle.rect.y < 40:  # mur de gauche
        balle.velocity[1] = -balle.velocity[1]

    # Détecte les collisions entre la balle et la raquette
    if pygame.sprite.collide_mask(balle, raquette):
        balle.rect.x -= balle.velocity[0]
        balle.rect.y -= balle.velocity[1]
        balle.rebond()

    # Détecte si la balle touche une des briques
    collision_briques = pygame.sprite.spritecollide(balle, briques, False)
    for brique in collision_briques:
        balle.rebond()
        score += 1
        brique.kill()  # casse la brique
        if len(briques)==0:
            police = pygame.font.Font(None, 74)  # indentation de la police
            text = police.render("Niveau Réussi Bravo", 1, couleurs[3])  # affichage du message de fin
            fenetre.blit(text, (200, 300))  # positionement du message de fin
            pygame.display.flip()
            pygame.time.wait(3000)  # temps d'affichage du message de fin

            # Arrête le jeu
            jeu = False
    # créer l'écran
    # fenetre.fill(noir)  # fond noir

    police = pygame.font.Font(None, 34)  # indentation de la police
    text = police.render("Score: " + str(score), 1, couleurs[3])  # affichage du score
    fenetre.blit(text, (500, 10))  # positionement du score
    text = police.render("Vies: " + str(vies), 1, couleurs[3])  # affichage du compteur de vies
    fenetre.blit(text, (650, 10))  # positionement du compteur de vies

    # Apparition de nos classes (raquette, briques, balle..)

    liste_sprites.draw(fenetre)  # tout dessiner

    # refresh l'écran
    pygame.display.flip()

    # FPS
    temps.tick(130)

pygame.quit()
