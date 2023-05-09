import pygame
import os
from game_specifications import *

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
        animation_types = ['idle', 'sprint', 'hit', 'death']
        #inserting all animation types into 2d array animation_list
        for animation in animation_types:
            temp_list = []
            #count the number of files in folder
            num_of_frames = len(os.listdir(f'imgs/{self.player_type}/{animation}')) 
            for i in range(0, num_of_frames):
                img = pygame.image.load(f'imgs/{self.player_type}/{animation}/{i}.png')
                img = pygame.transform.scale(img,(int(img.get_width()*scale), int(img.get_height()*scale))) #scaling
                temp_list.append(img)
            self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (xstart, ystart)

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
        if self.rectangle.left + dx < 0:
            dx = 0 - self.rectangle.left
        if self.rectangle.right + dx > screen_width:
            dx = screen_width - self.rectangle.right

        self.rectangle.x += dx
        self.rectangle.y += dy