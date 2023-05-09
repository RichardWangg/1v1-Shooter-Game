import pygame
from game_specifications import *
from player_class import *

pygame.init()

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
    if player.alive:
        player_1.move(movePlayer1_right, movePlayer1_left)
        player_2.move(movePlayer2_right, movePlayer2_left)
        if movePlayer1_right or movePlayer1_left:
            player_1.update_action(1) #index 1 of 2d list is the running animation
        else:
            player_1.update_action(0) #index 0 is idle animation
        if movePlayer2_right or movePlayer2_left:
            player_2.update_action(1)
        else:
            player_2.update_action(0)

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
            if event.key == pygame.K_w and player.alive:
                player_1.jump = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movePlayer1_left = False
            if event.key == pygame.K_d:
                movePlayer1_right = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                movePlayer2_left = True
            if event.key == pygame.K_l:
                movePlayer2_right = True
            if event.key == pygame.K_i and player.alive:
                player_2.jump = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_j:
                movePlayer2_left = False
            if event.key == pygame.K_l:
                movePlayer2_right = False

        #menu dropdown by clicking esc
    pygame.display.update()


pygame.quit()