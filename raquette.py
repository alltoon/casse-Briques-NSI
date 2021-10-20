import pygame  # importer pygame car sinon son appel n'est pas reconnu dans la classe

noir = (0, 0, 0)  # définition de la couleur noir pour la même raison


class Raquette(pygame.sprite.Sprite):  # notre classe raquette
    def __init__(self, couleur, larg, long):
        super().__init__()
        self.image = pygame.Surface([larg, long])
        self.image.fill(noir)
        self.image.set_colorkey(noir)
        pygame.draw.rect(self.image, couleur, [0, 0, larg, long])  # on permet le dessin notre raquette (rectangle)
        self.rect = self.image.get_rect()

    def gauche(self, pixels):  # méthode pour aller à gauche
        self.rect.x -= pixels
        if self.rect.x < 0:  # vérifier qu'on ne pars pas trop loin
            self.rect.x = 0  # bloque à la limite de la fenêtre

    def droite(self, pixels):  # méthode pour aller à droite
        self.rect.x += pixels
        if self.rect.x > 700:  # vérifier qu'on ne pars pas trop loin
            self.rect.x = 700  # bloque à la limite de la fenêtre
