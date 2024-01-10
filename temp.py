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
        self.points = [[0, 0], [10, 20], [20, 0]]
        self.color = (180, 255, 200)
        self.speed = 0.5
    
    def draw(self):
        pygame.draw.polygon(screen, self.color, self.points)
    def move(self, direction=0):
        print("move ran")
        counter = 0
        # Grab the center of the triangle
        centre_of_triangle_x = 0
        centre_of_triangle_y = 0
        for point in self.points:
            centre_of_triangle_x += point[0]
            centre_of_triangle_y += point[1]
            counter += 1
        centre_of_triangle_x = centre_of_triangle_x / counter
        centre_of_triangle_y = centre_of_triangle_y / counter

        # Get the points of the triangle
        self.points = self.get_points((centre_of_triangle_x, centre_of_triangle_y), 2, pygame.mouse.get_pos())

        # Move the triangle
        counter = 0
        while counter < len(self.points):
            self.points[counter][0] += self.speed
            counter += 1
    def get_points(self, center, radius, mouse_position):
        # calculate the normalized vector pointing from center to mouse_position
        length = math.hypot(mouse_position[0] - center[0], mouse_position[1] - center[1])
        # (note we only need the x component since y falls 
        # out of the dot product, so we won't bother to calculate y)
        angle_vector_x = (mouse_position[0] - center[0]) / length

        # calculate the angle between that vector and the x axis vector (aka <1,0> or i)
        angle = math.acos(angle_vector_x)

        # list of un-rotated point locations
        triangle = [0, (3 * math.pi / 4), (5 * math.pi / 4)]

        result = list()
        for t in triangle:
            # apply the circle formula
            x = center[0] + radius * math.cos(t + angle)
            y = center[1] + radius * math.sin(t + angle)
            result.append((x, y))

        return result

player = Player()
player.draw()


running = True
while running:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        player.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                print("w")

    player.draw()
    pygame.display.flip()
    clock.tick(fps)
