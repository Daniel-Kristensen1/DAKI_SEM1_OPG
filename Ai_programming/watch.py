import pygame
import math
import time


pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

#Center point
x_c = 640/2
y_c = 480/2
centerPoint = (x_c,y_c)

#Varibles
radius=150
angle_degree = 90
elipse_width = 80
elipse_height = 100
# TO DO: 
# color variables
color_primary = "#BF107B"
color_secondary = "#E936A4"
color_tertiary = "#FFCFB7"
color_black = "#25201E"
color_white = "#FFFFFF"

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


#####################################################################################################################################################

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    
    #Clear screen
    screen.fill(color_white)

    #Rebuild Clock

#####################################################################################################################################################
    #Build pelats for the outside of the clock
    for i in range(9):
        angle_radians = math.radians(angle_degree+20)
        angle_degree_elipse=angle_degree-90+20
        ellipse_surface=pygame.Surface((elipse_width,elipse_height), pygame.SRCALPHA)
        ellipse_surface.fill((0,0,0,0))
        pygame.draw.ellipse(ellipse_surface, color_primary, ellipse_surface.get_rect())
        rotated_ellipse = pygame.transform.rotate(ellipse_surface, -angle_degree_elipse)
        rotated_rect = rotated_ellipse.get_rect(center=(x_c - math.cos(angle_radians)*(radius), y_c - math.sin(angle_radians)*(radius)))
        screen.blit(rotated_ellipse,rotated_rect)
        angle_degree += 40

    for i in range(9):
        angle_radians = math.radians(angle_degree)
        angle_degree_elipse=angle_degree-90
        ellipse_surface=pygame.Surface((elipse_width,elipse_height), pygame.SRCALPHA)
        ellipse_surface.fill((0,0,0,0))
        pygame.draw.ellipse(ellipse_surface, color_secondary, ellipse_surface.get_rect())
        rotated_ellipse = pygame.transform.rotate(ellipse_surface, -angle_degree_elipse)
        rotated_rect = rotated_ellipse.get_rect(center=(x_c - math.cos(angle_radians)*(radius), y_c - math.sin(angle_radians)*(radius)))
        screen.blit(rotated_ellipse,rotated_rect)
        angle_degree += 40

#####################################################################################################################################################

    #Create outside border of clock:
    pygame.draw.circle(screen, color_tertiary, centerPoint,radius) #Base color of clock
    pygame.draw.circle(screen, color_white, centerPoint,radius, width=5) #Outer color of clock
    #Create centerpoint
    pygame.draw.circle(screen, color_black, centerPoint,radius=7, width=5)

    #Create 12 lines
    for i in range(60):
        angle_radians = math.radians(angle_degree)
        x_start = x_c - math.cos(angle_radians)*(radius-20)
        y_start = y_c - math.sin(angle_radians)*(radius-20)
        x_end = x_c - math.cos(angle_radians) * (radius-30)
        y_end = y_c - math.sin(angle_radians) * (radius-30)
        #pygame.draw.line(screen, "black" ,(x_start, y_start), (x_end, y_end))
        if i % 5 == 0:
            pygame.draw.line(screen, color_secondary ,(x_start, y_start), (x_end, y_end), width=4) #consider change to cylinder and not line
        else: 
            pygame.draw.line(screen, color_secondary ,(x_start, y_start), (x_end, y_end), width=2)

        angle_degree += 6

    angle_degree = 120 #Adjust the angel so it positions the numbers at the correct spot.
    font = pygame.font.Font(None, 36) # Creates a font
    #Draw numbers on clock
    for i in range(12):
        text=f"{i+1}"
        number_surface = font.render(text, True, color_primary)

        number_rect = number_surface.get_rect()

        #Calculate text position
        angle_radians = math.radians(angle_degree) #Is called to recalculate the radians after the degrees change
        x_num = x_c - math.cos(angle_radians)*(radius-50)
        y_num = y_c - math.sin(angle_radians)*(radius-50)
        #Adjust x_num and y_num so numbers are positioned correcly
        x_num -= number_rect.width / 2
        y_num -= number_rect.height / 2
    
        screen.blit(number_surface, (x_num, y_num))
    
        angle_degree += 30

#####################################################################################################################################################

    #Draw Clock arrows
    current_time = time.localtime()
    current_time_hour = current_time.tm_hour
    current_time_min = current_time.tm_min
    current_time_second = current_time.tm_sec
    #Calculate degree for each arrow
    angle_degree_arrow_one = 180 + (current_time_hour*30) + (current_time_min / 60 * 30)
    angle_degree_arrow_two = 180 + (current_time_min*6)
    angle_degree_arrow_three = 180 + (current_time_second*6)
    

    #Arrow one (hour)
    #print(f"hour: {current_time_hour}, degree: {angle_degree_arrow_one}")
    arrow_one_width = 20
    arrow_one_height = 125
    arrow_one_surface = custom_arrow(arrow_one_width, arrow_one_height, color_black)

    rotated_arrow_one_surface = pygame.transform.rotate(arrow_one_surface, -(angle_degree_arrow_one))
    rotated_arrow_one_rect = rotated_arrow_one_surface.get_rect(center=centerPoint)
    screen.blit(rotated_arrow_one_surface, rotated_arrow_one_rect)


    #Arrow two (min)
    arrow_two_width = 20
    arrow_two_height = 175
    arrow_two_surface = custom_arrow(arrow_two_width, arrow_two_height, color_black)

    rotated_arrow_two_surface = pygame.transform.rotate(arrow_two_surface, -(angle_degree_arrow_two))
    rotated_arrow_two_rect = rotated_arrow_two_surface.get_rect(center=centerPoint)
    screen.blit(rotated_arrow_two_surface, rotated_arrow_two_rect)


    #Arrow tree (seconds)    
    arrow_three_width = 5
    arrow_three_height = 175
    arrow_three_surface = custom_arrow(arrow_three_width, arrow_three_height, color_primary)

    rotated_arrow_three_surface = pygame.transform.rotate(arrow_three_surface, -(angle_degree_arrow_three))
    rotated_arrow_three_rect = rotated_arrow_three_surface.get_rect(center=centerPoint)
    screen.blit(rotated_arrow_three_surface, rotated_arrow_three_rect)
    #print(current_time_second)

#####################################################################################################################################################

    pygame.display.flip() # Refresh the screen so drawing appears



