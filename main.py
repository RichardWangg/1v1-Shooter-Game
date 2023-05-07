import pygame

pygame.init()

# Game Window Specifications

screen_width = 1000 
screen_height = int(screen_width*0.6)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('1v1 Shooter')

#CONTROLS
movePlayer1_right = False
movePlayer1_left = False
movePlayer2_right = False
movePlayer2_left = False

#FRAMERATE
clock = pygame.time.Clock()
FPS = 120
bg = (144, 201, 120)
def fill_bg(): #fills screen so no trail left behind
    screen.fill(bg)

#PLAYERS
#inheritance class from pygame.sprite.Sprite built in sprite class for the players icons
class player(pygame.sprite.Sprite):
    def __init__(self, player_type, xstart, ystart, scale, speed):
        pygame.sprite.Sprite.__init__(self)  #initializing self from the parent Sprite class 
        self.speed = speed
        self.player_type = player_type
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.action = 0
        temp_list = []
        for i in range(0,4):
            img = pygame.image.load(f'imgs/{self.player_type}/idle/{i}.png')
            img = pygame.transform.scale(img,(int(img.get_width()*scale), int(img.get_height()*scale))) #scaling
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(0,8):
            img = pygame.image.load(f'imgs/{self.player_type}/sprint/{i}.png')
            img = pygame.transform.scale(img,(int(img.get_width()*scale), int(img.get_height()*scale))) #scaling
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (xstart,ystart)

    def disp(self): #To display the player on screen
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rectangle)

    def update_animation(self):
        animation_cooldown = 200
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
    
    def update_action(self, new_action):
        #check if new action is different
        if new_action != self.action:
            self.action = new_action
            #update the animation
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def move(self, move_right, move_left):
        dx = 0
        dy = 0 

        if move_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        if move_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        self.rectangle.x += dx
        self.rectangle.y += dy
        
#Instances of the Player Class
player_1 = player('player_1', 100, 50, 2.5, 5) 
player_2 = player('player_2', 900, 50, 2.5, 5) 

#While loop to run the game window
run_game = True
while run_game:

    #METHODS

    #Framerate 
    clock.tick(FPS)
    fill_bg()

    #displaying player
    player_1.disp()
    player_2.disp()
    player_1.update_animation()
    player_2.update_animation()

    #update player action
    if movePlayer1_right or movePlayer1_left:
        player_1.update_action(1) #index 1 of 2d list is the running animation
    else:
        player_1.update_action(0) #index 0 is idle animation
    if movePlayer2_right or movePlayer2_left:
        player_2.update_action(1)
    else:
        player_2.update_action(0)

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