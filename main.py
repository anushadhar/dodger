import pygame
from Ship import *

pygame.init()
screen_info = pygame.display.Info()
# set the width and height to the size of the screen
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size) 
clock = pygame.time.Clock()
color = (30, 0, 30)

NumLevels = 4
Level = 1
AsteroidCount = 3
Player = Ship()

def main(): 
  while Level <= NumLevels:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          Player.speed[0] = 10
    Player.update()
    screen.fill(color) 
    screen.blit(Player.image, Player.rect)
    pygame.display.flip()

if __name__ == '__main__':
  main()

