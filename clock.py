import pygame
import sys
import datetime
import time

pygame.init()


screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clock")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)


font = pygame.font.Font(None, 36)


def draw_button(text, x, y):
    pygame.draw.rect(screen, GRAY, (x, y, 200, 50))
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + 100, y + 25))
    screen.blit(text_surface, text_rect)


def show_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    text_surface = font.render("Current time: " + current_time, True, BLACK)
    screen.blit(text_surface, (50, 150))


def stopwatch():
    start_time = datetime.datetime.now()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

        screen.fill(WHITE)
        elapsed_time = datetime.datetime.now() - start_time
        text_surface = font.render(f"Elapsed time: {str(elapsed_time)[:-7]}", True, BLACK)
        screen.blit(text_surface, (50, 150))
        pygame.display.update()


def timer(duration):
    end_time = datetime.datetime.now() + datetime.timedelta(seconds=duration)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        time_left = end_time - datetime.datetime.now()
        if time_left.total_seconds() <= 0:
            text_surface = font.render("Time's up!", True, BLACK)
            screen.blit(text_surface, (150, 150))
            pygame.display.update()
            time.sleep(2)
            return
        else:
            text_surface = font.render(f"Time left: {str(time_left)[:-7]}", True, BLACK)
            screen.blit(text_surface, (50, 150))
            pygame.display.update()

def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 100 <= x <= 300:
                    if 50 <= y <= 100:
                        show_time_menu()
                    elif 120 <= y <= 170:
                        stopwatch()
                    elif 190 <= y <= 240:
                        duration = 10  
                        timer(duration)
                    elif 260 <= y <= 310:
                        running = False

        screen.fill(WHITE)
        draw_button("Show Time", 100, 50)
        draw_button("Stopwatch", 100, 120)
        draw_button("Timer (10s)", 100, 190)
        draw_button("Exit", 100, 260)
        pygame.display.update()

def show_time_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running = False

        screen.fill(WHITE)
        show_time()
        pygame.display.update()

main_menu()
pygame.quit()
sys.exit()
