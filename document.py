import pygame
import sys
import os

pygame.init()

# Ustawienia ekranu
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Notepad")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Czcionka
font = pygame.font.Font(None, 36)

# Prostokąt dla tekstu
text_area = pygame.Rect(50, 50, 700, 500)
text_color = BLACK
bg_color = WHITE
cursor_color = BLACK
cursor_width = 2
cursor_pos = (60, 60)
cursor_visible = True
cursor_blink_interval = 500

# Tekst
text = ""

# Folder do zapisywania plików
texts_folder = "texts"
if not os.path.exists(texts_folder):
    os.makedirs(texts_folder)
filename = os.path.join(texts_folder, "note.txt")

# Pole tekstowe na nazwę pliku
filename_input_rect = pygame.Rect(200, 10, 200, 30)
filename_input_color = DARK_GRAY
filename_input_text = ""

# Funkcja do rysowania tekstu
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
    try:
        with open(filename, "w") as file:
            file.write(text)
        print(f"File saved as {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")


def load_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""
    except IOError as e:
        print(f"Error loading file: {e}")
        return ""

def clear_text():
    global text
    text = ""

def save_as_dialog():
    global text, filename

    input_rect = pygame.Rect(100, 200, 600, 50) 
    input_text = ""  

    clock = pygame.time.Clock()
    dialog_active = True

    while dialog_active:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    filename = os.path.join(texts_folder, input_text + ".txt")
                    save_file(filename, text)
                    dialog_active = False
                elif event.key == pygame.K_ESCAPE:
                    dialog_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        pygame.draw.rect(screen, GRAY, input_rect, 2)

        draw_text(screen, input_text, font, BLACK, input_rect)

        pygame.display.flip()
        clock.tick(30)



def notepad():
    global text, cursor_visible, cursor_timer, filename_input_text, filename_input_active
    text = load_file(filename)
    cursor_timer = pygame.time.get_ticks()
    filename_input_text = ""  
    filename_input_active = False  

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if clear_button_rect.collidepoint(mouse_pos):
                    clear_text()
                elif save_as_button_rect.collidepoint(mouse_pos):
                    save_as_dialog()

                elif filename_input_rect.collidepoint(mouse_pos):
                    filename_input_active = True
                else:
                    filename_input_active = False

                if filename_input_active:
                    filename_input_text += event.unicode

        pygame.draw.rect(screen, GRAY, text_area)
        draw_text(screen, text, font, text_color, text_area.inflate(-10, -10))

        current_time = pygame.time.get_ticks()
        if current_time - cursor_timer > cursor_blink_interval:
            cursor_timer = current_time
            cursor_visible = not cursor_visible

        if cursor_visible:
            cursor_pos_x = text_area.left + font.size(text[:cursor_pos[1]])[0]
            cursor_pos_y = text_area.top + cursor_pos[0] + 10
            pygame.draw.line(screen, cursor_color, (cursor_pos_x, cursor_pos_y),
                             (cursor_pos_x, cursor_pos_y + font.size(text[cursor_pos[1]:])[1]), cursor_width)

        # Przycisk Wyczyść
        clear_button_rect = pygame.Rect(50, 10, 100, 30)
        pygame.draw.rect(screen, DARK_GRAY, clear_button_rect)
        draw_text(screen, "clear", font, WHITE, clear_button_rect, True)

        # Przycisk Zapisz jako
        save_as_button_rect = pygame.Rect(600, 10, 150, 30)
        pygame.draw.rect(screen, DARK_GRAY, save_as_button_rect)
        draw_text(screen, "save as", font, WHITE, save_as_button_rect, True)

        # Pole tekstowe na nazwę pliku
        pygame.draw.rect(screen, WHITE, filename_input_rect)
        draw_text(screen, filename_input_text, font, BLACK, filename_input_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Uruchomienie notatnika
notepad()


