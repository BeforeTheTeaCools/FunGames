import pygame
from random import *
#This game aims to recreate the game a chimp was playing in this video https://youtu.be/qyJomdyjyvM

def setup(level):
    global display_time

    #difficulty scaling
    display_time = int(5 - (level // 3))
    display_time = max(display_time, 1)

    number_count = (level // 2) + 3
    number_count = min(number_count, 20) #we don't want it to get too large

    #put numbers randomly in the grid
    shuffle_grid(number_count)

def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130
    button_size = 110
    screen_left_margin = 55
    screen_top_margin = 20

    #[[0,0,0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0,0,0]]
    grid = [[0 for col in range(columns)] for row in range(rows)]

    number = 1 #1 to number_count
    while number <= number_count:
        row_ind = randrange(0,rows)
        col_ind = randrange(0,columns)

        if grid[row_ind][col_ind] == 0:
            grid[row_ind][col_ind] = number
            number += 1
    
            center_x = screen_left_margin + (col_ind * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_ind * cell_size) + (cell_size / 2)

            #draw button
            button = pygame.Rect(0,0,button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)
               

#show start screen
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    msg = game_font.render(f"Start", True, WHITE)
    msg_rect = msg.get_rect(center=start_button.center)
    msg1 = game_font1.render(f"Level {curr_level}", True, WHITE)
    msg1_rect = msg.get_rect(center=screen_center)
    screen.blit(msg, msg_rect)
    screen.blit(msg1, msg1_rect)

def display_game_screen():
    global hidden

    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #change from ms to seconds
        if elapsed_time > display_time:
            hidden = True

    for ind, rect in enumerate(number_buttons, start=1):
        if hidden:
            #draw square button
            pygame.draw.rect(screen, WHITE, rect)
        else:
            #draw number
            cell_text = game_font1.render(str(ind), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)

def check_buttons(pos):
    global start, start_ticks

    if start: #game started?
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks() #start timer

def check_number_buttons(pos):
    global hidden, start, curr_level

    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]: #clicked on correct button
                print("Correct")
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                print("Wrong")
                game_over()
            break
    #if got everything correct, move on to next level/setup
    if len(number_buttons) == 0:
        start = False
        hidden = False
        curr_level += 1
        setup(curr_level)

#game over
def game_over():
    global running

    running = False
    msg = game_font1.render(f"You failed on level {curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2))
    screen.fill(BLACK)
    screen.blit(msg, msg_rect)

#initialization
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 60) #pick font
game_font1 = pygame.font.Font(None, 120)

#start button
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120, screen_height - 120)

screen_center = (screen_width/2.33, screen_height/2) #location to display logo at start page
#color
BLACK = (0,0,0) #RGB
WHITE = (255,255,255)
GRAY = (50,50,50)

curr_level = 1
number_buttons = [] #buttons players have to click on
display_time = None
start_ticks = None
#game start?
start = False
#for hiding numbers ex: if user clicked on button
hidden = False
#set up before game starts
setup(curr_level)

#game loop
running = True #to check if the game is running
while running:

    click_pos = None

    for event in pygame.event.get(): #what event happened?
        if event.type == pygame.QUIT: 
            running = False #game no longer running
        elif event.type == pygame.MOUSEBUTTONUP: #if mouse clicks
            click_pos = pygame.mouse.get_pos()


    #color screen black
    screen.fill(BLACK)

    if start:
        display_game_screen()
    else:
        display_start_screen()

    #if user clicked somewhere
    if click_pos:
        check_buttons(click_pos)

    #update screen
    pygame.display.update()

pygame.time.delay(5000)

pygame.quit()
