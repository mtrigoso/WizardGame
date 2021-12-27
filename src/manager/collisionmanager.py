from game.gameobject import GameObject
from move.coordinate import Coordinate


class CollisionManager:
    def __init__(self) -> None:
        pass

    def are_colliding(self, object1: GameObject, object2: GameObject, lightning_bolt=False):
        """check if object1 has a corner in object2 or object2 has a corner in object1
        """
        obj1_in_obj2 = self.obj1_in_obj2(object1, object2, lightning_bolt)
        obj2_in_obj1 = self.obj1_in_obj2(object2, object1, lightning_bolt)
        return obj1_in_obj2 or obj2_in_obj1

    def obj1_in_obj2(self, object1: GameObject, object2: GameObject, lightning_bolt=False) -> bool:
        """OK listen up boils an ghouls, here's how we're doing collision. It's currently two days before Christmas and I'm hyped up on python so lets go

           Since all objects are squares, simple check each corner of square 1 and see if it's coordinate is bounded by the square of object 2
           If it's ever bounded, you know you have a collision

           Repeate this process for all 4 corners. Viola. This should handle every case *EXCEPT* when the squares are *EXACTLY* one on top of each other.
           In that case, according to this algorithm, no collision will be detected. But what are the chances of that happening right?.....?
        """

        # check if bottom right corner of object 1 is in the square of object 2
        if  object2.get_left_up_corner().x <= object1.get_right_down_corner().x <= object2.get_right_up_corner().x and \
            object2.get_left_up_corner().y <= object1.get_right_down_corner().y <= object2.get_left_down_corner().y:
            if lightning_bolt:
                print(f"bottom right corner of {type(object1)} is in the square of {type(object2)}")
                self.debug(object1, object2)
            return True

        # check if bottom left corner of object 1 is in the square of object 2
        if  object2.get_left_up_corner().x <= object1.get_left_down_corner().x <= object2.get_right_up_corner().x and \
            object2.get_left_up_corner().y <= object1.get_left_down_corner().y <= object2.get_right_down_corner().y:
            if lightning_bolt:
                print(f"bottom left corner of {type(object1)} is in the square of {type(object2)}")
                self.debug(object1, object2)
            return True

        # check if top right corner of object 1 is in the square of object 2
        if  object2.get_left_down_corner().x <= object1.get_right_up_corner().x <= object2.get_right_down_corner().x and \
            object2.get_left_up_corner().y <= object1.get_right_up_corner().y <= object2.get_left_down_corner().y:
            if lightning_bolt:
                print(f"top right corner of {type(object1)} is in the square of {type(object2)}")
                self.debug(object1, object2)
            return True

        # check if top left corner of object 1 is in the square of object 2
        if  object2.get_left_down_corner().x <= object1.get_left_up_corner().x <= object2.get_right_down_corner().x and \
            object2.get_right_up_corner().y <= object1.get_left_up_corner().y <= object2.get_right_down_corner().y:
            if lightning_bolt:
                print(f"top left corner of {type(object1)} is in the square of {type(object2)}")
                self.debug(object1, object2)
            return True

        return False

    def debug(self, object1: GameObject, object2: GameObject):
        object1_type = type(object1)
        object2_type = type(object2)

        obj1_top_left_x = object1.get_left_up_corner().x
        obj1_top_left_y= object1.get_left_up_corner().y

        obj1_top_right_x = object1.get_right_up_corner().x
        obj1_top_right_y = object1.get_right_up_corner().y

        obj1_bottom_left_x = object1.get_left_down_corner().x
        obj1_bottom_left_y = object1.get_left_down_corner().y

        obj1_bottom_right_x = object1.get_right_down_corner().x
        obj1_bottom_right_y = object1.get_right_down_corner().y

        obj2_top_left_x = object2.get_left_up_corner().x
        obj2_top_left_y= object2.get_left_up_corner().y

        obj2_top_right_x = object2.get_right_up_corner().x
        obj2_top_right_y = object2.get_right_up_corner().y

        obj2_bottom_left_x = object2.get_left_down_corner().x
        obj2_bottom_left_y = object2.get_left_down_corner().y

        obj2_bottom_right_x = object2.get_right_down_corner().x
        obj2_bottom_right_y = object2.get_right_down_corner().y

        foo = 10