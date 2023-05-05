import pygame

pygame.init()

# Game Window Specifications

screen_width = 1000 
screen_height = int(screen_width*0.6)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('2v2 Shooter')

#CONTROLS
movePlayer1_right = False
movePlayer1_left = False
movePlayer2_right = False
movePlayer2_left = False

#PLAYERS
#inheritance class from pygame.sprite.Sprite built in sprite class for the players icons
class player(pygame.sprite.Sprite):
    def __init__(self, img, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)  #initializing self from the parent Sprite class 
        self.img = img #pygame.image.load('')
        self.x = x
        self.y = y
        self.scale = scale
        self.speed = speed
        self.image = pygame.transform.scale(img,(int(img.get_width()*scale), int(img.get_height()*scale))) #scaled image
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (x,y)

    def disp(self): #To display the player on screen
        screen.blit(self.image, self.rectangle)

    def move(self, move_right, move_left):
        dx = 0
        dy = 0 

        if move_right:
            dx = self.speed
        if move_left:
            dx = -self.speed

        self.rectangle.x = dx
        self.rectangle.y = dy
        
#Instances of the Player Class
player_1 = player(pygame.image.load('imgs/player/idle_player1.png'), 100, 50, 0.1, 5) 
player_2 = player(pygame.image.load('imgs/player/idle_player1.png'), 900, 50, 0.1, 5) 

#While loop to run the game window
run_game = True
while run_game:

    #METHODS

    #displaying player
    player_1.disp()
    player_2.disp()

    #moving player
    player_1.move(movePlayer1_right, movePlayer1_left)
    player_2.move(movePlayer2_right, movePlayer2_left)

    for event in pygame.event.get():
        #QUIT GAME
        if event.type == pygame.QUIT: #quit game
            run_game = False
        #LOOKING FOR KEYPRESSES/RELEASES
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movePlayer1_left = True
            if event.key == pygame.K_d:
                movePlayer1_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movePlayer1_left = False
            if event.key == pygame.K_d:
                movePlayer1_right = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movePlayer2_left = True
            if event.key == pygame.K_RIGHT:
                movePlayer2_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                movePlayer2_left = False
            if event.key == pygame.K_RIGHT:
                movePlayer2_right = False

        #menu dropdown by clicking esc
    pygame.display.update()


pygame.quit()