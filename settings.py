import pygame
import sys

pygame.init()

screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Settings")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)

def save_settings(background_image_index):
    with open("settings.txt", "w") as file:
        file.write(str(background_image_index))

background_images = [
    "backgrounds/background_1.png",
    "backgrounds/background_2.png",
    "backgrounds/background_3.png",
    "backgrounds/background_4.png",
    "backgrounds/background_5.png",
    "backgrounds/background_6.png"
]

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for idx, image_path in enumerate(background_images):
                button_rect = pygame.Rect(50, 50 + idx * 40, 300, 30)
                if button_rect.collidepoint(mouse_pos):
                    save_settings(idx)
                    print(f"Background set to {image_path}")

    for idx, image_path in enumerate(background_images):
        button_rect = pygame.Rect(50, 50 + idx * 40, 300, 30)
        pygame.draw.rect(screen, BLACK, button_rect)
        button_text = font.render(f"Background {idx + 1}", True, WHITE)
        screen.blit(button_text, (60, 55 + idx * 40))

    pygame.display.flip()
