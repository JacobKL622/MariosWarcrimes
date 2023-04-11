import pygame
from settings import *

#Create classes for level
class Level:
    def__init__(self):

        #level setup
        self.diplay_surface = pygame.display.get_surface()
    
    #Sprite group setup
    self.visible_sprites = pygame.sprite.Group()
    self.active_sprites = pygame.sprite.Group()
    self.collision_sprites = pygame.sprite.Group()
    
    def run(self):
        #Runs game level
        pass