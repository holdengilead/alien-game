import pygame

RIGHT = 1073741903
LEFT = 1073741904
DOWN = 1073741905
UP = 1073741906


class Ship:
    def __init__(self, ai_game) -> None:
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/ship_m96.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_direction = {
            RIGHT: False,
            LEFT: False,
            DOWN: False,
            UP: False,
        }

    def update(self):
        if self.moving_direction[RIGHT] and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_direction[LEFT] and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_direction[UP] and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_direction[DOWN] and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.x, self.rect.y = self.x, self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
