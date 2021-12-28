from game.gameobject import GameObject
from game.projectile.lightningbolt import LightningBolt
from move.coordinate import Coordinate
from user.player import Player


class CollisionManager:
    def __init__(self) -> None:
        pass

    def are_colliding(self, object1: GameObject, object2: GameObject, debug=True):
        """check if object1 has a corner in object2 or object2 has a corner in object1
        """
        if debug:
            self.debug(object1, object2)
        return self.is_overlap(object1.get_left_up_corner(), object1.get_right_down_corner(), object2.get_left_up_corner(), object2.get_right_down_corner())

    # lovingly stolen from: https://www.geeksforgeeks.org/find-two-rectangles-overlap/
    def is_overlap(self, rect1_top_left_corner: Coordinate, rect1_bottom_right_corner: Coordinate, rect2_top_left_corner: Coordinate, rect2_bottom_right_corner: Coordinate):
        if (rect1_top_left_corner.x == rect1_bottom_right_corner.x or rect1_top_left_corner.y == rect1_bottom_right_corner.y or rect2_top_left_corner.x == rect2_bottom_right_corner.x or rect2_top_left_corner.y == rect2_bottom_right_corner.y):
            # the line cannot have positive overlap
            return False

        # If one rectangle is on left side of other
        if(rect1_top_left_corner.x >= rect2_bottom_right_corner.x or rect2_top_left_corner.x >= rect1_bottom_right_corner.x):
            return False

        # If one rectangle is above other
        if(rect1_bottom_right_corner.y <= rect2_top_left_corner.y or rect2_bottom_right_corner.y <= rect1_top_left_corner.y):
            return False

        return True

    def debug(self, object1: GameObject, object2: GameObject):
        object1_type = type(object1)
        object2_type = type(object2)

        obj1_top_left_x = object1.get_left_up_corner().x
        obj1_top_left_y = object1.get_left_up_corner().y

        obj1_top_right_x = object1.get_right_up_corner().x
        obj1_top_right_y = object1.get_right_up_corner().y

        obj1_bottom_left_x = object1.get_left_down_corner().x
        obj1_bottom_left_y = object1.get_left_down_corner().y

        obj1_bottom_right_x = object1.get_right_down_corner().x
        obj1_bottom_right_y = object1.get_right_down_corner().y

        obj2_top_left_x = object2.get_left_up_corner().x
        obj2_top_left_y = object2.get_left_up_corner().y

        obj2_top_right_x = object2.get_right_up_corner().x
        obj2_top_right_y = object2.get_right_up_corner().y

        obj2_bottom_left_x = object2.get_left_down_corner().x
        obj2_bottom_left_y = object2.get_left_down_corner().y

        obj2_bottom_right_x = object2.get_right_down_corner().x
        obj2_bottom_right_y = object2.get_right_down_corner().y

        foo = 10
