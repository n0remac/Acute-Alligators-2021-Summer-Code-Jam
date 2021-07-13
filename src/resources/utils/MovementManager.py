from ..entities.AbstractDungeonEntity import AbstractDungeonEntity
from ..Level import Level


def move_entity(entity: AbstractDungeonEntity, new_position: (int, int), level: Level) -> None:
    """A helper class to move reset the board symbol when entities move"""
    level.board[entity.y][entity.x] = entity.ground_symbol
    entity.x = new_position[0]
    entity.y = new_position[1]
    # level.board[entity.y][entity.x] = entity.symbol
