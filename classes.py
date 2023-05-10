import pygame
import os
import random
from game_specifications import *
from game_specifications import screen_width

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
        self.shoot_cooldown = 0
        self.health = 5
        animation_types = ['idle', 'sprint', 'hit', 'death']
        #inserting all animation types into 2d array animation_list
        for animation in animation_types:
            temp_list = []
            #count the number of files in folder
            num_of_frames = len(os.listdir(f'imgs/{self.player_type}/{animation}')) 
            for i in range(0, num_of_frames):
                img = pygame.image.load(f'imgs/{self.player_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img,(int(img.get_width()*scale), int(img.get_height()*scale))) #scaling
                temp_list.append(img)
            self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (xstart, ystart)

    def disp(self): #To display the player on screen
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def update_animation(self):
        animation_cooldown = 200
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                if self.action == 3:
                    self.frame_index = len(self.animation_list[self.action]) - 1
                else:
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
        if self.rect.bottom + dy > screen_height - 100:
            dy = (screen_height - 100) - self.rect.bottom
        #Roof
        if self.rect.top + dy < 0:
            dy = 0 - self.rect.top
        #Side Boundaries
        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        self.rect.x += dx
        self.rect.y += dy
    
    def shoot(self):
        if self.shoot_cooldown == 0:    
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (self.rect.size[0]*self.direction), self.rect.centery, self.direction)
            bullet_group.add(bullet)
    
    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3)
    
    def update(self):
        self.check_alive()
        self.update_animation()
        #update shot cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

#Instances of the Player Class
player_1 = player('player_1', 100, 50, 2.5, 5) 
player_2 = player('player_2', 900, 50, 2.5, 5)
#----------------------------------------------------------------------------------------------------------------------------------------------------
bullet_img = pygame.image.load('imgs/bullet/0.png').convert_alpha()
bullet_img = pygame.transform.scale(bullet_img,(int(bullet_img.get_width()*0.035), int(bullet_img.get_height()*0.035))) #scaling
shoot_cooldown = 200
shoot_time= pygame.time.get_ticks()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, xstart, ystart, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 20
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (xstart, ystart)
        self.direction = direction

    #overidding update method
    def update(self):
        #move bullet
        self.rect.x += (self.direction*self.speed)
        if self.rect.x < 0 or self.rect.left > screen_width:
            self.kill()
        #check collisions with others
        if pygame.sprite.spritecollide(player_1, bullet_group, False):
            if player_1.alive:
                self.kill()
                player_1.health -= 1
                player_1.update_action(2)
        if pygame.sprite.spritecollide(player_2, bullet_group, False):
            if player_2.alive:
                self.kill()
                player_2.health -= 1
                player_2.update_action(2)
#sprite group
bullet_group = pygame.sprite.Group()
#---------------------------------------------------------------------------------------------------------------------------------------------
Bandage_img = pygame.image.load('bandage/0.png').convert_alpha()
Bandage_img = pygame.transform.scale(Bandage_img,(int(Bandage_img.get_width()*0.07), int(Bandage_img.get_height()*0.07))) #scaling
class Bandage(pygame.sprite.Sprite):
    def __init__(self, xstart, ystart):
        pygame.sprite.Sprite.__init__(self)
        self.image = Bandage_img
        self.rect = self.image.get_rect()
        self.rect.center = (xstart, ystart)
        self.bandage_clock = pygame.time.get_ticks()

    def update(self):
        if pygame.sprite.spritecollide(player_1, Bandage_group, False):
            self.kill()
            if player_1.health != 5 and player_1.alive:
                player_1.health += 1
        if pygame.sprite.spritecollide(player_2, Bandage_group, False):
            self.kill()
            if player_2.health != 5 and player_2.alive:
                player_2.health += 1
        if pygame.time.get_ticks() - self.bandage_clock > 10000:
            self.kill()
    
    def spawn_bandage(self):
        if pygame.time.get_ticks() - self.bandage_clock > 5000:
            self.bandage_clock = pygame.time.get_ticks()
            bandage = Bandage(random.uniform(0,screen_width), random.uniform(0,screen_height - 100))
            Bandage_group.add(bandage)

Bandage_group = pygame.sprite.Group()
Bandage_start = Bandage(screen_width/2, screen_height/2)