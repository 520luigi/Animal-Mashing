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
import sys
import os

def resource_path(path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    return os.path.join(os.path.abspath("."), path)
pygame.init()

#Declare some rgb color variables for ease of use.
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#Display width and height made to the background image resolution
display_width = 736
display_height = 600

#Set finish line to be fraction of window height and increments per key pressed
finish_line = display_height/13
increment = 10

#Specific calling of pygame window to set width and height
win = pygame.display.set_mode((display_width, display_height))

#Display the caption on top of pygame window top banner
pygame.display.set_caption("Animal Mashing")

#Set positions of background image, startup menu to the top left corner
img_pos = [0, 0]

#Load and set up background image and startup menu
bg_image = pygame.image.load(resource_path("graphics/bgimage.png")).convert()
startup_image = pygame.image.load(resource_path("graphics/startmenu.png")).convert()
p1_wins = pygame.image.load(resource_path("graphics/p1win.png")).convert_alpha()
p2_wins = pygame.image.load(resource_path("graphics/p2win.png")).convert_alpha()

#Initialize sounds for player clicks, winner, players, intro countdown, etc
bg_music = pygame.mixer.Sound(resource_path("sounds/FrozenJam.ogg"))
bg_music.set_volume(0.4)
p1_click = pygame.mixer.Sound(resource_path("sounds/jingle1.ogg"))
p1_click.set_volume(0.4)
p2_click = pygame.mixer.Sound(resource_path("sounds/jingle2.ogg"))
p2_click.set_volume(0.4)
winner_sound = pygame.mixer.Sound(resource_path("sounds/flawless_victory.ogg"))
p1_sound = pygame.mixer.Sound(resource_path("sounds/player_1.ogg"))
p2_sound = pygame.mixer.Sound(resource_path("sounds/player_2.ogg"))
prepare_yourself = pygame.mixer.Sound(resource_path("sounds/prepare_yourself.ogg"))
one = pygame.mixer.Sound(resource_path("sounds/1.ogg"))
two = pygame.mixer.Sound(resource_path("sounds/2.ogg"))
three = pygame.mixer.Sound(resource_path("sounds/3.ogg"))
begin = pygame.mixer.Sound(resource_path("sounds/begin.ogg"))

def change_animal():
    #Create a string array of animals to choose from randomly per game reset
    animals = [resource_path("graphics/chick.png"), resource_path("graphics/horse.png"), resource_path("graphics/pig.png"),
        resource_path("graphics/elephant.png"), resource_path("graphics/parrot.png"), resource_path("graphics/duck.png"),
        resource_path("graphics/hippo.png"), resource_path("graphics/penguin.png"), resource_path("graphics/whale.png")]

    player1_animal = random.choice(animals)
    player2_animal = random.choice(animals)
    #Prevent players from having the same animal
    while player1_animal == player2_animal:
         player2_animal = random.choice(animals)
    #Load and set up players animal
    player1_image = pygame.image.load(player1_animal).convert()
    player1_image.set_colorkey(black)
    player2_image = pygame.image.load(player2_animal).convert()
    player2_image.set_colorkey(black)
    return (player1_image, player2_image)

def set_position():
    #Players location stored in arrays
    x = [display_width/3, display_width * 0.61]
    y = [display_height * 2/3 - 20, display_height * 2/3 - 20]
    return (x[0], y[0], x[1], y[1])

def show_victory_screen(message, sound_number):
    #Show victory screen and play the sounds according to who won
    winner_sound.play()
    pygame.time.delay(2000)
    if sound_number == 1:
        win.blit(p1_wins, img_pos)
        p1_sound.play()
    elif sound_number == 2:
        win.blit(p2_wins, img_pos)
        p2_sound.play()
    pygame.display.flip()
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
    #Game intro which loops with music and goes into game countdown
    intro = True
    win.blit(startup_image, img_pos)
    bg_music.play(loops=-1)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    bg_music.stop()
                    prepare_yourself.play()
                    pygame.time.delay(1888)
                    three.play()
                    pygame.time.delay(788)
                    two.play()
                    pygame.time.delay(788)
                    one.play()
                    pygame.time.delay(788)
                    begin.play()
                    pygame.time.delay(788)
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        pygame.display.update()

def game_loop():
    #Use this to put the background image to the window and clear start menu
    win.blit(bg_image, img_pos)
    #Deletes all the keypresses before game start bug
    pygame.event.get()
    #Change animal for players every game loop and reset position
    p1_img, p2_img = change_animal()
    x1, y1, x2, y2 = set_position()

    pygame.display.update()

    running = True
    game_over = False
    while running:
        #Put the animal pictures onto the screen many times after increments!!
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
