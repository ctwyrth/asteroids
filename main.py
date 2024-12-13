import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  pygame.init()
  dt = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, asteroids)
  AsteroidField.containers = (updatable)
  Shot.containers = (updatable, drawable, shots)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    pygame.Surface.fill(screen, (0, 0, 0))

    since_last = clock.tick(60)
    dt = since_last / 1000

    for item in drawable:
      item.draw(screen)

    for item in updatable:
      item.update(dt)

    for asteroid in asteroids:
      if asteroid.collisions(player):
        sys.exit("Game over!")
      for shot in shots:
        if shot.collisions(asteroid):
          asteroid.split()

    pygame.display.flip()

  pygame.quit()

if __name__ == "__main__":
  main()