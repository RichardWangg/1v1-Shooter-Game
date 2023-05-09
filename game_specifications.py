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
red = (255, 0, 0)
def fill_bg(): #fills screen so no trail left behind
    screen.fill(bg)
    pygame.draw.line(screen, red, (0, screen_height - 100), (screen_width, screen_height - 100))
    pygame.draw.line(screen, red, (0, 0), (screen_width, 0))

#GAME VARIABLES
GRAVITY = 0.4

#PLAYERS
#inheritance class from pygame.sprite.Sprite built in sprite class for the players icons
class player(pygame.sprite.Sprite):
    def __init__(self, player_type, xstart, ystart, scale, speed):
        pygame.sprite.Sprite.__init__(self)  #initializing self from the parent Sprite class 
        self.alive = True
        self.speed = speed
        self.player_type = player_type
        self.jump = False
        self.vel_y = 0
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
        if self.jump == True:
            self.vel_y = -11 #in pygame negative represents positive y-direction
            self.jump = False
        #Gravity
        self.vel_y += GRAVITY
        dy += self.vel_y
        #Ground
        if self.rectangle.bottom + dy > screen_height - 100:
            dy = (screen_height - 100) - self.rectangle.bottom
        #Roof
        if self.rectangle.top + dy < 0:
            dy = 0 - self.rectangle.top
        #Side Boundaries

        self.rectangle.x += dx
        self.rectangle.y += dy

pygame.quit()