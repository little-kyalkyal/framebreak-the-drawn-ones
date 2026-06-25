import pygame

from options.const import *
from models.character import Character
from models.spritesheet import SpriteSheet

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
        scale=CHARACTER_SCALE
    ))

animations["jumping"].append(spritesheet.get_image(
        0,
        CHARACTER_FRAME_HEIGHT + BORDER_THICKNESS,
        CHARACTER_FRAME_WIDTH,
        CHARACTER_FRAME_HEIGHT,
        scale=CHARACTER_SCALE
    ))


for col in range(12):

    frame = spritesheet.get_image(
        (col * BORDER_THICKNESS) + (col * CHARACTER_FRAME_WIDTH),
        (CHARACTER_FRAME_HEIGHT + BORDER_THICKNESS) * 2,
        CHARACTER_FRAME_WIDTH,
        CHARACTER_FRAME_HEIGHT,
        scale=CHARACTER_SCALE
    )

    animations["walking"].append(frame)
    
running = True

player = Character(
    400,
    GROUND_Y,
    animations
)

print(GROUND_Y)

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