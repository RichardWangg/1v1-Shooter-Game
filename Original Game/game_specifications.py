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
white = (255, 255, 255)
def fill_bg(): #fills screen so no trail left behind
    screen.fill(bg)
    pygame.draw.line(screen, red, (0, screen_height - 100), (screen_width, screen_height - 100))
    pygame.draw.line(screen, red, (0, 0), (screen_width, 0))
    pygame.draw.line(screen, red, (0,screen_height), (0,0))
    pygame.draw.line(screen, red, (screen_width, screen_height), (screen_width, 0))

#health bar
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
health_bar_icon = pygame.image.load('health_bar_icon/0.png').convert_alpha()
health_bar_icon = pygame.transform.scale(health_bar_icon,(int(health_bar_icon.get_width()*0.01), int(health_bar_icon.get_height()*0.01))) #scaling

#GAME VARIABLES
GRAVITY = 0.4