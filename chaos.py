import pygame
import random
import sys

WIDTH = 800
HEIGHT = 600
FRAMES = 25

class Point:
    def __init__(self):
        self.radius = 10
        self.divisor = 9

        self.lower_bound = 1 / self.divisor
        self.upper_bound = (self.divisor - 1) / self.divisor

point = Point()

# Color Definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

dots = []
dot_size = 1  # In pixels

A = (round(WIDTH / 2), round(point.lower_bound * HEIGHT))
display_a = (A[0], A[1] - 30)

B = (round(point.lower_bound * WIDTH), round(point.upper_bound * HEIGHT))
display_b = (B[0] - 30, B[1])

C = (round(point.upper_bound * WIDTH), round(point.upper_bound * HEIGHT))
display_c = (C[0] + 30, C[1])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text, pos):
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (pos)
    display.blit(TextSurf, TextRect)

start = (400, 300)  # Change starting point here
current_position = start


# Pygame init
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chaos Game")
clock = pygame.time.Clock()

while True:

    # Handle Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    random_number = random.randint(1, 6)

    # The formula for the middle point of a line drawn between two points
    # is M = ((x1 + x2) / 2, (y1 + y2) / 2)

    if random_number in [1, 2]:
        # A[0] == x; A[1] == y
        x = round((A[0] + current_position[0]) / 2)
        y = round((A[1] + current_position[1]) / 2)

        current_position = (x, y)
        dots.append(current_position)

    elif random_number in [3, 4]:
        # B[0] == x; B[1] == y
        x = round((B[0] + current_position[0]) / 2)
        y = round((B[1] + current_position[1]) / 2)

        current_position = (x, y)
        dots.append(current_position)

    elif random_number in [5, 6]:
        # C[0] == x; C[1] == y
        x = round((C[0] + current_position[0]) / 2)
        y = round((C[1] + current_position[1]) / 2)

        current_position = (x, y)
        dots.append(current_position)

    display.fill(white)

    for dot in dots:
        pygame.draw.circle(display, black, dot, dot_size)

    message_display("A", display_a)
    pygame.draw.circle(display, red, A, point.radius)

    message_display("B", display_b)
    pygame.draw.circle(display, red, B, point.radius)

    message_display("C", display_c)
    pygame.draw.circle(display, red, C, point.radius)

    # Starting Position
    pygame.draw.circle(display, green, start, point.radius)


    pygame.display.update()
    clock.tick(FRAMES)

if __name__ == "__main__":
    game_loop()
    pygame.quit()
