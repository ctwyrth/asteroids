import pygame
from constants import *
from player import Player

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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

    pygame.display.flip()

if __name__ == "__main__":
  main()