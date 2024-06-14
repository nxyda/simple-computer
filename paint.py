import pygame
import sys
import math

#TEST

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

selected_color = BLACK
colors = [RED, GREEN, BLUE, WHITE, BLACK]
brush_sizes = [5, 10, 20, 30]
selected_brush_size = brush_sizes[0]
shapes = ['circle', 'square', 'triangle']
selected_shape = shapes[0]

button_size = 30
button_padding = 5
return_button_rect = pygame.Rect(WIDTH - 100, HEIGHT - 50, 80, 30)  

def draw_color_buttons():
    x = WIDTH - button_size - button_padding
    y = button_padding
    for color in colors:
        pygame.draw.rect(win, color, (x, y, button_size, button_size))
        y += button_size + button_padding

def draw_brush_size_indicators():
    x = button_padding
    y = HEIGHT - button_size - button_padding
    for size in brush_sizes:
        pygame.draw.rect(win, BLACK, (x, y, button_size, button_size))
        if size == selected_brush_size:
            pygame.draw.rect(win, WHITE, (x + 2, y + 2, button_size - 4, button_size - 4))
        x += button_size + button_padding

def draw_shape_indicators():
    x = button_padding
    y = button_padding
    for shape in shapes:
        pygame.draw.rect(win, BLACK, (x, y, button_size, button_size))
        if shape == selected_shape:
            pygame.draw.rect(win, WHITE, (x + 2, y + 2, button_size - 4, button_size - 4))
        x += button_size + button_padding

def draw_circle(pos, radius):
    pygame.draw.circle(win, selected_color, pos, radius)

def draw_square(pos, size):
    rect = pygame.Rect(pos[0] - size / 2, pos[1] - size / 2, size, size)
    pygame.draw.rect(win, selected_color, rect)

def draw_triangle(pos, size):
    half_height = size * math.sqrt(3) / 2 / 2
    points = [(pos[0], pos[1] - half_height),
              (pos[0] - size / 2, pos[1] + half_height),
              (pos[0] + size / 2, pos[1] + half_height)]
    pygame.draw.polygon(win, selected_color, points)

def draw_return_button():
    pygame.draw.rect(win, BLACK, return_button_rect)
    font = pygame.font.Font(None, 24)
    text = font.render('Return', True, WHITE)
    text_rect = text.get_rect(center=return_button_rect.center)
    win.blit(text, text_rect)

win.fill(WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if return_button_rect.collidepoint(event.pos):
                running = False
            elif WIDTH - button_size - button_padding <= event.pos[0] <= WIDTH - button_padding:
                y = button_padding
                for color in colors:
                    if y <= event.pos[1] <= y + button_size:
                        selected_color = color
                        break
                    y += button_size + button_padding
            elif HEIGHT - button_size - button_padding <= event.pos[1] <= HEIGHT - button_padding:
                x = button_padding
                for size in brush_sizes:
                    if x <= event.pos[0] <= x + button_size:
                        selected_brush_size = size
                        break
                    x += button_size + button_padding
            else:
                if selected_shape == 'circle':
                    draw_circle(event.pos, selected_brush_size)
                elif selected_shape == 'square':
                    draw_square(event.pos, selected_brush_size)
                elif selected_shape == 'triangle':
                    draw_triangle(event.pos, selected_brush_size)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:  
                if selected_shape == 'circle':
                    draw_circle(event.pos, selected_brush_size)
                elif selected_shape == 'square':
                    draw_square(event.pos, selected_brush_size)
                elif selected_shape == 'triangle':
                    draw_triangle(event.pos, selected_brush_size)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                selected_shape = 'circle'
            elif event.key == pygame.K_s:
                selected_shape = 'square'
            elif event.key == pygame.K_t:
                selected_shape = 'triangle'

    draw_color_buttons()
    draw_brush_size_indicators()
    draw_shape_indicators()
    draw_return_button()
    pygame.display.update()

pygame.quit()
sys.exit()
