import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Notepad")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

font = pygame.font.Font(None, 36)

text_area = pygame.Rect(50, 50, 700, 500)
text_color = BLACK
bg_color = WHITE
cursor_color = BLACK
cursor_width = 2
cursor_pos = (60, 60)
cursor_visible = True
cursor_timer = 0
cursor_blink_interval = 500  

text = ""
filename = "note.txt"

def draw_text(surface, text, font, color, rect, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    line_spacing = -2

    font_height = font.size("Tg")[1]

    while text:
        i = 1
        if y + font_height > rect.bottom:
            break

        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += font_height + line_spacing

        text = text[i:]

    return text

def save_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)

def load_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

text = load_file(filename)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                text += "\n"
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pygame.K_TAB:
                text += "    "  
            else:
                text += event.unicode

            if event.mod & pygame.KMOD_CTRL and event.key == pygame.K_s:
                save_file(filename, text)

    # Draw text area
    pygame.draw.rect(screen, GRAY, text_area)
    draw_text(screen, text, font, text_color, text_area.inflate(-10, -10))

    # Manage cursor blinking
    current_time = pygame.time.get_ticks()
    if current_time - cursor_timer > cursor_blink_interval:
        cursor_timer = current_time
        cursor_visible = not cursor_visible

    if cursor_visible:
        cursor_pos_x = text_area.left + font.size(text[:cursor_pos[1]])[0]
        cursor_pos_y = text_area.top + cursor_pos[0] + 10  
        pygame.draw.line(screen, cursor_color, (cursor_pos_x, cursor_pos_y),
                         (cursor_pos_x, cursor_pos_y + font.size(text[cursor_pos[1]:])[1]), cursor_width)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
