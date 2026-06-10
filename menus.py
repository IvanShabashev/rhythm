import pygame
import sys
from pygame.locals import *
from playsound import playsound
import time
from pydub import AudioSegment
import struct
from queue import Queue


def mainMenu():
    # The play button should be in the center of the screen and
    # should take up one third of the screen's height
    playHeight = res[1] // 3
    playX = res[0]//2 - playHeight//2
    playY = res[1]//2 - playHeight//2
    # Instructions button should be
    # 2/3 the size of the play button
    # It should be centered to the middle
    # of the screen along the Y axis and
    # the first quarter of the screen on the X axis
    instHeight = (2 * res[1]) // 9
    instX = res[0]//4 - instHeight//2
    instY = res[1]//2 - instHeight//2
    # Credits button is mostly
    # the same as the instructions button
    # except aligned to the third quarter
    # of the screen along the X axis instead
    # of the first quarter
    credHeight = (2 * res[1]) // 9
    credX = (3 * res[0])//4 - credHeight//2
    credY = res[1]//2 - credHeight//2
    # The following rectangles heights create the circle for the
    # copyright (©) used to represent the credits.
    cred1Height = (14 * res[1]) // 81
    cred2Height = (10 * res[1]) // 81
    # Out of the 3 lines used to represent the instructions,
    # one should be wider and the other two should be shorter.
    # They should also take up 1/7 of the button each in terms of
    # height (to allow for a pattern of gap-line-gap-line-gap-line-gap).
    # Finally, the top line is centered the same as the instructions
    # button, while the other two lines are aligned to the left based
    # on the top line.
    instLine1Width = (14 * res[1]) // 81
    instLineHeight = (2 * res[1]) // 63
    instLine23Width = (10 * res[1]) // 81
    instLinesX = res[0]//4 - instLine1Width//2
    # Load the play button which I created by modifying the Terminus font's "V"
    playButton = pygame.image.load("res/play.png")
    # Scale the play button accordingly
    factor = res[1] / 173
    playButton = pygame.transform.scale_by(playButton, factor)
    # The title text's height should take up
    # roughly 2/3 of the top third of the screen
    titleHeight = (2 * res[1]) // 9
    titleFont = pygame.font.Font("res/Terminus.ttf", titleHeight)
    title = titleFont.render("RHYTHM", True, WHITE)
    # Align the title to be centered to the middle of the
    # screen along the X axis and the middle of the
    # top third of the screen along the Y axis
    titleRect = title.get_rect()
    titleRect.center = (res[0] // 2, res[1] // 6)
    # Calculate the height for the "C" in the ©
    credCHeight = (10 * res[1]) // 81
    credFont = pygame.font.Font("res/Terminus.ttf", credCHeight)
    # Make the "C" bold
    credFont.set_bold(True)
    credC = credFont.render("C", True, WHITE)
    # Align the "C" to be centered to the credits button
    credRect = credC.get_rect()
    credRect.center = ((3 * res[0]) // 4, res[1] // 2)
    # Initialise the "hitboxes" for the buttons, where the user's mouse
    # will cause the button to be highlited and, if clicked,
    # trigger an action.
    playCoords = ((playX, playY), (playX + playHeight, playY + playHeight))
    credCoords = ((credX, credY), (credX + credHeight, credY + credHeight))
    instCoords = ((instX, instY), (instX + instHeight, instY + instHeight))
    while True:
        # Assume the user has not clicked the mouse yet
        clicked = False
        for event in pygame.event.get():
            # Allow person to close the game
            if event.type == pygame.QUIT:
                sys.exit()
            # Check if person has clicked the mouse
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = True
            # Quit game if person presses escape
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        # Get player's mouse position
        mouse = pygame.mouse.get_pos()
        # Fill the background with dark slate
        pygame.draw.rect(DISPLAY, DSLATE, (0, 0, res[0], res[1]))
        # If a user hovers over a button, highlight it iron.
        # Otherwise, colour it metal
        if (mouse[0] >= playCoords[0][0] and
                mouse[0] <= playCoords[1][0] and
                mouse[1] >= playCoords[0][1] and
                mouse[1] <= playCoords[1][1]):
            # Draw play button (hovered)
            pygame.draw.rect(
                                DISPLAY,
                                IRON,
                                (playX, playY, playHeight, playHeight)
                            )
            if clicked:
                songSelect()
            clicked = 0
        else:
            # Draw play button (normal)
            pygame.draw.rect(
                                DISPLAY,
                                METAL,
                                (playX, playY, playHeight, playHeight)
                            )

        if (mouse[0] >= instCoords[0][0] and
                mouse[0] <= instCoords[1][0] and
                mouse[1] >= instCoords[0][1] and
                mouse[1] <= instCoords[1][1]):
            # Draw instructions button (hovered)
            pygame.draw.rect(
                                DISPLAY,
                                IRON,
                                (instX, instY, instHeight, instHeight)
                            )
            if clicked:
                instructions()
            clicked = 0
        else:
            # Draw instructions button (normal)
            pygame.draw.rect(
                                DISPLAY,
                                METAL,
                                (instX, instY, instHeight, instHeight)
                            )

        if (mouse[0] >= credCoords[0][0] and
                mouse[0] <= credCoords[1][0] and
                mouse[1] >= credCoords[0][1] and
                mouse[1] <= credCoords[1][1]):
            # Draw credits button (hovered)
            pygame.draw.rect(
                                DISPLAY,
                                IRON,
                                (credX, credY, credHeight, credHeight)
                            )
            # Draw the white outline for the © symbol
            pygame.draw.rect(
                                DISPLAY,
                                WHITE,
                                (
                                    (3 * res[0])//4 - cred1Height//2,
                                    res[1]//2 - cred1Height//2,
                                    cred1Height,
                                    cred1Height
                                )
                            )
            # Draw the iron (as it is hovered)
            # inside of the © symbol
            pygame.draw.rect(
                                DISPLAY,
                                IRON,
                                (
                                    (3 * res[0])//4 - cred2Height//2,
                                    res[1]//2 - cred2Height//2,
                                    cred2Height,
                                    cred2Height
                                )
                            )
            if clicked:
                creds()
            clicked = 0
        else:
            # Draw credits button (normal)
            pygame.draw.rect(
                                DISPLAY,
                                METAL,
                                (credX, credY, credHeight, credHeight)
                            )
            # Draw the white outline for the © symbol
            pygame.draw.rect(
                                DISPLAY,
                                WHITE,
                                (
                                    (3 * res[0])//4 - cred1Height//2,
                                    res[1]//2 - cred1Height//2,
                                    cred1Height,
                                    cred1Height
                                )
                            )
            # Draw the metal (as it is normal)
            # inside of the © symbol
            pygame.draw.rect(
                                DISPLAY,
                                METAL,
                                (
                                    (3 * res[0])//4 - cred2Height//2,
                                    res[1]//2 - cred2Height//2,
                                    cred2Height,
                                    cred2Height
                                )
                            )
        # Draw the top of the three
        # instruction lines
        pygame.draw.rect(
                             DISPLAY,
                             WHITE,
                             (
                                instLinesX,
                                instY + instLineHeight,
                                instLine1Width,
                                instLineHeight
                             )
                        )
        # Draw the middle instruction line
        pygame.draw.rect(
                            DISPLAY,
                            WHITE,
                            (
                                instLinesX,
                                instY + instLineHeight*3,
                                instLine23Width,
                                instLineHeight
                            )
                        )
        # Draw the bottom instruction line
        pygame.draw.rect(
                            DISPLAY,
                            WHITE,
                            (
                                instLinesX,
                                instY + instLineHeight*5,
                                instLine23Width,
                                instLineHeight)
                        )
        # Draw the PNG of the play button and the texts
        DISPLAY.blit(
                        playButton,
                        playButton.get_rect(center=(res[0]//2, res[1]//2))
                    )
        DISPLAY.blit(title, titleRect)
        DISPLAY.blit(credC, credRect)
        # Update the display
        pygame.display.update()
        # Lock the game to 240 FPS
        clock.tick(240)


def creds():
    # Read list of people in the game's credits
    artists = open("credits.txt").read().split("\n")
    # Keep track of how far down the list the user has scrolled
    credHead = 0
    # Calculate position of the instruction text
    # It should be centered along the X axis
    # The position along the Y axis was mostly educated trial and error
    instY1 = (31 * res[1]) // 36
    instY2 = (33 * res[1]) // 36
    instX = res[0] // 2
    # The height of the instruction text was also mostly guesswork
    # but since it's relative to the screen height, it will scale
    # properly
    instHeight = (3 * res[1]) // 72
    # Render the text, positioning it according to the calculations
    instFont = pygame.font.Font("res/Terminus.ttf", instHeight)
    inst1 = instFont.render("USE UP/DOWN ARROW KEYS TO SCROLL", True, WHITE)
    inst2 = instFont.render("PRESS ESC TO EXIT", True, WHITE)
    inst1Rect = inst1.get_rect()
    inst1Rect.center = (instX, instY1)
    inst2Rect = inst2.get_rect()
    inst2Rect.center = (instX, instY2)
    # Centre people's names along the X axis
    # The textbox containing people's names should be 2/3 of the screen
    # at 10 names in the box, each name should be 2/30 of the screen height
    artistX = res[0] // 2
    artistHeight = (2 * res[1]) // 30
    # each artist's name is at a different Y position
    # the Y positions are calculated to be spread evenly
    artistYs = []
    for i in range(min(10, len(artists))):
        artistYs.append((i + 1) * artistHeight)
    artistFont = pygame.font.Font("res/Terminus.ttf", artistHeight)

    while True:
        artistSurfaces = []
        artistRects = []
        for event in pygame.event.get():
            # Allow person to close the game
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                # Allow person to scroll through the list of names
                if event.key == pygame.K_DOWN and credHead < len(artists)-10:
                    credHead += 1
                elif event.key == pygame.K_UP and credHead > 0:
                    credHead -= 1
                # Allow person to go to the previous menu screen
                elif event.key == pygame.K_ESCAPE:
                    return

        # Fill screen with background colour and draw the instructions text
        pygame.draw.rect(DISPLAY, DSLATE, (0, 0, res[0], res[1]))
        DISPLAY.blit(inst1, inst1Rect)
        DISPLAY.blit(inst2, inst2Rect)
        # Render 10 artist's names, depending on
        # how far down the user has scrolled
        for i in range(min(10, len(artists))):
            artistSurfaces.append(artistFont.render(
                                                        artists[credHead + i],
                                                        True,
                                                        WHITE
                                                   ))
            artistRects.append(artistSurfaces[i].get_rect())
            artistRects[i].center = (artistX, artistYs[i])
            DISPLAY.blit(artistSurfaces[i], artistRects[i])
        pygame.display.update()
        clock.tick(240)


def instructions():
    slide = 0
    instY1 = (31 * res[1]) // 36
    instY2 = (33 * res[1]) // 36
    instX = res[0] // 2
    instHeight = (3 * res[1]) // 72
    instFont = pygame.font.Font("res/Terminus.ttf", instHeight)
    inst1 = instFont.render("USE LEFT/RIGHT ARROW KEYS TO NAVIGATE TUTORIAL", True, WHITE)
    inst2 = instFont.render("PRESS ESC TO EXIT", True, WHITE)
    inst1Rect = inst1.get_rect()
    inst1Rect.center = (instX, instY1)
    inst2Rect = inst2.get_rect()
    inst2Rect.center = (instX, instY2)
    while True:
        for event in pygame.event.get():
            # Allow person to close the game
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and slide < 2:
                    slide += 1
                elif event.key == pygame.K_LEFT and slide > 0:
                    slide -= 1
                elif event.key == pygame.K_ESCAPE:
                    return

        pygame.draw.rect(DISPLAY, DSLATE, (0, 0, res[0], res[1]))
        DISPLAY.blit(inst1, inst1Rect)
        DISPLAY.blit(inst2, inst2Rect)
        if slide == 0:
            pygame.draw.circle(DISPLAY, METAL, (res[0]//2, res[1]//2), min(res)//4)
        elif slide == 1:
            pygame.draw.circle(DISPLAY, WHITE, (res[0]//2, res[1]//2), min(res)//4)
        elif slide == 2:
            pygame.draw.circle(DISPLAY, WHITE, (res[0]//2, res[1]//2), min(res)//4)
        pygame.display.update()
        clock.tick(240)


def songSelect():
    print("TODO: ADD SONG SELECTION SCREEN")


# Initialise pygame
pygame.init()
clock = pygame.time.Clock()
# Choose highest possible reslution for fullscreen
res = pygame.display.list_modes()[0]
DISPLAY = pygame.display.set_mode(res, 0, 32)
pygame.display.toggle_fullscreen()
# Define colours that will be used (white, platinum, alabaster, light slate,
# medium slate, dark slate, iron, metal, and black)
WHITE = (0xF8, 0xF9, 0xFA)
PLAT = (0xE9, 0xEC, 0xEF)
ALABAST = (0xDE, 0xE2, 0xE6)
LSLATE = (0xCE, 0xD4, 0xDA)
MSLATE = (0xAD, 0xB5, 0xBD)
DSLATE = (0x6C, 0x75, 0x7D)
IRON = (0x49, 0x50, 0x57)
METAL = (0x34, 0x3A, 0x40)
BLACK = (0x21, 0x25, 0x29)
FULLBLACK = (0, 0, 0)
# Render main menu
mainMenu()
