import pygame  # importer pygame car sinon son appel n'est pas reconnu dans la classe
from random import randint

noir = (0, 0, 0)  # définition de la couleur noir pour la même raison


class Balle(pygame.sprite.Sprite):  # notre classe balle
    def __init__(self, couleur, rayon):
        super().__init__()

        self.image = pygame.Surface([rayon * 2, rayon * 2])
        self.image.fill(noir)   # image de fond en noir
        self.image.set_colorkey(noir)

        pygame.draw.circle(self.image, couleur, [rayon, rayon], rayon)      # On dessine le cercle
        self.velocity = [randint(4, 5), randint(-8, 8)]     # on set la direction de la balle aléatoirement

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def rebond(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
