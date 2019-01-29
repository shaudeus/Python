# Python game "Froggie" for python programming practice
# Written by Rashaun Forrest 8/2017
# With Zenva tutorial and assets


######### Programming Cheat Sheet ####################

# Python Data Structure list

# List = A List is a sequence of mutable Python objects
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# Dictionary = Objects paired together seperated by colon.
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Tuples = A tuple is a sequence of immutable Python objects
# tup1 = ('physics', 'chemistry', 1997, 2000);

# Function = A function is a block of organized, reusable code that is used to perform a single, related action.
#def functionname( parameters ):
#   "function_docstring"
#   function_suite
#   return [expression]


#######################################################################

import pygame #imports pygame library

##### Define function for Collision for treasure

def checkCollision(x, y, treasureX, treasureY):
    global screen, textWin
    collisionState = False
    if y >= treasureY and y <= treasureY + 40:
        if x >= treasureX and x <= treasureX + 35:
            y = 650
            collisionState = True

        elif x + 35 >= treasureX and x + 35 <= treasureX + 35:
            y = 650
            collisionState = True

    elif y + 40 >= treasureY and y + 40 <= treasureY + 40:
        if x >= treasureX and x <= treasureX + 35:
            y = 650
            collisionState = True

        elif x + 35 >= treasureX and x + 35 <= treasureX + 35:
            y = 650
            collisionState = True
    return collisionState, y

######### Scoring system   #################

def hi_score(count):
    global screen, font
    #font = pygame.font.SysFont("comicsans", 70)
    scoreText = font.render(str(collected) + "  Points", True, (YELLOW))
    screen.blit(scoreText,(50,50))
    #pygame.display.flip()

########## game set up #####################

pygame.init() #initializes pygame

pygame.mixer.init() # initialize music mixer function
pygame.mixer.music.load("music.mp3") # Loads mp3
pygame.mixer.music.play(-1) # infinite loops music

screen = pygame.display.set_mode((900, 700)) # Set Screen Size


######## Load graphics  ##############

playerImage = pygame.image.load("Player.png") #load graphic from folder assets
playerImage = pygame.transform.scale(playerImage, (35, 40)) # resize graphic
playerImage = playerImage.convert_alpha() # remove whitespace from graphic

backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage, (900, 700))
screen.blit(backgroundImage, (0, 0))

treasureImage = pygame.image.load("treasure.png")
treasureImage = pygame.transform.scale(treasureImage, (35, 40))
treasureImage = treasureImage.convert_alpha()

enemyImage = pygame.image.load("enemy.png")
enemyImage = pygame.transform.scale(enemyImage, (35, 40))
enemyImage = enemyImage.convert_alpha()


##########   Set Variables     ##########################

finished = False  # set parameter to end game

x = 450 - 35 / 2  # Starting position for player x axis
y = 650   # Starting Position for player y axis

treasureX = 450 - 35 / 2  #position for treasure box
treasureY = 50

enemyX = 100   #Position for enemy
enemyY = 580 - 10

font = pygame.font.SysFont("comicsans", 70) # Set font and size of text
level = 1 #Set level to 1
enemyNames = {0: "Klinky", 1: "Winky", 2: "Stinky", 3: "Blinky"} #create dictionary with enemy names
frame = pygame.time.Clock() #Set framerate to clock
collisionTreasure = False # Set initial treasure collision to false
collisionEnemy = False # Set initial enemy collision to false
movingRight = True # Set moving boolean
name = "" # open container for enemy name
enemies = [(enemyX, enemyY, movingRight)] # create list for enemy location and set movement
collected = 0  #Set score to 0

###### Colors RGB Setup  #########

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

######### Game Master Loop   ###################

while finished == False:  # While our game is not finished
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit game from pygame
            finished = True

    pressedKeys = pygame.key.get_pressed()
    # action when key pressed
    enemyIndex = 0 # Sets enemy index to 0

    # Make enemies move back and forth accross screen
    for enemyX, enemyY, movingRight in enemies:
        if enemyX >= 800 - 35:
            movingRight = False
        elif enemyX <= 100:
            movingRight = True
        if movingRight == True:
            enemyX += 5 * level #increases speed with difficulty
        else:
            enemyX -= 5 * level
        enemies[enemyIndex] = (enemyX, enemyY, movingRight)
        enemyIndex += 1

    ####### moves the player up the screen
    if pressedKeys[pygame.K_SPACE] == 1:
        y -= 15  #moves player this much when key pressed

    screen.blit(backgroundImage, (0, 0)) #show background image on screen
    screen.blit(treasureImage, (treasureX, treasureY))# show treasure image on screen
    screen.blit(playerImage, (x, y)) # Show player image on screen

    enemyIndex = 0 # Set index to 0

    ########### Enemy Collision  #########
    for enemyX, enemyY, movingRight in enemies:
        screen.blit(enemyImage, (enemyX, enemyY))
        collisionEnemy, y = checkCollision(x, y, enemyX, enemyY)
        if collisionEnemy == True:
            name = enemyNames[enemyIndex]
            textLose = font.render("You were killed by " + name, True, (RED))
            screen.blit(textLose, (450 - textLose.get_width() / 2, 350 - textLose.get_height() / 2))
            pygame.display.flip()
            frame.tick(1)
        frame.tick(30)
        enemyIndex += 1 #adds 1 to the enemy count

    ######## Treasure Collision  ########

    collisionTreasure, y = checkCollision(x, y, treasureX, treasureY)
    # checks collision with treasure
    if collisionTreasure == True:
        level += 1  #adds 1 to the level
        collected += 100 * level
        hi_score(collected)
        enemies.append((enemyX - 50 * level, enemyY - 50 * level, False))
        textWin = font.render("You've reached level " + str(level), True, (BLUE))
        screen.blit(textWin, (450 - textWin.get_width() / 2, 350 - textWin.get_height() / 2))
        pygame.display.flip()
        frame.tick(1)

######## Global refresh rate ###########

    pygame.display.flip() #updates display
    frame.tick(30) #sets frame rate to 30


