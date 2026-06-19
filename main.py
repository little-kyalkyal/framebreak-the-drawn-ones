import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Framebreak - The Drawn Ones")
clock = pygame.time.Clock()

### background
background_image = pygame.image.load("images/me_computer.png").convert()
background_image = pygame.transform.scale(background_image, (1280, 720))

### character
crimson = pygame.image.load("images/Crimson_Sovereign.png").convert_alpha()
crimson = pygame.transform.scale(crimson, (100, 100))

crimson_pos = pygame.Vector2(500, 585)

# Jump variables
velocity_y = 0
gravity = 900
jump_power = -500
on_ground = True

running = True

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Horizontal movement
    if keys[pygame.K_a]:
        crimson_pos.x -= 300 * dt

    if keys[pygame.K_d]:
        crimson_pos.x += 300 * dt

    # Jump
    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = jump_power
        on_ground = False

    # Apply gravity
    velocity_y += gravity * dt
    crimson_pos.y += velocity_y * dt

    # Ground collision
    if crimson_pos.y >= 585:
        crimson_pos.y = 585
        velocity_y = 0
        on_ground = True

    if crimson_pos.x >= 1280 - crimson.get_width():
        crimson_pos.x = 1280 - crimson.get_width()
    if crimson_pos.x <= 0:
        crimson_pos.x = 0

 
    screen.blit(background_image, (0, 0))
    
     ### platform
    pygame.draw.rect(screen, "white", (50, 595, 100, 30))

    screen.blit(crimson, crimson_pos)

    pygame.display.flip()

pygame.quit()