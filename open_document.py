import pygame
import sys
import os

pygame.init()

if len(sys.argv) != 2:
    print("Usage: python open_document.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

if not os.path.isfile(filename):
    print(f"File '{filename}' does not exist.")
    sys.exit(1)

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Open Document")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)

with open(filename, 'r') as file:
    content = file.read()

lines = content.split('\n')
y_offset = 50

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, BLACK)
        screen.blit(text_surface, (50, y_offset + i * 40))

    pygame.display.flip()

pygame.quit()
sys.exit()
