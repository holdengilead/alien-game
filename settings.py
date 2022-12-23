class Settings:
    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (230, 230, 230)
        self.ship_speed = 5

        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 13
        self.alien_speed = 5.0
        self.fleet_drop_speed = 2
        self.fleet_direction = 1  # 1, to the right, -1, to the left.

        self.ship_limit = 3
