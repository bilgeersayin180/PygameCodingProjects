import pygame
import random as teleport
pygame.init()
window_x = 1566
window_y = 632
x_max = 1443
x_min = 3
location_left = False
window = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("Horror Game")
#background_RGB = (50, 50, 50)
#character's scale: (120, 150)
speed = 30
x = window_x/2
y = 400
slender_x = teleport.uniform(200,(window_x - 200))
slender_y = teleport.uniform(150,(window_y - 325))
width = 50
height = 50
clock = pygame.time.Clock()
white = (255,255,255)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
isLeft = False
isRight = False
clock = pygame.time.Clock()
walkCount = 0
slenderman_light = pygame.image.load('slenderman_light.png')
slender_man_light = pygame.transform.scale(slenderman_light, (120,150))
slenderman_dark = pygame.image.load('slenderman_dark.png')
slender_man_dark = pygame.transform.scale(slenderman_dark, (120,150))
right = pygame.image.load('char_sag.png')
R = pygame.transform.scale(right, (120,150))
right_reverse = pygame.image.load('char_sag_reverse.png')
r = pygame.transform.scale(right_reverse, (120,150))
left = pygame.image.load('char_sol.png')
left_reverse = pygame.image.load('char_sol_reverse.png')
L = pygame.transform.scale(left, (120,150))
l = pygame.transform.scale(left_reverse, (120,150))
turn_right = [R,R,R,R,R,R,R,R,R]
turn_left =  [L,L,L,L,L,L,L,L,L]
turn_right_reverse = [r,r,r,r,r,r,r,r,r]
turn_left_reverse =  [l,l,l,l,l,l,l,l,l]
night_vision = pygame.image.load('night_vision.png')
background = pygame.image.load('Giriş.png') #.convert()
Left_place = pygame.image.load('left_place.png')
Left_place_inverse = pygame.image.load('left_place - Kopya_inverse.png')
main = pygame.image.load('char_orta.png')
main_reverse = pygame.image.load('char_orta_reverse.png')
font = pygame.font.SysFont(None, 25)
run = True
def displayWindow():
    global walkCount
    window.blit(background, [0,0])
    window.blit(slender_man_light, (slender_x,slender_y))
    #window.blit(slender_man_light, (teleport.uniform(200,(window_x - 200)),teleport.uniform(150,(window_y - 325))))
    if walkCount + 1 >= 27:
        walkCount = 0
    if isLeft:
        window.blit(turn_left[walkCount//3], (x,y))
        walkCount = walkCount + 1
    elif isRight:
        window.blit(turn_right[walkCount//3], (x,y))
        walkCount = walkCount + 1
    else:
        Main = pygame.transform.scale(main, (120,150))
        window.blit(Main, (x,y))
    pygame.display.update()
def displayWindowNightVision():
    global walkCount
    window.blit(night_vision, [0,0])
    window.blit(slender_man_dark, (slender_x, slender_y))
    #window.blit(slender_man_light, (teleport.uniform(200,(window_x - 200)),teleport.uniform(150,(window_y - 325))))
    if walkCount + 1 >= 27:
        walkCount = 0
    if isLeft:
        window.blit(turn_left_reverse[walkCount//3], (x,y))
        walkCount = walkCount + 1
    elif isRight:
        window.blit(turn_right_reverse[walkCount//3], (x,y))
        walkCount = walkCount + 1
    else:
        Main_Reverse = pygame.transform.scale(main_reverse, (120,150))
        window.blit(Main_Reverse, (x,y))
    pygame.display.update()
def left_placeWindow():
    global walkCount
    window.blit(Left_place, [0,0])
    window.blit(slender_man_light, (slender_x,slender_y))
    #window.blit(slender_man_light, (teleport.uniform(200,(window_x - 200)),teleport.uniform(150,(window_y - 325))))
    if walkCount + 1 >= 27:
        walkCount = 0
    if isLeft:
        window.blit(turn_left[walkCount//3], (x,y))
        walkCount = walkCount + 1
    elif isRight:
        window.blit(turn_right[walkCount//3], (x,y))
        walkCount = walkCount + 1
    else:
        Main = pygame.transform.scale(main, (120,150))
        window.blit(Main, (x,y))
    pygame.display.update()
def left_placeWindow_inverse():
    global walkCount
    window.blit(Left_place_inverse, [0,0])
    window.blit(slender_man_light, (slender_x,slender_y))
    #window.blit(slender_man_light, (teleport.uniform(200,(window_x - 200)),teleport.uniform(150,(window_y - 325))))
    if walkCount + 1 >= 27:
        walkCount = 0
    if isLeft:
        window.blit(turn_left[walkCount//3], (x,y))
        walkCount = walkCount + 1
    elif isRight:
        window.blit(turn_right[walkCount//3], (x,y))
        walkCount = walkCount + 1
    else:
        Main = pygame.transform.scale(main, (120,150))
        window.blit(Main, (x,y))
    pygame.display.update()
    
def blitme(self):
    self.window.blit(self.image, self.rect)
def write(msg,color):
    screen_text = font.render(msg,True,color)
    window.blit(screen_text, [20,20])
while (run):
    clock.tick(27)
    pygame.time.delay(60)
    for user_events in pygame.event.get():
        if user_events.type == pygame.QUIT:
            run = False    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > speed:  #left
        x = x - speed
        isLeft = True
        isRight = False
        if keys[pygame.K_w] and y > 10: #up
            y = y - speed
        elif keys[pygame.K_s] and y < (530 - height - speed): #down
            y = y + speed
    elif keys[pygame.K_d] and x < (1500 - width - speed): #right
        x = x + speed
        isRight = True
        isLeft = False
        if keys[pygame.K_w] and y > 10: #up
            y = y - speed
        elif keys[pygame.K_s] and y < (530 - height - speed): #down
            y = y + speed
        
    elif keys[pygame.K_w] and y > 10: #up
        y = y - speed
    elif keys[pygame.K_s] and y < (530 - height - speed): #down
        y = y + speed
    else:
        isRight = False
        isLeft = False
        walkCount = 0
    """
    if (not isNightVision):
        displayWindow()
    """
    if (x != x_min):
        displayWindow()
        if keys[pygame.K_f]:
            slender_x = teleport.uniform(200,(window_x - 200))
            slender_y = teleport.uniform(150,(window_y - 325))
            displayWindowNightVision()
            pygame.display.update()
    if(x == x_min):
        location_left = True
        left_placeWindow()
        if keys[pygame.K_f]:
            slender_x = teleport.uniform(200,(window_x - 200))
            slender_y = teleport.uniform(250,(window_y - 100))
            left_placeWindow_inverse()
            pygame.display.update()
    pygame.display.update()
    """
    window.blit(background, [0,0])
    main_character = pygame.transform.scale(main, (120,150))
    window.blit(main_character, (x, y))
    pygame.display.update()
    """
pygame.quit()

    
