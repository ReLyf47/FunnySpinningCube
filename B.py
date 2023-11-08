import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time
import random

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 1, 5, 4),
    (2, 3, 7, 6),
    (0, 3, 7, 4),
    (1, 2, 6, 5)
)

def get_rainbow_color(t):
    frequency = 5.0
    r = (math.sin(frequency * t) + 1) / 2
    g = (math.sin(frequency * t + 2) + 1) / 2
    b = (math.sin(frequency * t + 4) + 1) / 2
    return r, g, b

def draw_cube(t):
    glBegin(GL_QUADS)
    for i, face in enumerate(edges):
        glColor3fv(get_rainbow_color(t))
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    t = 0
    rotation_angle = 0
    rotation_axis = [0, 1, 1]

    # Initialize the mixer and load the audio file
    pygame.mixer.init()
    pygame.mixer.music.load("Song.mp3")  # Replace with your audio file

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Use a time-dependent function to control rotation speed
        rotation_speed = 5 * math.sin(0.1 * t)

        # Randomly change the rotation axis direction
        if random.random() < 0.01:
            rotation_axis = [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)]

        glRotatef(rotation_speed, *rotation_axis)  # Rotate the cube
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube(t)
        pygame.display.flip()

        # Play the audio file (looping)
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)  # -1 makes it loop

        pygame.time.wait(10)
        t = time.time()

if __name__ == "__main__":
    main()
