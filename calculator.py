import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

screen_width = 400
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Calculator")

font = pygame.font.Font(None, 36)

buttons = [
    {"label": "7", "pos": (10, 150)}, {"label": "8", "pos": (110, 150)}, {"label": "9", "pos": (210, 150)}, {"label": "/", "pos": (310, 150)},
    {"label": "4", "pos": (10, 250)}, {"label": "5", "pos": (110, 250)}, {"label": "6", "pos": (210, 250)}, {"label": "*", "pos": (310, 250)},
    {"label": "1", "pos": (10, 350)}, {"label": "2", "pos": (110, 350)}, {"label": "3", "pos": (210, 350)}, {"label": "-", "pos": (310, 350)},
    {"label": "0", "pos": (10, 450)}, {"label": ".", "pos": (110, 450)}, {"label": "=", "pos": (210, 450)}, {"label": "+", "pos": (310, 450)},
    {"label": "C", "pos": (10, 550)}, {"label": "(", "pos": (110, 550)}, {"label": ")", "pos": (210, 550)}, {"label": "^", "pos": (310, 550)},
]

display_rect = pygame.Rect(10, 10, 380, 120)

current_input = ""

def draw_buttons():
    for button in buttons:
        pygame.draw.rect(screen, GRAY, (button["pos"][0], button["pos"][1], 90, 90))
        text_surface = font.render(button["label"], True, BLACK)
        text_rect = text_surface.get_rect(center=(button["pos"][0] + 45, button["pos"][1] + 45))
        screen.blit(text_surface, text_rect)

def draw_display():
    pygame.draw.rect(screen, DARK_GRAY, display_rect)
    text_surface = font.render(current_input, True, WHITE)
    text_rect = text_surface.get_rect(right=display_rect.right - 10, centery=display_rect.centery)
    screen.blit(text_surface, text_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button["pos"][0] <= pos[0] <= button["pos"][0] + 90 and button["pos"][1] <= pos[1] <= button["pos"][1] + 90:
                    if button["label"] == "C":
                        current_input = ""  
                    elif button["label"] == "=":
                        try:
                            current_input = str(eval(current_input))
                        except:
                            current_input = "Error"
                    else:
                        current_input += button["label"]
                    break

    screen.fill(BLACK)
    draw_display()
    draw_buttons()
    pygame.display.update()

pygame.quit()
sys.exit()
