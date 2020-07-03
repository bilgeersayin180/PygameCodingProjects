import pygame
import random
pygame.init()
window_x = 900
window_y = 800
green = (50,205,50)
black = (0, 0, 0)
white = (255,255,255)
deep_blue = (0, 0, 89)
line1_start_pos = (300,50)
line1_end_pos = (100,600)
line2_start_pos = (500,50)
line2_end_pos = (700,600)
moving_x = 160
moving_y = 440
moving_x2 = 600
moving_y2 = 325 
circle1_pos_start = (line1_start_pos)
circle1_pos_end = (line1_end_pos)
circle2_pos_start = (line2_start_pos)
circle2_pos_end = (line2_end_pos)
window = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("Pappus Theory")
program = True
while (program):
    for userEvents in pygame.event.get():
        if userEvents.type == pygame.QUIT:
            program = False
    key = pygame.key.get_pressed()
    if ((key[pygame.K_s]) and (moving_x >= 100)):
        moving_x = moving_x - 4
        moving_y = moving_y + 11
    if ((key[pygame.K_w]) and (moving_x <= 300)):
        moving_x = moving_x + 4
        moving_y = moving_y - 11
    if ((key[pygame.K_DOWN]) and (moving_x2 <= 700)):
        moving_x2 = moving_x2 + 4
        moving_y2 = moving_y2 + 11
    if ((key[pygame.K_UP]) and (moving_x2 >= 500)):
        moving_x2 = moving_x2 - 4
        moving_y2 = moving_y2 - 11
    window.fill(white)
    pygame.draw.line(window, green, line1_start_pos, line1_end_pos, 2)
    pygame.draw.line(window, green, line2_start_pos, line2_end_pos, 2)
    
    pygame.draw.circle(window, deep_blue, circle1_pos_start, 15)
    pygame.draw.circle(window, deep_blue, circle1_pos_end, 15)
    pygame.draw.circle(window, deep_blue, (moving_x,moving_y), 15)
    moving_circle_pos =  (moving_x,moving_y)
    pygame.draw.circle(window, deep_blue, (moving_x2,moving_y2), 15)
    moving_circle_pos2 = (moving_x2,moving_y2) 
    pygame.draw.circle(window, deep_blue, circle2_pos_start, 15)
    pygame.draw.circle(window, deep_blue, circle2_pos_end, 15)
    
    pygame.draw.line(window, black, (400,50), (400,600), 2)
    pygame.draw.line(window, deep_blue, circle1_pos_start, circle2_pos_start, 2)
    pygame.draw.line(window, deep_blue, circle1_pos_start, moving_circle_pos2, 2)
    pygame.draw.line(window, deep_blue, circle1_pos_start, circle2_pos_end, 2)
    pygame.draw.line(window, deep_blue, circle1_pos_end, circle2_pos_start, 2)
    pygame.draw.line(window, deep_blue, circle1_pos_end, circle2_pos_end, 2)
    pygame.draw.line(window, deep_blue, circle1_pos_end, moving_circle_pos2, 2)
    pygame.draw.line(window, deep_blue, moving_circle_pos, moving_circle_pos2, 2)
    pygame.draw.line(window, deep_blue, circle2_pos_start, moving_circle_pos, 2)
    pygame.draw.line(window, deep_blue, moving_circle_pos, circle2_pos_end, 2)

    pygame.display.update()
pygame.quit()
