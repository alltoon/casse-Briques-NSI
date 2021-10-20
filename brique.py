import pygame

noir = (0, 0, 0)


class Brique(pygame.sprite.Sprite):
    # creation de la classe brique
    def __init__(self, couleur, longueur, largeur):
        # initialisation de la couleur la longueur et largeur
        super().__init__()
        # constructeur de la classe
        self.image = pygame.Surface([longueur, largeur])
        self.image.fill(noir)
        self.image.set_colorkey(noir)
        pygame.draw.rect(self.image, couleur, [0, 0, longueur, largeur])
        # on permet le dessin notre raquette (rectangle)
        self.rect = self.image.get_rect()
