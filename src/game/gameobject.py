from typing import overload
from game.action.gameaction import GameAction
from game.gamestate import GameState
from move.movementaction import MovementAction
from move.coordinate import Coordinate
from scene import Scene


class GameObject(object):
    def __init__(self) -> None:
        super().__init__()
        self._object_width: int = 16
        self._object_height: int = 16
        self.x = 0
        self.y = 0
        self._speed = 1
        self._bitmap_x = 64
        self._bitmap_y = 0
        self._killable = False
        self._to_be_killed = False
        self._can_kill = False
        self._die_on_stalled = False
        self.image_num = 0
        self._transparent_color = 0

    @overload
    def get_left_up_corner(self) -> Coordinate:
        pass

    @overload
    def get_left_down_corner(self) -> Coordinate:
        pass

    @overload
    def get_right_down_corner(self) -> Coordinate:
        pass

    @overload
    def get_right_up_corner(self) -> Coordinate:
        pass

    @overload 
    def get_action(self, game_state: GameState, scene: Scene) -> GameAction:
        pass

    @overload 
    def apply_action(self, action: MovementAction):
        pass

    @overload 
    def bitmap_x(self) -> int:
        pass

    @overload 
    def bitmap_y(self) -> int:
        pass

    @overload 
    def get_obj_horiz_tilemap_size(self) -> int:
        pass

    @overload 
    def get_obj_vert_tilemap_size(self) -> int:
        pass

    def removable(self) -> bool:
        return self._killable
    
    def to_be_removed(self) -> bool:
        return self._to_be_killed

    def set_to_be_removed(self) -> bool:
        self._to_be_killed = True
    
    def can_kill(self) -> bool:
        return self._can_kill

    def die_on_stalled(self) -> bool:
        return self._die_on_stalled
    
    def get_transparent_color(self) -> int:
        return self._transparent_color