import numpy as np
import pygame
from math import *

def connect_points(i, j, points, color):
    pygame.draw.line(screen, color, ((points[i][0]), (points[i][1])), (points[j][0], points[j][1]))

# ---------------- Constants ------------------------------------
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 127, 0)
PURPLE = (127, 0, 255)
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

projected_points = [
    [n, n] for n in range(len(points))
]

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

    rotation_matrix_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)],
    ])

    rotation_matrix_y = np.matrix([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)],
    ])

    rotation_matrix_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1],
    ])

    angle += 0.01

    screen.fill(WHITE)

    i = 0
    # draw points
    for point in points:
        rotated_2D = np.dot(rotation_matrix_z, point.reshape((3, 1)))
        rotated_2D = np.dot(rotation_matrix_y, rotated_2D)
        rotated_2D = np.dot(rotation_matrix_x, rotated_2D)
        projected_2D = np.dot(projection_matrix, rotated_2D)

        x = int(projected_2D[0][0] * scale) + circle_pos[0]
        y = int(projected_2D[1][0] * scale) + circle_pos[1]

        projected_points[i] = [x, y]
        pygame.draw.circle(screen, BLACK, (x, y), 5)
        i += 1

    connect_points(0, 1, projected_points, RED)
    connect_points(4, 5, projected_points, RED)

    connect_points(0, 4, projected_points, BLUE)
    connect_points(1, 5, projected_points, BLUE)


    connect_points(2, 3, projected_points, GREEN)
    connect_points(6, 7, projected_points, GREEN)

    connect_points(2, 6, projected_points, ORANGE)
    connect_points(3, 7, projected_points, ORANGE)

    connect_points(0, 3, projected_points, PURPLE)
    connect_points(1, 2, projected_points, PURPLE)

    connect_points(4, 7, projected_points, PURPLE)
    connect_points(5, 6, projected_points, PURPLE)





    pygame.display.update()

