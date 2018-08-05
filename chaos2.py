import pygame
import random
import sys
import string


WIDTH = 800
HEIGHT = 600
FRAMES = 25


# Color Definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# Pygame init
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chaos Game")
clock = pygame.time.Clock()


class Point:

    label_index = 0
    offset = 35

    def __init__(self, position):
    
        self.x = position[0]
        self.y = position[1]
        self.radius = 10
        
        # Label
        self.font_name = "freesansbold.ttf"
        self.font_size = 40
        self.label_alphanumeric = "{}{}".format(string.ascii_uppercase, string.digits)[Point.label_index]
        self.label_text = pygame.font.Font(self.font_name, self.font_size)
        self.label_surface = self.label_text.render(self.label_alphanumeric, True, black)
        self.label_rect = self.label_surface.get_rect()
        self.label_offset_x, self.label_offset_y = self.set_label_offset()
        self.label_rect.center = (self.x + self.label_offset_x, self.y + self.label_offset_y)
        
        # Increment 'label_index' for next point
        Point.label_index += 1
        
        
    def display(self):
        '''
        Draw the point on the screen. A point consists of a dot and an 
        alphanumeric label.
        '''
        
        # Display the dot
        pygame.draw.circle(display, red, (self.x, self.y), self.radius)
        
        # Display label
        display.blit(self.label_surface, self.label_rect)
        
        
    def set_label_offset(self):
        '''
        Positions the label on a point based on the position of the point on
        the screen.
        '''
        
        # x-coordinate
        if self.x > 0 and self.x < WIDTH / 2:
            x = -Point.offset
            
        elif self.x > WIDTH / 2 and self.x < WIDTH:
            x = Point.offset
        else:
            x = 0
        
        # y-coordinate
        if self.y > 0 and self.y < HEIGHT / 2:
            y = -Point.offset
        elif self.y > HEIGHT / 2 and self.y < HEIGHT:
            y = Point.offset
        else:
            y = 0

        return x, y


points = []

while True:

    # Handle Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONUP:
            point = Point(pygame.mouse.get_pos())
            points.append(point)

    display.fill(white)
    
    # Draw points
    for point in points:
        point.display()

    pygame.display.update()
    clock.tick(FRAMES)
