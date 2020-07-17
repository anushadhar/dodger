import pygame, random
from Ship import *
from Asteroid import *

pygame.init()
screen_info = pygame.display.Info()
# set the width and height to the size of the screen
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size) 
clock = pygame.time.Clock()
color = (30, 0, 30)

NumLevels = 4
Level = 1
AsteroidCount = 0
Player = Ship((20, 200))
#Asteroid = Asteroid((400, 300))
Asteroids = pygame.sprite.Group()

def init():
  global AsteroidCount
  Player.reset((20, 200))
  Asteroids.empty()
  AsteroidCount += 3
  for i in range(AsteroidCount):
    Asteroids.add(Asteroid((400, 300)))

def main(): 
  init()
  while Level <= NumLevels:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          Player.speed[0] = 10
        if event.key == pygame.K_LEFT:
          Player.speed[0] = -10
        if event.key == pygame.K_UP:
          Player.speed[1] = -10
        if event.key == pygame.K_DOWN:
          Player.speed[1] = 10
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
          Player.speed[0] = 0
        if event.key == pygame.K_LEFT:
          Player.speed[0] = 0
        if event.key == pygame.K_UP:
          Player.speed[1] = 0
        if event.key == pygame.K_DOWN:
          Player.speed[1] = 0
    Player.update()
    Asteroids.update()
    #gets_hit = pygame.sprite.spritecollide(Player, Asteroids, False)
    screen.fill(color) 
    Asteroids.draw(screen)
    screen.blit(Player.image, Player.rect)
    pygame.display.flip()

    if Player.checkReset(width):
      init()
    #elif gets_hit:
    #  Player.reset((20, 200))

if __name__ == '__main__':
  main()

