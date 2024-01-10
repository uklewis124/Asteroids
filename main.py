import pygame
from pygame.locals import *
import math

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()
fps = 60
screen.fill((0, 0, 0))

class Player:
    def __init__(self):
        self.original_image = pygame.image.load("res/player.png").convert_alpha()
        self.angle = 0
        self.png = pygame.transform.rotate(self.original_image, self.angle)
        self.x = 30
        self.y = 70
        self.points = [[self.x, self.y], [self.x - 10, self.y - 20], [self.x + 10, self.y - 20]]
        self.color = (180, 255, 200)
        self.speed = 5


    def draw(self):
        pygame.draw.polygon(screen, self.color, self.points)
    def move(self, direction=0):
        print("Moving")
        self.x += math.sin(math.radians(self.angle)) * self.speed
        self.y -= math.cos(math.radians(self.angle)) * self.speed

player = Player()
player.draw()


running = True
direction = 0
while running:
    screen.fill((0,0,0))
    move = False
    # See if a key is presssed
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        move = True
    if keys[K_a]:
        direction += 1
    if keys[K_d]:
        direction -= 1
    
    # Move the player
    if move:
        player.move(direction)
    
    # End of section
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.blit(player.png, (player.x, player.y))
    pygame.display.flip()
    clock.tick(fps)