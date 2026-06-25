import pygame

from const import *
from player import Player
from spritesheet import SpriteSheet

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Framebreak - The Drawn Ones")
clock = pygame.time.Clock()

### background
background_image = pygame.image.load(BACKGROUND_IMAGE).convert()
background_image = pygame.transform.scale(background_image, (1280, 720))

# sprites
spritesheet = SpriteSheet(PRINCESS_IMG)

animations = {
    "idle": [],
    "jumping": [],
    "walking": []
}

# sprite extraction
## idle
animations["idle"].append(spritesheet.get_image(
        0,
        0,
        CHARACTER_FRAME_WIDTH,
        CHARACTER_FRAME_HEIGHT,
        scale=3
    ))

animations["jumping"].append(spritesheet.get_image(
        0,
        CHARACTER_FRAME_HEIGHT + BORDER_THICKNESS,
        CHARACTER_FRAME_WIDTH,
        CHARACTER_FRAME_HEIGHT,
        scale=3
    ))


for col in range(12):

    frame = spritesheet.get_image(
        (col * BORDER_THICKNESS) + (col * CHARACTER_FRAME_WIDTH),
        (CHARACTER_FRAME_HEIGHT + BORDER_THICKNESS) * 2,
        CHARACTER_FRAME_WIDTH,
        CHARACTER_FRAME_HEIGHT,
        scale=3
    )

    animations["walking"].append(frame)
    
running = True

player = Player(
    400,
    400,
    animations
)

while running:

    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.move(dt, keys)
    player.animate(0.02)

    screen.blit(background_image, (0, 0))

    player.draw(screen)

    pygame.display.flip()

pygame.quit()