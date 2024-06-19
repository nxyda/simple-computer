import pygame
import sys
import os


pygame.init()


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
MUSIC_FOLDER = "music"  


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 36)


def get_music_files(folder):
    return [f for f in os.listdir(folder) if f.endswith('.mp3') or f.endswith('.wav')]

music_files = get_music_files(MUSIC_FOLDER)
current_song = None
playing = False
paused = False

def draw_text(surface, text, position, color=BLACK):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

def draw_music_files(surface, files, selected_index):
    for idx, file in enumerate(files):
        color = BLUE if idx == selected_index else BLACK
        draw_text(surface, file, (50, 170 + idx * 40), color)

def load_and_play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    return file_path.split("/")[-1]


clock = pygame.time.Clock()
selected_index = 0

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_index = (selected_index - 1) % len(music_files)
            elif event.key == pygame.K_DOWN:
                selected_index = (selected_index + 1) % len(music_files)
            elif event.key == pygame.K_RETURN:
                current_song = load_and_play_music(os.path.join(MUSIC_FOLDER, music_files[selected_index]))
                playing = True
                paused = False
            elif event.key == pygame.K_SPACE and playing:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_s and playing:
                pygame.mixer.music.stop()
                playing = False
                paused = False


    draw_text(screen, "Use UP/DOWN to select", (50, 10))
    draw_text(screen, "ENTER to play", (50, 50))
    draw_text(screen, "SPACE to pause", (50, 90))
    draw_text(screen, "S to stop", (50, 130))

    draw_music_files(screen, music_files, selected_index)


    if current_song:
        draw_text(screen, f"Now Playing: {current_song}", (50, 350), RED)

    pygame.display.flip()
    clock.tick(30)
