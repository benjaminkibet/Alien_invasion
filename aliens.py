import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a fleet of aliens."""

    def __init__(self, ai_settings, screen):
        # Initialize the alien and its starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and its attributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each alien at the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    

    def update(self):
        """Update the alien's position."""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        elif self.rect.left <= 0:
            return  True    


    def blitme(self):
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)
