import pygame
import sys
import calendar as cal_module
from datetime import datetime

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Calendar")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

font = pygame.font.Font(None, 36)

events = {}

def draw_text(text, x, y, center=False):
    text_surface = font.render(text, True, BLACK)
    if center:
        text_rect = text_surface.get_rect(center=(x, y))
    else:
        text_rect = text_surface.get_rect(topleft=(x, y))
    screen.blit(text_surface, text_rect)

def draw_button(text, x, y, w=200, h=50, color=GRAY):
    pygame.draw.rect(screen, color, (x, y, w, h))
    draw_text(text, x + w//2, y + h//2, center=True)

def input_text(prompt, x, y):
    user_text = ''
    input_box = pygame.Rect(x, y, 200, 50)
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return user_text
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        screen.fill(WHITE)
        draw_text(prompt, x, y - 30)
        txt_surface = font.render(user_text, True, BLACK)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, DARK_GRAY, input_box, 2)
        pygame.display.flip()

def show_calendar():
    current_date = datetime.now()
    year = current_date.year
    month = current_date.month

    def draw_calendar(year, month):
        cal = cal_module.Calendar()
        month_days = cal.monthdayscalendar(year, month)
        screen.fill(WHITE)
        month_year_text = f"{cal_module.month_name[month]} {year}"
        draw_text(month_year_text, screen_width // 2, 50, center=True)
        days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days_of_week):
            draw_text(day, 50 + i * 100, 100, center=True)
        y_offset = 150
        for week in month_days:
            for i, day in enumerate(week):
                if day != 0:
                    draw_text(str(day), 50 + i * 100, y_offset, center=True)
            y_offset += 50
        draw_button("Previous", 50, 500, w=150, h=50)
        draw_button("Next", 600, 500, w=150, h=50)
        draw_button("Back", 325, 500, w=150, h=50)
        pygame.display.flip()

    running = True
    while running:
        draw_calendar(year, month)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 <= x <= 200 and 500 <= y <= 550:
                    month -= 1
                    if month == 0:
                        month = 12
                        year -= 1
                elif 600 <= x <= 750 and 500 <= y <= 550:
                    month += 1
                    if month == 13:
                        month = 1
                        year += 1
                elif 325 <= x <= 475 and 500 <= y <= 550:
                    running = False

def add_event():
    year = int(input_text("Enter year:", 300, 200))
    month = int(input_text("Enter month:", 300, 250))
    day = int(input_text("Enter day:", 300, 300))
    event = input_text("Enter event:", 300, 350)
    if year not in events:
        events[year] = {}
    if month not in events[year]:
        events[year][month] = {}
    if day not in events[year][month]:
        events[year][month][day] = []
    events[year][month][day].append(event)

def remove_event():
    year = int(input_text("Enter year:", 300, 200))
    month = int(input_text("Enter month:", 300, 250))
    day = int(input_text("Enter day:", 300, 300))
    if year in events and month in events[year] and day in events[year][month]:
        event = input_text("Enter event to remove:", 300, 350)
        if event in events[year][month][day]:
            events[year][month][day].remove(event)
            if not events[year][month][day]:
                del events[year][month][day]
            if not events[year][month]:
                del events[year][month]
            if not events[year]:
                del events[year]

def show_events():
    year = int(input_text("Enter year:", 300, 200))
    month = int(input_text("Enter month:", 300, 250))
    if year in events and month in events[year]:
        running = True
        event_texts = []
        for day in events[year][month]:
            for event in events[year][month][day]:
                event_texts.append(f"{day}: {event}")
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= event.pos[0] <= 500 and 500 <= event.pos[1] <= 550:
                        running = False

            screen.fill(WHITE)
            for i, event_text in enumerate(event_texts):
                draw_text(event_text, 50, 50 + i * 30)
            draw_button("Back", 300, 500)
            pygame.display.flip()
    else:
        print("No events in this month.")

def calendar():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 300 <= x <= 500:
                    if 150 <= y <= 200:
                        show_calendar()
                    elif 220 <= y <= 270:
                        add_event()
                    elif 290 <= y <= 340:
                        remove_event()
                    elif 360 <= y <= 410:
                        show_events()
                    elif 430 <= y <= 480:
                        running = False

        screen.fill(WHITE)
        draw_button("Show Calendar", 300, 150)
        draw_button("Add Event", 300, 220)
        draw_button("Remove Event", 300, 290)
        draw_button("Show Events", 300, 360)
        draw_button("Exit", 300, 430)
        pygame.display.flip()

calendar()
pygame.quit()
sys.exit()
