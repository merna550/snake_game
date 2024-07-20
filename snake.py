# snake.py

import pygame
from pygame.locals import *
from game_constants import SIZE, BACKGROUND_COLOR



class Snake:
  def __init__(self, parent_screen,length):
    self.length = length
    self.parent_screen = parent_screen
    self.block = pygame.image.load("resources/block.jpg").convert()
    self.x, self.y = [SIZE]*length, [SIZE]*length
    self.direction = 'down'
    
  def draw(self):
    
    for i in range(self.length):
      self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
    pygame.display.flip()
    
  def increase_length(self):  
    self.length += 1
    self.x.append(-1)
    self.y.append(-1)
    
  def move_left(self):
    if self.direction != 'right':
      self.direction = 'left'
    
  def move_right(self):
    if self.direction != 'left':
      self.direction = 'right'
    
  def move_up(self):
    if self.direction != 'down':
      self.direction = "up"
    
  def move_down(self):
    if self.direction != 'up':
      self.direction = "down"
    
  def walk(self):
    for i in range(self.length-1,0,-1):
      self.x[i] = self.x[i - 1]
      self.y[i] = self.y[i - 1]
      
    if self.direction == 'left':
      self.x[0] -= SIZE
    elif self.direction == 'right':
      self.x[0] += SIZE
    elif self.direction == 'up':
      self.y[0] -= SIZE
    elif self.direction == 'down':
      self.y[0] += SIZE
    
    
    self.draw()