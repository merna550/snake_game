# game.py

import pygame
from pygame.locals import *
import time
from apple import Apple
from snake import Snake
from game_constants import SIZE, BACKGROUND_COLOR


class Game:
  def __init__(self):
    # Initialize the pygame
    pygame.init()
    pygame.display.set_caption("Codebasics Snake And Apple Game")
    pygame.mixer.init()
    self.play_background_music()
    
    # Create a game window
    self.surface = pygame.display.set_mode((1000, 800))
    self.surface.fill(BACKGROUND_COLOR)
    self.snake=Snake(self.surface,1)
    self.snake.draw()
    self.apple=Apple(self.surface)
    self.apple.draw()
    
  def reset(self):
        self.snake = Snake(self.surface,1)
        self.apple = Apple(self.surface)
        
  def play_sound(self,sound):
    sound= pygame.mixer.Sound(f"resources/{sound}.mp3")
    pygame.mixer.Sound.play(sound)
        
  def render_background(self):
    bg = pygame.image.load("resources/background.jpg")
    self.surface.blit(bg,(0,0))
    
    
  def is_collision(self,x1,x2,y1,y2):
    if x1 >= x2 and x1 < x2 + SIZE:
      if y1 >= y2 and y1 < y2 + SIZE:
        return True
    return False 
    
  def play_background_music(self):
    pygame.mixer.music.load("resources/bg_music_1.mp3")
    pygame.mixer.music.play(-1,0)
    
  def play(self):
    self.render_background()
    self.snake.walk()
    self.apple.draw()
    self.display_score()
    pygame.display.flip()
    
    #snake colliding with apple 
    if self.is_collision(self.snake.x[0], self.apple.x, self.snake.y[0], self.apple.y):
      self.play_sound("ding")
      self.snake.increase_length()
      self.apple.move()
      
      
    #snake colliding with itself 
    for i in range(3, self.snake.length):
      if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
          self.play_sound("crash")
          raise "Collision Occured"
        
    # snake colliding with the boundries of the window
    if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
        self.play_sound('crash')
        raise "Hit the boundry error"   
      
  def display_score(self):
    font = pygame.font.SysFont('arial',30)
    score = font.render(f"Score: {self.snake.length}",True,(255,255,255))
    self.surface.blit(score,(800,10))
    
  def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()  
        
        pygame.mixer.music.pause()
    

  def run(self):
    # Game loop
    running = True
    pause = False
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
              if event.key == K_ESCAPE:
                running=False
              if event.key == K_RETURN:
                pygame.mixer.music.unpause()
                pause = False
              if not pause:
                if event.key == K_LEFT:
                  self.snake.move_left()

                if event.key == K_RIGHT:
                  self.snake.move_right()

                if event.key == K_UP:
                  self.snake.move_up()

                if event.key == K_DOWN:
                  self.snake.move_down()
                
            elif event.type == pygame.QUIT:
                running = False 
        
        try:

          if not pause:
            self.play()

        except Exception as e:
          self.show_game_over()
          pause = True
          self.reset()

        time.sleep(.1)

# Quit pygame
pygame.quit()

