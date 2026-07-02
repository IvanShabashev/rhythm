import pygame
import sys
from pygame.locals import *
import time
import struct
from queue import Queue
import os
from level import Level


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
            # Allow user to close the game
            if event.type == pygame.QUIT:
                sys.exit()
            # Check if user has clicked the mouse
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = True
            # Quit game if user presses escape
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
            # Allow user to close the game
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                # Allow user to scroll through the list of names
                if event.key == pygame.K_DOWN and credHead < len(artists)-10:
                    credHead += 1
                elif event.key == pygame.K_UP and credHead > 0:
                    credHead -= 1
                # Allow user to go to the previous menu screen
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

        # Update display and lock to 240 FPS
        pygame.display.update()
        clock.tick(240)


def instructions():
    # This will count the slide the user is on
    slide = 0
    # Set up the control instructions
    contY1 = (31 * res[1]) // 36
    contY2 = (33 * res[1]) // 36
    contX = res[0] // 2
    contHeight = (3 * res[1]) // 72
    contFont = pygame.font.Font("res/Terminus.ttf", contHeight)
    cont1 = contFont.render(
                                "USE LEFT/RIGHT ARROW KEYS " +
                                "TO NAVIGATE TUTORIAL",
                                True,
                                WHITE
                           )
    cont2 = contFont.render("PRESS ESC TO EXIT", True, WHITE)
    cont1Rect = cont1.get_rect()
    cont1Rect.center = (contX, contY1)
    cont2Rect = cont2.get_rect()
    cont2Rect.center = (contX, contY2)
    # Calculate the position of the
    # general instructions
    instY1 = (3 * res[1]) // 36
    instY2 = (5 * res[1]) // 36
    while True:
        for event in pygame.event.get():
            # Allow user to close the game
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                # Switch slides with arrow keys
                # Use ESC to exit
                if event.key == pygame.K_RIGHT and slide < 2:
                    slide += 1
                elif event.key == pygame.K_LEFT and slide > 0:
                    slide -= 1
                elif event.key == pygame.K_ESCAPE:
                    return

        # Fill screen
        pygame.draw.rect(DISPLAY, DSLATE, (0, 0, res[0], res[1]))
        # Display control instructions
        DISPLAY.blit(cont1, cont1Rect)
        DISPLAY.blit(cont2, cont2Rect)
        if slide == 0:
            # Hit object #1
            pygame.draw.circle(
                                   DISPLAY,
                                   WHITE,
                                   (3*res[0]//8-res[1]//4, res[1]//2),
                                   res[1]//80
                              )
            # Hit object #2
            pygame.draw.circle(
                                   DISPLAY,
                                   WHITE,
                                   ((3*res[0])//16-res[1]//4, res[1]//2),
                                   res[1]//80
                              )
            # Center circle
            pygame.draw.circle(
                                   DISPLAY,
                                   METAL,
                                   (res[0]//2, res[1]//2),
                                   res[1]//4
                              )
            # General instructions
            inst1 = contFont.render(
                                        "WHEN YOU PLAY RHYTHM, " +
                                        "SMALL OBJECTS WILL APPROACH " +
                                        "A LARGE CIRCLE IN THE MIDDLE",
                                        True,
                                        WHITE
                                   )
            inst1Rect = inst1.get_rect()
            inst1Rect.center = (contX, instY1)
            DISPLAY.blit(inst1, inst1Rect)

        elif slide == 1:
            # Hit object #1
            pygame.draw.circle(
                                   DISPLAY,
                                   WHITE,
                                   (res[0]//2-res[1]//4, res[1]//2),
                                   res[1]//80
                              )
            # Hit object #2
            pygame.draw.circle(
                                   DISPLAY,
                                   WHITE,
                                   ((5*res[0])//16-res[1]//4, res[1]//2),
                                   res[1]//80
                              )
            # Center circle
            pygame.draw.circle(
                                   DISPLAY,
                                   WHITE,
                                   (res[0]//2, res[1]//2),
                                   res[1]//4
                              )
            # General instructions
            inst1 = contFont.render(
                                        "AIM TO PUSH A CONTROLLER BUTTON " +
                                        "WHEN THE OBJECT TOUCHES THE CIRCLE",
                                        True,
                                        WHITE
                                   )
            inst1Rect = inst1.get_rect()
            inst1Rect.center = (contX, instY1)
            inst2 = contFont.render(
                                        "YOU CAN USE THE D, F, J, " +
                                        "K, AND SPACE KEYS",
                                        True,
                                        WHITE
                                   )
            inst2Rect = inst2.get_rect()
            inst2Rect.center = (contX, instY2)
            DISPLAY.blit(inst1, inst1Rect)
            DISPLAY.blit(inst2, inst2Rect)

        elif slide == 2:
            # Hit object #1
            pygame.draw.circle(
                                   DISPLAY,
                                   WHITE,
                                   (res[0]//2-res[1]//4, res[1]//2),
                                   res[1]//80
                              )
            # Hit object #2
            pygame.draw.circle(
                                   DISPLAY,
                                   WHITE,
                                   ((5*res[0])//16-res[1]//4, res[1]//2),
                                   res[1]//80
                              )
            # Center circle
            pygame.draw.circle(
                                   DISPLAY,
                                   WHITE,
                                   (res[0]//2, res[1]//2),
                                   res[1]//4
                              )
            # General instructions
            inst1 = contFont.render(
                                        "EACH HIT IS GRADED OUT OF 999" +
                                        " DEPENDING ON HOW " +
                                        "MANY MILLISECONDS OFF IT WAS",
                                        True,
                                        WHITE
                                   )
            inst1Rect = inst1.get_rect()
            inst1Rect.center = (contX, instY1)
            # Hit score display
            hitHeight = res[1]//4
            hitY = res[1]//2
            hitFont = pygame.font.Font("res/Terminus.ttf", hitHeight)
            hitText = hitFont.render("999", True, FULLBLACK)
            hitRect = hitText.get_rect()
            hitRect.center = (contX, hitY)
            DISPLAY.blit(hitText, hitRect)
            DISPLAY.blit(inst1, inst1Rect)

        # Update display and lock to 240 FPS
        pygame.display.update()
        clock.tick(240)


def songSelect():
    # Keep track of how far down the list the user has scrolled
    lvlHead = 0
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
    # Height of the song name text should be a bit bigger
    # than the artists name and the artists name uses the
    # same font size as the controls
    nameHeight = (3 * instHeight) // 2
    nameFont = pygame.font.Font("res/Terminus.ttf", nameHeight)
    # Render the text, positioning it according to the calculations
    instFont = pygame.font.Font("res/Terminus.ttf", instHeight)
    inst1 = instFont.render("USE UP/DOWN ARROW KEYS TO SCROLL", True, WHITE)
    inst2 = instFont.render("PRESS ESC TO EXIT", True, WHITE)
    inst1Rect = inst1.get_rect()
    inst1Rect.center = (instX, instY1)
    inst2Rect = inst2.get_rect()
    inst2Rect.center = (instX, instY2)
    # Calculate the coordinates and dimensions of the container
    lvlBoxX = (3 * res[0])//10
    lvlBoxY = (5 * res[1])//72
    lvlBoxWidth = (2 * res[0])//5
    lvlBoxHeight = (7 * res[1])//10
    # Calculate the coordinates and dimensions of the
    # level boxes
    lvlX = lvlBoxX + instHeight
    lvlHeight = (lvlBoxHeight - 4*instHeight)//3
    lvlWidth = lvlBoxWidth - 2*instHeight
    lvlY1 = lvlBoxY + instHeight
    lvlY2 = lvlY1 + instHeight + lvlHeight
    lvlY3 = lvlY2 + instHeight + lvlHeight
    # Calculate margins for the level texts
    textMargin = (lvlHeight-instHeight-nameHeight)//3
    # Get all levels from the directory
    levels = os.listdir("levels")
    # Filter out the audio files to leave only the data files
    levels = [i for i in levels if i.endswith(".rtm")]
    # Initialise a level object for each data file
    levels = [Level(i) for i in levels]
    # Calculate positions for level textboxes
    textX = lvlX + textMargin
    nameY1 = lvlY1 + textMargin
    artistY1 = nameY1 + textMargin + nameHeight
    nameY2 = lvlY2 + textMargin
    artistY2 = nameY2 + textMargin + nameHeight
    nameY3 = lvlY3 + textMargin
    artistY3 = nameY3 + textMargin + nameHeight

    while True:
        # Assume the user has not clicked the mouse yet
        clicked = False
        for event in pygame.event.get():
            # Allow user to close the game
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                # Allow user to scroll through the list of names
                if event.key == pygame.K_DOWN and lvlHead < len(levels)-3:
                    lvlHead += 1
                elif event.key == pygame.K_UP and lvlHead > 0:
                    lvlHead -= 1
                # Allow user to go to the previous menu screen
                elif event.key == pygame.K_ESCAPE:
                    return
            # Check if user has clicked the mouse
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = True

        # Get player's mouse position
        mouse = pygame.mouse.get_pos()
        # Fill screen with background colour and draw the instructions text
        pygame.draw.rect(DISPLAY, DSLATE, (0, 0, res[0], res[1]))
        # Draw container for levels
        pygame.draw.rect(DISPLAY, METAL, (
                                              lvlBoxX,
                                              lvlBoxY,
                                              lvlBoxWidth,
                                              lvlBoxHeight
                                         ))
        # Draw the background for level 1 and colour it based
        # on whether the user hovered their mouse over it
        if (mouse[0] >= lvlX and
                mouse[0] <= lvlX + lvlWidth and
                mouse[1] >= lvlY1 and
                mouse[1] <= lvlY1 + lvlHeight):
            pygame.draw.rect(DISPLAY, IRON, (lvlX, lvlY1, lvlWidth, lvlHeight))
            # if the player clicks the button, take them to the song menu
            if clicked:
                song(levels[lvlHead])
        else:
            pygame.draw.rect(DISPLAY, BLACK, (
                                                  lvlX,
                                                  lvlY1,
                                                  lvlWidth,
                                                  lvlHeight
                                             ))

        # Render textboxes for the first level on the screen
        name1 = nameFont.render(levels[lvlHead].name, True, WHITE)
        artist1 = instFont.render(levels[lvlHead].artist, True, WHITE)
        name1Rect = name1.get_rect()
        artist1Rect = artist1.get_rect()
        name1Rect.topleft = (textX, nameY1)
        artist1Rect.topleft = (textX, artistY1)
        # Draw the background for level 2 and colour it based
        # on whether the user hovered their mouse over it
        if (mouse[0] >= lvlX and
                mouse[0] <= lvlX + lvlWidth and
                mouse[1] >= lvlY2 and
                mouse[1] <= lvlY2 + lvlHeight):
            pygame.draw.rect(DISPLAY, IRON, (lvlX, lvlY2, lvlWidth, lvlHeight))
            if clicked:
                # if the player clicks the button, take them to the song menu
                song(levels[lvlHead+1])
        else:
            pygame.draw.rect(DISPLAY, BLACK, (
                                                  lvlX,
                                                  lvlY2,
                                                  lvlWidth,
                                                  lvlHeight
                                             ))

        # Render textboxes for the second level on the screen
        # currently disabled as there aren't enough levels
        """name2 = nameFont.render(levels[lvlHead+1].name, True, WHITE)
        artist2 = instFont.render(levels[lvlHead+1].artist, True, WHITE)
        name2Rect = name2.get_rect()
        artist2Rect = artist2.get_rect()
        name2Rect.topleft = (textX, nameY2)
        artist2Rect.topleft = (textX, artistY2)"""
        # Draw the background for level 3 and colour it based
        # on whether the user hovered their mouse over it
        if (mouse[0] >= lvlX and
                mouse[0] <= lvlX + lvlWidth and
                mouse[1] >= lvlY3 and
                mouse[1] <= lvlY3 + lvlHeight):
            pygame.draw.rect(DISPLAY, IRON, (lvlX, lvlY3, lvlWidth, lvlHeight))
            if clicked:
                # if the player clicks the button, take them to the song menu
                song(levels[lvlHead+2])
        else:
            pygame.draw.rect(DISPLAY, BLACK, (
                                                  lvlX,
                                                  lvlY3,
                                                  lvlWidth,
                                                  lvlHeight
                                             ))

        # Render textboxes for the third level on the screen
        # currently disabled as there aren't enough levels
        """name3 = nameFont.render(levels[lvlHead+2].name, True, WHITE)
        artist3 = instFont.render(levels[lvlHead+2].artist, True, WHITE)
        name3Rect = name3.get_rect()
        artist3Rect = artist3.get_rect()
        name3Rect.topleft = (textX, nameY3)
        artist3Rect.topleft = (textX, artistY3)"""
        # Render text explaining controls
        DISPLAY.blit(inst1, inst1Rect)
        DISPLAY.blit(inst2, inst2Rect)
        # Blit the level textboxes
        # 2 and 3 currently disables as there aren't enough levels
        DISPLAY.blit(name1, name1Rect)
        DISPLAY.blit(artist1, artist1Rect)
        """DISPLAY.blit(name2, name2Rect)
        DISPLAY.blit(artist2, artist2Rect)
        DISPLAY.blit(name3, name3Rect)
        DISPLAY.blit(artist3, artist3Rect)"""

        # Update display and lock to 240 FPS
        pygame.display.update()
        clock.tick(240)


def song(level):
    # Set up the exit instructions
    contY = (33 * res[1]) // 36
    contX = res[0] // 2
    contHeight = (3 * res[1]) // 72
    contFont = pygame.font.Font("res/Terminus.ttf", contHeight)
    cont = contFont.render("PRESS ESC TO EXIT", True, WHITE)
    contRect = cont.get_rect()
    contRect.center = (contX, contY)
    # Set up level name text
    nameX = res[1] // 60
    nameY = res[1] // 60
    nameHeight = (18 * res[1]) // 90
    nameFont = pygame.font.Font("res/Terminus.ttf", nameHeight)
    name = nameFont.render(level.name, True, WHITE)
    nameRect = name.get_rect()
    nameRect.topleft = (nameX, nameY)
    # Set up artist name text
    artistY = nameY + nameHeight
    artistHeight = nameHeight // 2
    artistFont = pygame.font.Font("res/Terminus.ttf", artistHeight)
    artist = artistFont.render(level.artist, True, WHITE)
    artistRect = artist.get_rect()
    artistRect.topleft = (nameX, artistY)
    # Set up "HIGH SCORES" label
    hsY = res[1] // 3
    hs = contFont.render("HIGH SCORES:", True, WHITE)
    hsRect = hs.get_rect()
    hsRect.topleft = (nameX, hsY)
    # Set up play instruction text
    # Split over four textboxes, one per line
    playX = (2 * res[0]) // 3
    playY3 = res[1] // 2 - res[1] // 40
    playY4 = playY3 + nameHeight - res[1] // 40
    playY2 = playY3 - nameHeight + res[1] // 40
    playY1 = playY2 - nameHeight + res[1] // 40
    play1 = nameFont.render("PRESS", True, WHITE)
    play2 = nameFont.render("SPACE", True, WHITE)
    play3 = nameFont.render("TO", True, WHITE)
    play4 = nameFont.render("PLAY", True, WHITE)
    play1Rect = play1.get_rect()
    play2Rect = play2.get_rect()
    play3Rect = play3.get_rect()
    play4Rect = play4.get_rect()
    play1Rect.topleft = (playX, playY1)
    play2Rect.topleft = (playX, playY2)
    play3Rect.topleft = (playX, playY3)
    play4Rect.topleft = (playX, playY4)

    while True:
        for event in pygame.event.get():
            # Allow user to close the game
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                # Use ESC to exit
                # Press SPACE to start level
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_SPACE:
                    play(level)

        # Fill screen
        pygame.draw.rect(DISPLAY, DSLATE, (0, 0, res[0], res[1]))
        # Blit all textboxes
        DISPLAY.blit(cont, contRect)
        DISPLAY.blit(name, nameRect)
        DISPLAY.blit(artist, artistRect)
        DISPLAY.blit(hs, hsRect)
        DISPLAY.blit(play1, play1Rect)
        DISPLAY.blit(play2, play2Rect)
        DISPLAY.blit(play3, play3Rect)
        DISPLAY.blit(play4, play4Rect)
        # Update display and lock to 240 FPS
        pygame.display.update()
        clock.tick(240)


def play(level):
    # Load the song audio
    pygame.mixer.music.load(level.songName)
    # Initialise the queue which will store the hit timings
    hits = Queue(maxsize=len(level.hits))
    # Initialise the font that will show the score per hit
    hitHeight = res[1]//4
    hitFont = pygame.font.Font("res/Terminus.ttf", hitHeight)
    # Initialise total score font and location
    scoreX = res[1] // 60
    scoreY = res[1] // 60
    scoreHeight = res[1] // 10
    scoreFont = pygame.font.Font("res/Terminus.ttf", scoreHeight)
    # Store center of screen
    center = (res[0]//2, res[1]//2)
    # Variable to store player's score
    score = 0
    # This will keep track of key presses
    # the first item in the list is whether the key is being pressed
    # the second item is whether the press has been used already on a hit
    keys = {
               pygame.K_SPACE: [False, False],
               pygame.K_d: [False, False],
               pygame.K_f: [False, False],
               pygame.K_j: [False, False],
               pygame.K_k: [False, False]
           }
    # When the user pauses, the timing will go out of sync
    # this variable is used to adjust for that
    pauseOffset = 0
    # Play song
    pygame.mixer.music.play()
    # Synchronise timing offsets to current time
    x = time.time()
    for i in level.hits:
        hits.put(x+i)

    while True:
        for event in pygame.event.get():
            # Allow user to close the game
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # If a key is pressed down, mark it as active
                if event.key in keys:
                    keys[event.key][0] = True
            elif event.type == pygame.KEYUP:
                # Use ESC to pause
                if event.key == pygame.K_ESCAPE:
                    # Pause music and start timing how long the user is paused for
                    pygame.mixer.music.pause()
                    pauseLength = time.time()
                    # pause returns True if the user wishes to exit the level
                    # if the user wants to continue, pause returns false
                    if pause():
                        return
                    # calculate pause adjustment
                    pauseOffset += time.time() - pauseLength
                    # unpause the music
                    pygame.mixer.music.unpause()
                elif event.key in keys:
                    # If a key is no longer pressed, mark it as inactive
                    # additionally, mark it as being open to presses
                    keys[event.key][0] = False
                    keys[event.key][1] = False

        # Adjust timings according to the pauses
        timeOff = time.time() - pauseOffset
        # Fill screen
        pygame.draw.rect(DISPLAY, DSLATE, (0, 0, res[0], res[1]))
        # flash keeps track of whether a key is being held down
        flash = False
        # click keeps track of whether a key was just pressed on this frame
        click = False
        for key, press in keys.items():
            if press[0]:
                flash = True
                if not press[1]:
                    click = True
                    keys[key][1] = True
        # Flash the circle with white if the user is holding a key
        if flash:
            pygame.draw.circle(DISPLAY, WHITE, center, res[1]//4)
        else:
            pygame.draw.circle(DISPLAY, METAL, center, res[1]//4)

        # Only work with hit objects if there are some hit objects left
        # otherwise, the game crashes
        if not hits.empty():
            # Render hit objects
            # At the same time, if the hit object passes the halfway
            # point on the screen, remove it and count it as a missed object.
            missed = False
            for hit in hits.queue:
                hitX = (res[0]//2 - res[1]//4) * (1 - (hit-timeOff))
                if hitX > res[0]//2:
                    missed = True
                elif hitX > 0:
                    pygame.draw.circle(
                                           DISPLAY,
                                           WHITE,
                                           (hitX, res[1]//2),
                                           res[1]//80
                                      )
            if missed:
                hits.get()
            # If the user has just pressed a key on this frame
            # Count it as a hit
            if click:
                # Do not allow negative scores
                hitVal = max(0, int((1 - abs(timeOff - hits.get()))*1000))
                score += hitVal

            
            # If circle is white, display the score of the last hit
            if flash:
                hitText = hitFont.render(str(hitVal), True, FULLBLACK)
                hitRect = hitText.get_rect()
                hitRect.center = center
                DISPLAY.blit(hitText, hitRect)

        # Display the player's current score
        scoreText = scoreFont.render(str(score), True, WHITE)
        scoreRect = scoreText.get_rect()
        scoreRect.topleft = (scoreX, scoreY)
        DISPLAY.blit(scoreText, scoreRect)

        # If the song finished playing, the level ends
        if not pygame.mixer.music.get_busy():
            done(level, score)
            return
        # Update display and lock to 240 FPS
        pygame.display.update()
        clock.tick(240)


def pause():
    # Initialise and position control instructions
    # do NOT fill screen as we want the user to be
    # able to see the game in the background
    textHeight = (3 * res[1])//72
    textFont = pygame.font.Font("res/Terminus.ttf", textHeight)
    textX = res[0]//2
    textY1 = (3 * res[1]) // 36
    textY2 = (33 * res[1]) // 36
    text1 = textFont.render("PRESS SPACE TO CONTINUE", True, WHITE)
    text2 = textFont.render("PRESS ESC TO EXIT", True, WHITE)
    text1Rect = text1.get_rect()
    text2Rect = text2.get_rect()
    text1Rect.center = (textX, textY1)
    text2Rect.center = (textX, textY2)
    DISPLAY.blit(text1, text1Rect)
    DISPLAY.blit(text2, text2Rect)

    while True:
        for event in pygame.event.get():
            # Allow user to close the game
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                # Use ESC to exit
                # Press SPACE to continue game
                # pause returns True if the user wishes to exit the level
                # if the user wants to continue, pause returns false
                if event.key == pygame.K_ESCAPE:
                    return True
                elif event.key == pygame.K_SPACE:
                    return False
        # Update display and lock to 240 FPS
        pygame.display.update()
        clock.tick(240)


def done(level, score):
    # Initialise the two textboxes showing the user
    # their final score
    textHeight = (2 * res[1])//9
    textFont = pygame.font.Font("res/Terminus.ttf", textHeight)
    textX = res[0]//2
    textY1 = res[1]//6
    textY2 = res[1]//2
    text1 = textFont.render("FINAL SCORE:", True, WHITE)
    text2 = textFont.render(str(score), True, WHITE)
    text1Rect = text1.get_rect()
    text2Rect = text2.get_rect()
    text1Rect.center = (textX, textY1)
    text2Rect.center = (textX, textY2)

    while True:
        for event in pygame.event.get():
            # Allow user to close the game
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                # Use ESC or SPACE to continues
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                    return

        # Fill screen
        pygame.draw.rect(DISPLAY, DSLATE, (0, 0, res[0], res[1]))
        # Blit the textboxes
        DISPLAY.blit(text1, text1Rect)
        DISPLAY.blit(text2, text2Rect)
        # Update display and lock to 240 FPS
        pygame.display.update()
        clock.tick(240)


# Fix issues when running outside of game directory
os.chdir(os.path.dirname(__file__))
# Initialise pygame
pygame.init()
pygame.mixer.init()
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
