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
    player_1.action_update()
    player_2.disp()
    player_2.update()
    player_2.action_update()

    #Game over condition
    if not player_1.alive or  not player_2.alive:
        player_1.reset()
        player_2.reset()

    for event in pygame.event.get():
        #QUIT GAME
        if event.type == pygame.QUIT: #quit game
            run_game = False
        #LOOKING FOR KEYPRESSES/RELEASES
        if event.type == pygame.KEYDOWN:
            #player1
            if event.key == pygame.K_a:
                player_1.move_left = True
            if event.key == pygame.K_d:
                player_1.move_right = True
            if event.key == pygame.K_w:
                player_1.jump = True
            if event.key == pygame.K_LSHIFT:
                player_1.shoot_var = True
            #player2
            if event.key == pygame.K_j:
                player_2.move_left = True
            if event.key == pygame.K_l:
                player_2.move_right = True
            if event.key == pygame.K_i:
                player_2.jump = True
            if event.key == pygame.K_SPACE:
                player_2.shoot_var = True

        if event.type == pygame.KEYUP:
            #player1
            if event.key == pygame.K_a:
                player_1.move_left = False
            if event.key == pygame.K_d:
                player_1.move_right = False
            if event.key == pygame.K_LSHIFT:
                player_1.shoot_var = False
            #player2
            if event.key == pygame.K_j:
                player_2.move_left = False
            if event.key == pygame.K_l:
                player_2.move_right = False
            if event.key == pygame.K_SPACE:
                player_2.shoot_var = False 

        #menu dropdown by clicking esc
    pygame.display.update()

pygame.quit()
