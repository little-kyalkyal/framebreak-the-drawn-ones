import pygame

from const import BLUE_BACKGROUND


class Player:

    def __init__(self, x, y, animations):

        self.pos = pygame.Vector2(x, y)

        self.animations = animations

        self.state = "idle"
        self.direction = "left"

        self.frame_index = 0
        self.animation_timer = 0

        self.animation_speed = 0.1

        self.velocity_y = 0

        self.gravity = 900
        self.jump_power = -500

        self.on_ground = True



    def update_state(self, moving):

        old_state = self.state

        if not self.on_ground:
            self.state = "jumping"

        elif moving:
            self.state = "walking"

        else:
            self.state = "idle"

        if old_state != self.state:
            self.frame_index = 0



    def animate(self, dt):
        self.animation_timer += dt

        if self.animation_timer >= self.animation_speed:

            self.animation_timer = 0

            self.frame_index += 1

            frames = self.animations[self.state]

            if self.frame_index >= len(frames):
                self.frame_index = 0

    
    def move(self, dt, keys):

        moving = False

        if keys[pygame.K_a]:

            self.pos.x -= 300 * dt
            self.direction = "left"
            moving = True

        if keys[pygame.K_d]:

            self.pos.x += 300 * dt
            self.direction = "right"
            moving = True

        if keys[pygame.K_SPACE] and self.on_ground:

            self.velocity_y = self.jump_power
            self.on_ground = False

        self.velocity_y += self.gravity * dt

        self.pos.y += self.velocity_y * dt

        if self.pos.y >= 400:

            self.pos.y = 400

            self.velocity_y = 0

            self.on_ground = True

        self.update_state(moving)



    def draw(self, screen):

        frame = self.animations[self.state][
            self.frame_index
        ]

        if self.direction == "right":

            frame = pygame.transform.flip(
                frame,
                True,
                False
            )

        frame.set_colorkey(BLUE_BACKGROUND)

        screen.blit(frame, self.pos)