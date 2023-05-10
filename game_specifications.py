import pygame

# Game Window Specifications
screen_width = 1000 
screen_height = int(screen_width*0.6)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('1v1 Shooter')

#CONTROLS VARIABLES
movePlayer1_right = False
movePlayer1_left = False

movePlayer2_right = False
movePlayer2_left = False

shoot_player1 = False
shoot_player2 = False
#FRAMERATE
clock = pygame.time.Clock()
FPS = 120
bg = (144, 201, 120)
red = (255, 0, 0)
def fill_bg(): #fills screen so no trail left behind
    screen.fill(bg)
    pygame.draw.line(screen, red, (0, screen_height - 100), (screen_width, screen_height - 100))
    pygame.draw.line(screen, red, (0, 0), (screen_width, 0))
    pygame.draw.line(screen, red, (0,screen_height), (0,0))
    pygame.draw.line(screen, red, (screen_width, screen_height), (screen_width, 0))

#GAME VARIABLES
GRAVITY = 0.4