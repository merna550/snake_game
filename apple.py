# apple.py

import pygame
from pygame.locals import *
import random
from game_constants import SIZE, BACKGROUND_COLOR

class Apple:
  def __init__(self, parent_screen):
    self.parent_screen = parent_screen
    self.image = pygame.image.load("resources/apple.jpg").convert()
    self.x = SIZE*3
    self.y = SIZE*3
    
  def draw(self):
    self.parent_screen.blit(self.image, (self.x, self.y))
    pygame.display.flip()
  
  def move(self):
    self.x = random.randint(0, 24)*SIZE
    self.y = random.randint(0, 19)*SIZE
    
    