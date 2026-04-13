import pygame

def draw_rectangle_colored(surface, rectangle, color_bool):
    if color_bool == True:
        color = (255, 255, 255)
    else: 
        color = (0, 128, 0)
    
    pygame.draw.rect(surface, color, rectangle)


def draw_board(surface, clock, height, width):
    rect_color = True # True for white and False for black

    rect_height = height/8
    rect_width = width/8

    rect_left = 0
    rect_top = 0
    while rect_top <= (720 - rect_height):
    
        while rect_left <= (1280 - rect_width):

            rectangle = pygame.Rect(rect_left, rect_top, rect_width, rect_height)
            draw_rectangle_colored(surface, rectangle, rect_color)

            rect_color = not rect_color

            rect_left = rect_left + rect_width
            
        rect_color = not rect_color

        rect_top = rect_top + rect_height
        rect_left = 0
     

