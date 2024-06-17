import pygame
import sys
import subprocess
import os

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
settings_img = pygame.image.load("data/settings.png")
text_img = pygame.image.load("data/text.png")

texts_folder = "texts"
if not os.path.exists(texts_folder):
    os.makedirs(texts_folder)

def draw_icon(image, x, y):
    screen.blit(image, (x, y))
    return pygame.Rect(x, y, image.get_width(), image.get_height())

def list_text_files(folder):
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

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
            elif clock_img.get_rect(topleft = (50, 250)).collidepoint(mouse_pos):
                subprocess.Popen(['python', 'clock.py'])
            elif calendar_img.get_rect(topleft = (50, 150)).collidepoint(mouse_pos):
                subprocess.Popen(["python", "calendar_app.py"])
            elif document_img.get_rect(topleft = (50, 350)).collidepoint(mouse_pos):
                subprocess.Popen(["python", "document.py"])
            for idx, text_file in enumerate(list_text_files(texts_folder)):
                file_rect = draw_icon(text_img, 300, 50 + idx * 100)
                if file_rect.collidepoint(mouse_pos):
                    subprocess.Popen(["python", "document.py"])

    screen.fill(BLUE)

    draw_icon(calculator_img, 50, 50)
    draw_icon(calendar_img, 50, 150)
    draw_icon(clock_img, 50, 250)
    draw_icon(document_img, 50, 350)
    draw_icon(paint_img, 150, 50)
    draw_icon(folder_img, 50, 450)
    draw_icon(settings_img, 150, 150)

    for idx, text_file in enumerate(list_text_files(texts_folder)):
        draw_icon(text_img, 250, 50 + idx * 100)

    pygame.display.update()
    clock.tick(FPS)
