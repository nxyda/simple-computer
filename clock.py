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

def draw_button(text, x, y, width=100, height=50):
    pygame.draw.rect(screen, GRAY, (x, y, width, height))
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

def show_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    text_surface = font.render("Current time: " + current_time, True, BLACK)
    screen.blit(text_surface, (50, 150))

def stopwatch():
    start_time = datetime.datetime.now()
    running = True
    paused = False
    elapsed_time = datetime.timedelta()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 100 <= x <= 300 and 400 <= y <= 450:
                    return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if paused:
                        start_time = datetime.datetime.now() - elapsed_time
                    paused = not paused

        if not paused:
            elapsed_time = datetime.datetime.now() - start_time

        screen.fill(WHITE)
        text_surface = font.render(f"Elapsed time: {str(elapsed_time)[:-7]}", True, BLACK)
        screen.blit(text_surface, (50, 150))
        draw_button("Back", 100, 400, 200, 50)
        pygame.display.update()

def timer(duration):
    end_time = datetime.datetime.now() + datetime.timedelta(seconds=duration)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 100 <= x <= 300 and 400 <= y <= 450:
                    return

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
        draw_button("Back", 100, 400, 200, 50)
        pygame.display.update()

def set_timer():
    running = True
    hours, minutes, seconds = 0, 0, 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 <= x <= 150 and 300 <= y <= 350:
                    hours += 1
                elif 250 <= x <= 350 and 300 <= y <= 350:
                    if hours > 0:
                        hours -= 1
                elif 50 <= x <= 150 and 350 <= y <= 400:
                    minutes += 1
                elif 250 <= x <= 350 and 350 <= y <= 400:
                    if minutes > 0:
                        minutes -= 1
                elif 50 <= x <= 150 and 400 <= y <= 450:
                    seconds += 10
                elif 250 <= x <= 350 and 400 <= y <= 450:
                    if seconds >= 10:
                        seconds -= 10
                elif 150 <= x <= 250 and 500 <= y <= 550:
                    return hours * 3600 + minutes * 60 + seconds
                elif 100 <= x <= 300 and 550 <= y <= 600:
                    return None

        screen.fill(WHITE)
        text_surface = font.render(f"Set timer: {hours}h {minutes}m {seconds}s", True, BLACK)
        screen.blit(text_surface, (50, 150))
        draw_button("+1h", 50, 300)
        draw_button("-1h", 250, 300)
        draw_button("+1m", 50, 350)
        draw_button("-1m", 250, 350)
        draw_button("+10s", 50, 400)
        draw_button("-10s", 250, 400)
        draw_button("Start", 150, 500, 100, 50)
        draw_button("Back", 100, 550, 200, 50)
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
                        duration = set_timer()
                        if duration is not None:
                            timer(duration)
                    elif 260 <= y <= 310:
                        running = False

        screen.fill(WHITE)
        draw_button("Show Time", 100, 50, 200, 50)
        draw_button("Stopwatch", 100, 120, 200, 50)
        draw_button("Timer", 100, 190, 200, 50)
        draw_button("Exit", 100, 260, 200, 50)
        pygame.display.update()

def show_time_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 100 <= x <= 300 and 400 <= y <= 450:
                    running = False

        screen.fill(WHITE)
        show_time()
        draw_button("Back", 100, 400, 200, 50)
        pygame.display.update()

main_menu()
pygame.quit()
sys.exit()
