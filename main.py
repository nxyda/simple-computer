import pygame
import sys
import subprocess

pygame.init()
screen_width = 800
screen_height = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("system")
clock = pygame.time.Clock()
FPS = 60 

font = pygame.font.Font(None, 36)

calculator_img = pygame.image.load("data/calculator.png")
calendar_img = pygame.image.load("data/calendar.png")
clock_img = pygame.image.load("data/clock.png")
document_img = pygame.image.load("data/document.png")
folder_img = pygame.image.load("data/folder.png")
paint_img = pygame.image.load("data/paint.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if paint_img.get_rect(topleft=(150, 50)).collidepoint(mouse_pos):
                subprocess.Popen(['python', 'paint.py'])
            elif calculator_img.get_rect(topleft = (50, 50)).collidepoint(mouse_pos):
                subprocess.Popen(['python', 'calculator.py'])
    screen.fill(BLUE)


    calculator_rect = pygame.Rect(50, 50, calculator_img.get_width(),
                                  calculator_img.get_height())
    screen.blit(calculator_img, calculator_rect)


    calendar_rect = pygame.Rect(50, 150, calendar_img.get_width(),
                                calendar_img.get_height())
    screen.blit(calendar_img, calendar_rect)


    clock_rect = pygame.Rect(50, 250, clock_img.get_width(),
                             clock_img.get_height())
    screen.blit(clock_img, clock_rect)


    document_rect = pygame.Rect(50, 350, document_img.get_width(),
                                document_img.get_height())
    screen.blit(document_img, document_rect)


    folder_rect = pygame.Rect(50, 450, folder_img.get_width(),
                              folder_img.get_height())
    screen.blit(folder_img, folder_rect)


    paint_rect = pygame.Rect(150, 50, paint_img.get_width(),
                             paint_img.get_height())
    screen.blit(paint_img, paint_rect)

    pygame.display.update()
    clock.tick(FPS)
