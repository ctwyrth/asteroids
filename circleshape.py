import pygame

class CircleShape(pygame.sprite.Sprite):
  def __init__(self, x, y, radius):
    if hasattr(self, "containers"):
      super().__init__(self.containers)
    else:
      super().__init__()
    
    self.position = pygame.Vector2(x, y)
    self.velocity = pygame.Vector2(0, 0)
    self.radius = radius
  
  def draw(self, screen):
    pass

  def update(self, dt):
    pass

  def collisions(self, object):
    distance = pygame.Vector2.distance_to(self.position, object.position)
    combined_radius = self.radius + object.radius

    if combined_radius >= distance:
      return True
    
    return False