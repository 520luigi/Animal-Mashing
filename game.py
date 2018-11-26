# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/15 19:34:08 by szheng            #+#    #+#              #
#    Updated: 2018/11/24 17:45:41 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
import random

pygame.init()

#Declare some rgb color variables for ease of use.
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#display width and height made to the background image resolution
display_width = 736
display_height = 600

#set finish line to be fraction of window height and increments per key pressed
finish_line = display_height/13
increment = 10

#Specific calling of pygame window to set width and height
win = pygame.display.set_mode((display_width, display_height))

#Display the caption on top of pygame window top banner
pygame.display.set_caption("Button Smashers!")

#Set positions of background image, startup menu to the top left corner
img_pos = [0, 0]

#Load and set up background image and startup menu
bg_image = pygame.image.load("graphics/bgimage.png").convert()
startup_image = pygame.image.load("graphics/startmenu.png").convert()

#initialize sounds for player clicks, winner, players, intro countdown, etc
bg_music = pygame.mixer.Sound("sounds/FrozenJam.ogg")
bg_music.set_volume(0.4)
p1_click = pygame.mixer.Sound("sounds/jingle1.ogg")
p1_click.set_volume(0.4)
p2_click = pygame.mixer.Sound("sounds/jingle2.ogg")
p2_click.set_volume(0.4)
winner_sound = pygame.mixer.Sound("sounds/winner.ogg")
p1_sound = pygame.mixer.Sound("sounds/player_1.ogg")
p2_sound = pygame.mixer.Sound("sounds/player_2.ogg")
one = pygame.mixer.Sound("sounds/1.ogg")
two = pygame.mixer.Sound("sounds/2.ogg")
three = pygame.mixer.Sound("sounds/3.ogg")
begin = pygame.mixer.Sound("sounds/begin.ogg")

def change_animal():
    #Create a string array of animals to choose from randomly per game reset
    animals = ["graphics/chick.png", "graphics/horse.png", "graphics/pig.png",
        "graphics/elephant.png", "graphics/parrot.png", "graphics/duck.png",
        "graphics/hippo.png", "graphics/penguin.png", "graphics/whale.png"]

    player1_animal = random.choice(animals)
    player2_animal = random.choice(animals)
    #prevent players from having the same animal
    while player1_animal == player2_animal:
         player2_animal = random.choice(animals)

    # Load and set up players animal.
    player1_image = pygame.image.load(player1_animal).convert()
    player1_image.set_colorkey(black)
    player2_image = pygame.image.load(player2_animal).convert()
    player2_image.set_colorkey(black)
    return (player1_image, player2_image)

def set_position(): #add input of value 2-4, if statements to set up players...
    #players locations stored in arrays
    x = [display_width/3, display_width * 0.61]
    y = [display_height * 2/3 - 20, display_height * 2/3 - 20]
    return (x[0], y[0], x[1], y[1])

def draw_text(window, text, size, x, y):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, red)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    window.blit(text_surface, text_rect)

def show_victory_screen(message, sound_number):
    #screen, title, size, x, y
    #win.fill(white) #change to a cooler background maybe...or dont even use this...
    draw_text(win, "WINNER!", 88, display_width/2, display_height/4)
    draw_text(win, message, 80, display_width/2,
        display_height/2)
    draw_text(win, "<ESCAPE> Return to Main Menu", 18,
        display_width/2, display_height * 3/4)
    pygame.display.flip()
    winner_sound.play()
    pygame.time.delay(1200)
    if sound_number == 1:
        p1_sound.play()
    elif sound_number == 2:
        p2_sound.play()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_intro(win, display_width, display_height)

def game_intro(win, width, height):

    intro = True
    #use this to put the start menu onto the window
    win.blit(startup_image, img_pos)
    #play background music and loop it
    bg_music.play(loops=-1)
    while intro:
        for event in pygame.event.get():
            #print (event) #this prints the event to the terminal for checking
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    bg_music.stop()
                    three.play()
                    pygame.time.delay(1000)
                    two.play()
                    pygame.time.delay(1000)
                    one.play()
                    pygame.time.delay(1000)
                    begin.play()
                    pygame.time.delay(1000)
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        pygame.display.update()

def game_loop():
    #use this to put the background image to the window and clear start menu
    win.blit(bg_image, img_pos)
    #deletes all the keypresses before game start bug
    pygame.event.get()
    #change animal for players every game loop and reset position
    p1_img, p2_img = change_animal()
    x1, y1, x2, y2 = set_position()

    pygame.display.update()
    #add intro sounds before the game begins...


    running = True
    game_over = False
    while running:

        #put the animal pictures onto the screen many times after increments!!
        win.blit(p1_img, (x1, y1))
        win.blit(p2_img, (x2, y2))
        pygame.display.update()

        if game_over:
            if difference < 0:
                message = "Player 1"
                playersound = 1
            elif difference > 0:
                message = "Player 2"
                playersound = 2
            show_victory_screen(message, playersound)
            game_over = False
            p1_img, p2_img = change_animal()
            x1, y1, x2, y2 = set_position()
            win.blit(bg_image, img_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and y1 > finish_line:
                    y1 -= increment
                    p1_click.play()
                elif event.key == pygame.K_RSHIFT and y2 > finish_line:
                    y2 -= increment
                    p2_click.play()
                if y1 < finish_line or y2 < finish_line:
                    difference = y1 - y2
                    game_over = True
                    break
game_intro(win, display_width, display_height)
#game_loop(win, bg_img, img_pos, p1_click, p2_click, winner_sound, p1_sound, p2_sound)
