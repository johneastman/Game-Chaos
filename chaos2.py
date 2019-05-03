import pygame
from pygame.locals import *
import random
import sys
import string
import math

'''
    Create three dots, labeled A, B, and C, and assign each one two numbers. 
A is assigned 1 and 2; B is assigned 3 and 4; C is assigned 5 and 6. Starting 
Anywhere on the screen, roll a 6-sided die. Make a dot half way between where
you started and the point that is assigned the number you rolled. Repeat this, 
but start at the newly-drawn dot. This procedure will often produce fractal 
patterns. The three-points example -- mentioned above -- produced a Sierpinski 
triangle ( https://en.wikipedia.org/wiki/Sierpinski_triangle ). 
'''


class Point:

    '''
    This class contains information for the points (in red) that are labeled.
    These points dictate the perimiter where the dots will be generated.
    '''

    label_index = 0
    label_chars = string.ascii_uppercase + string.digits
    offset = 35

    def __init__(self, position):
    
        self.x = position[0]
        self.y = position[1]
        self.radius = 10
        
        self.choices_length = 2
        self.choices = list(range(self.choices_length * Point.label_index, (self.choices_length * Point.label_index) + self.choices_length))
        
        # Label
        self.font_name = "freesansbold.ttf"
        self.font_size = 40
        self.label_alphanumeric = Point.label_chars[Point.label_index]
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
        if self.x > 0 and self.x < WIDTH / 3:
            x = -Point.offset
            
        elif self.x > (2 * WIDTH) / 3 and self.x < WIDTH:
            x = Point.offset
        else:
            x = 0
        
        # y-coordinate
        if self.y > 0 and self.y < HEIGHT / 3:
            y = -Point.offset
        elif self.y > (2 * HEIGHT) / 3 and self.y < HEIGHT:
            y = Point.offset
        else:
            y = 0

        return x, y


class Dot:
    '''
    These are the dots that are generated and displayed within the bounds
    of the labeled points. 
    '''
    
    def __init__(self, position, radius):
    
        self.x = position[0]
        self.y = position[1]
        self.radius = radius
        
    def display(self):
        pygame.draw.circle(display, black, (self.x, self.y), self.radius)


def set_points():
    '''
    Allows the user to set the points that will be used for generation
    '''
    
    make_new_point = True
    
    while True:

        # Handle Events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                return
                
            if event.type == pygame.MOUSEBUTTONUP:
            
                point_x, point_y = pygame.mouse.get_pos()
                
                '''
                Deleting Points
                if display.get_at( (point_x, point_y) ) == red:
                    for point in points:
                        if (point_x >= point.x - point.radius and point_x <= point.x + point.radius) or (point_y >= point.y - point.radius and point_y <= point.y + point.radius):
                            point.label_index =- 1
                            points.remove(point)
                '''
                if make_new_point:
                    point = Point( (point_x, point_y) )
                    if point.label_index < len(point.label_chars):
                        points.append(point)
                    else:
                        points.append(point)
                        make_new_point = False    
                else:
                    print("Unable to add more points")
                    

                    

        # Set background color
        display.fill(BACKGROUND_COLOR)
        
        # Draw points
        for point in points:
            point.display()

        pygame.display.update()
        clock.tick(FRAMES)
        
  
def run():
    '''
    Uses the points chosen by the user to generate dots between them
    '''

    dots = []

    start = (WIDTH / 2, HEIGHT / 2)
    current_position = start
    
    while True:
        # Handle Events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        random_number = random.randint(0, (2 * len(points)) - 1 )
        
        for point in points:
            
            if random_number in point.choices:
                x = round((point.x + current_position[0]) / 2)
                y = round((point.y + current_position[1]) / 2)
                
                current_position = (x, y)
                dots.append(Dot(current_position, 5))
                break

        display.fill(BACKGROUND_COLOR)
        
        # Display the generated dots
        for dot in dots:
            dot.display()
        
        # Display the labeled points
        for point in points:
            point.display()

        pygame.display.update()
        clock.tick(FRAMES)
    

if __name__ == "__main__":

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    light_pink = (255, 211, 243)
    
    # Points displayed on the screen
    points = []

    # Constants
    WIDTH = 1000
    HEIGHT = 600
    FRAMES = 25
    BACKGROUND_COLOR = light_pink

    # Pygame init
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
    pygame.display.set_caption("Chaos Game")
    clock = pygame.time.Clock()
    
    # Display inststructions
    print("Game Chaos")
    print("Instructions:")
    print("\t1. Click on screen to place points")
    print("\t2. When done, press 's' on your keyboard to begin the game")
    
    # Start simulator
    set_points()
    run()
