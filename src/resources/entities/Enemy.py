from random import choice

from .AbstractDungeonEntity import AbstractDungeonEntity


class Enemy(AbstractDungeonEntity):
    """Enemy entity and hostile to players"""

    def __init__(self, aggro_radius: int, file: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aggro_radius = aggro_radius
        self.entity_type = "enemy"
        self.target: dict = {}
        self.file = f"{file.name!r}"
        self.player_detected = False
        # damage enemy attacked player for
        self.damage_attacked_for = 0

    def mill(self) -> None:
        """Random enemy movement"""
        movement_axis = choice(['x', 'y'])
        direction_axis = (1, -1)
        movement = choice(direction_axis)  # up or down (1, -1), left or right (1, -1)
        if movement_axis == 'x':  # movement will be on the x axis
            self.new_positions["x"] += movement
        if movement_axis == 'y':  # movement will be on the y axis
            self.new_positions["y"] += movement

    def follow(self, testing: bool = False) -> None:
        """Enemy movement function to chase player"""
        if not testing:
            x = self.target['x']
            y = self.target['y']
            move_x = 0
            move_y = 0

            # find direction
            if abs(x - self.x) > abs(y - self.y):
                if self.x < x:
                    move_x = 1
                if self.x > x:
                    move_x = -1
            elif abs(x - self.x) < abs(y - self.y):
                if self.y < y:
                    move_y = 1
                if self.y > y:
                    move_y = -1

            # move in that direction
            if x - self.aggro_radius <= self.x + self.new_positions["x"] <= x + self.aggro_radius:
                self.new_positions["x"] = move_x
            else:
                self.new_positions["x"] = 0

            if y - self.aggro_radius <= self.y + self.new_positions["y"] <= y + self.aggro_radius:
                self.new_positions["y"] = move_y
            else:
                self.new_positions["y"] = 0

    def is_in_radius(self, x: int, y: int) -> bool:
        """Check if player is in 'aggro' radius"""
        radius = self.aggro_radius
        if (y - radius <= self.y <= y + radius) and \
                (x - radius <= self.x <= x + radius):
            self.symbol.stylize("bold red")
            self.target = {'x': x, 'y': y}
            self.player_detected = True
            return True
        else:
            self.symbol.stylize("bold white")
            self.player_detected = False
            return False

    def hit(self) -> int:
        """Returns amount of damage that the player should be hit for"""
        # possible_hits = {"critical": randint(7, 10), "normal": randint(4, 6), "weak": randint(1, 3)}
        # hit_damage = possible_hits.get(choice(["critical", "normal", "weak"]), '')
        hit_damage = 5
        self.damage_attacked_for = hit_damage
        return hit_damage
