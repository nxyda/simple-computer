import pygame
import sys
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
DARK_GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Minesweeper")

cell_size = 40
grid_width = 10
grid_height = 10
num_mines = 10

font = pygame.font.SysFont(None, 24)

def create_grid():
    return [[0 for _ in range(grid_width)] for _ in range(grid_height)]

def place_mines(grid, initial_click):
    mines = random.sample(range(grid_width * grid_height), num_mines)
    initial_x, initial_y = initial_click

    for mine in mines:
        x = mine % grid_width
        y = mine // grid_width
        if (x, y) == (initial_x, initial_y):
            continue

        grid[y][x] = -1

    for y in range(grid_height):
        for x in range(grid_width):
            if grid[y][x] == -1:
                continue
            for i in range(max(0, y-1), min(grid_height, y+2)):
                for j in range(max(0, x-1), min(grid_width, x+2)):
                    if grid[i][j] == -1:
                        grid[y][x] += 1

    return grid

def draw_grid(grid, revealed, flags):
    for y in range(grid_height):
        for x in range(grid_width):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if revealed[y][x]:
                if grid[y][x] == -1:
                    pygame.draw.rect(screen, RED, rect)
                    pygame.draw.line(screen, BLACK, rect.topleft, rect.bottomright, 2)
                    pygame.draw.line(screen, BLACK, rect.topright, rect.bottomleft, 2)
                else:
                    pygame.draw.rect(screen, WHITE, rect)
                    if grid[y][x] > 0:
                        text = font.render(str(grid[y][x]), True, BLACK)
                        screen.blit(text, rect.topleft)
            else:
                pygame.draw.rect(screen, GRAY, rect)
                if flags[y][x]:
                    pygame.draw.rect(screen, GREEN, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

def reveal_cell(grid, revealed, y, x):
    if revealed[y][x]:
        return
    revealed[y][x] = True
    if grid[y][x] == 0:
        for i in range(max(0, y-1), min(grid_height, y+2)):
            for j in range(max(0, x-1), min(grid_width, x+2)):
                if not revealed[i][j]:
                    reveal_cell(grid, revealed, i, j)

def check_win(revealed, flags):
    for y in range(grid_height):
        for x in range(grid_width):
            if not revealed[y][x] and not flags[y][x]:
                return False
    return True

def first_click_reveal(grid, revealed, initial_x, initial_y):
    reveal_queue = [(initial_y, initial_x)]
    while reveal_queue:
        y, x = reveal_queue.pop()
        if revealed[y][x]:
            continue
        revealed[y][x] = True
        if grid[y][x] == 0:
            for i in range(max(0, y-1), min(grid_height, y+2)):
                for j in range(max(0, x-1), min(grid_width, x+2)):
                    if not revealed[i][j]:
                        reveal_queue.append((i, j))

def game_loop():
    grid = create_grid()
    revealed = [[False for _ in range(grid_width)] for _ in range(grid_height)]
    flags = [[False for _ in range(grid_width)] for _ in range(grid_height)]
    game_over = False
    won = False
    first_click = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                x //= cell_size
                y //= cell_size
                if event.button == 1:
                    if first_click:
                        grid = place_mines(grid, (x, y))
                        first_click_reveal(grid, revealed, x, y)
                        first_click = False
                    if grid[y][x] == -1:
                        game_over = True
                    else:
                        reveal_cell(grid, revealed, y, x)
                elif event.button == 3:
                    flags[y][x] = not flags[y][x]

        screen.fill(BLACK)
        draw_grid(grid, revealed, flags)

        if check_win(revealed, flags):
            won = True
            game_over = True

        if game_over:
            text = "You Win!" if won else "Game Over"
            text = font.render(text, True, BLUE if won else RED)
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))

        pygame.display.flip()

game_loop()
