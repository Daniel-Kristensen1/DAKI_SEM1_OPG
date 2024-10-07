import pygame

#Creates an arrow or clock hand. It is shaped like a triangle with a circle portraied on the top part of the arrow.
def custom_arrow(width, height, color):
    arrow_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    triangle_points = [(width/2, height), # Top point
                       (width*0.60, 0+(height/2)+6), # Right point
                       (width*0.30, 0+height/2+6) ] # Left point
    circle_centerpoint = ((width/2,height*0.8))
    pygame.draw.polygon(arrow_surface, color, triangle_points)
    pygame.draw.circle(arrow_surface, color, circle_centerpoint,width*0.25)
    return arrow_surface