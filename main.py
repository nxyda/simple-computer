import pygame
import sys
import random
import string
import datetime
import time
import calendar as cal_module
import os

pygame.init()
screen_width = 800
screen_height = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("system")
clock = pygame.time.Clock()

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

    screen.fill(WHITE)

    # Draw calculator button
    calculator_rect = pygame.Rect(50, 50, calculator_img.get_width(), calculator_img.get_height())
    screen.blit(calculator_img, calculator_rect)

    # Draw calendar button
    calendar_rect = pygame.Rect(50, 150, calendar_img.get_width(), calendar_img.get_height())
    screen.blit(calendar_img, calendar_rect)

    # Draw clock button
    clock_rect = pygame.Rect(50, 250, clock_img.get_width(), clock_img.get_height())
    screen.blit(clock_img, clock_rect)

    # Draw document button
    document_rect = pygame.Rect(50, 350, document_img.get_width(), document_img.get_height())
    screen.blit(document_img, document_rect)

    # Draw folder button
    folder_rect = pygame.Rect(50, 450, folder_img.get_width(), folder_img.
                              
  pygame.display.update()
  clock.tick(FPS)