import pygame
from game_specifications import *
from classes import *
pygame.init()

#While loop to run the game window
run_game = True
while run_game:

    #Framerate 
    clock.tick(FPS)
    fill_bg()
    #show health bar
    draw_text('Player 1: ', pygame.font.SysFont('Futura', 20), white, 20, 30)
    for x in range(player_1.health):
        screen.blit(health_bar_icon, (85 + (x*15), 27))
    draw_text('Player 2: ', pygame.font.SysFont('Futura', 20), white, screen_width - 160, 30)
    for x in range(player_2.health):
        screen.blit(health_bar_icon, ((screen_width - 95) + (x*15), 27))

    #update and display groups
    bullet_group.update()
    bullet_group.draw(screen)
    Bandage_start.spawn_bandage()
    Bandage_group.update()
    Bandage_group.draw(screen)

    #displaying player
    player_1.disp()
    player_1.update()
    player_2.disp()
    player_2.update()
    
    #update player action player 1
    #shoot
    if player_1.alive:
        if shoot_player1:
            player_1.shoot()
            shoot_player1 = False
        # movement
        player_1.move(movePlayer1_right, movePlayer1_left)
        if movePlayer1_right or movePlayer1_left:
            player_1.update_action(1) #index 1 of 2d list is the running animation
        else:
            player_1.update_action(0) #index 0 is idle animation
        if player_1.action == 2:  # Check if player 1 is in hit animation
            player_1.update_animation()
    
    #update player action player 2
    #shoot
    if player_2.alive:
        if shoot_player2:
            player_2.shoot()
            shoot_player2 = False
        # movement
        player_2.move(movePlayer2_right, movePlayer2_left)
        if movePlayer2_right or movePlayer2_left:
            player_2.update_action(1) #index 1 of 2d list is the running animation
        else:
            player_2.update_action(0) #index 0 is idle animation

    for event in pygame.event.get():
        #QUIT GAME
        if event.type == pygame.QUIT: #quit game
            run_game = False
        #LOOKING FOR KEYPRESSES/RELEASES
        if event.type == pygame.KEYDOWN:
            #player1
            if event.key == pygame.K_a:
                movePlayer1_left = True
            if event.key == pygame.K_d:
                movePlayer1_right = True
            if event.key == pygame.K_w:
                player_1.jump = True
            if event.key == pygame.K_LSHIFT:
                shoot_player1 = True
            #player2
            if event.key == pygame.K_j:
                movePlayer2_left = True
            if event.key == pygame.K_l:
                movePlayer2_right = True
            if event.key == pygame.K_i:
                player_2.jump = True
            if event.key == pygame.K_SPACE:
                shoot_player2 = True

        if event.type == pygame.KEYUP:
            #player1
            if event.key == pygame.K_a:
                movePlayer1_left = False
            if event.key == pygame.K_d:
                movePlayer1_right = False
            if event.key == pygame.K_LSHIFT:
                shoot_player1 = False
            #player2
            if event.key == pygame.K_j:
                movePlayer2_left = False
            if event.key == pygame.K_l:
                movePlayer2_right = False
            if event.key == pygame.K_SPACE:
                shoot_player2 = False 

        #menu dropdown by clicking esc
    pygame.display.update()

pygame.quit()