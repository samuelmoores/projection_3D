import numpy as np
import pygame
from math import *

# ---------------- Constants ------------------------------------
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600


# -------------------- Variables -----------------------------
points = []
scale = 100
circle_pos = [WIDTH/2, HEIGHT/2]

angle = 0

# ---------------------- Matrices ------------------------------
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1, 1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])

# -------------------------- Begin -------------------------------------
pygame.display.set_caption("3D projection in python")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    rotation_matrix_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1],
    ])

    angle += 0.01

    screen.fill(WHITE)

    # draw points
    for point in points:
        rotated_2D = np.dot(rotation_matrix_z, point.reshape((3, 1)))
        projected_2D = np.dot(projection_matrix, rotated_2D)

        x = int(projected_2D[0][0] * scale) + circle_pos[0]
        y = int(projected_2D[1][0] * scale) + circle_pos[1]
        pygame.draw.circle(screen, BLACK, (x, y), 5)

    pygame.display.update()

