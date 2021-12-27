from game.gameobject import GameObject
from move.coordinate import Coordinate


class CollisionManager:
    def __init__(self) -> None:
        pass

    def are_colliding(self, object1: GameObject, object2: GameObject):
        return self.obj1_in_obj2(object1, object2) or self.obj1_in_obj2(object2, object1)

    def obj1_in_obj2(self, object1: GameObject, object2: GameObject) -> bool:
        """OK listen up boils an ghouls, here's how we're doing collision. It's currently two days before Christmas and I'm hyped up on python so lets go

           Since all objects are squares, simple check each corner of square 1 and see if it's coordinate is bounded by the square of object 2
           If it's ever bounded, you know you have a collision

           Repeate this process for all 4 corners. Viola. This should handle every case *EXCEPT* when the squares are *EXACTLY* one on top of each other.
           In that case, according to this algorithm, no collision will be detected. But what are the chances of that happening right?.....?
        """

        # self.debug(object1, object2)

        # xone = object2.get_left_up_corner().x 
        # xtwo = object1.get_right_down_corner().x 
        # xthree = object2.get_right_up_corner().x 
        
        # yone = object2.get_left_up_corner().y 
        # ytwo = object1.get_right_down_corner().y 
        # ythree = object2.get_left_down_corner().y

        # check if bottom right corner of object 1 is in the square of object 2
        if  object2.get_left_up_corner().x <= object1.get_right_down_corner().x <= object2.get_right_up_corner().x and \
            object2.get_left_up_corner().y <= object1.get_right_down_corner().y <= object2.get_left_down_corner().y:
            return True

        # check if bottom left corner of object 1 is in the square of object 2
        if  object2.get_left_up_corner().x <= object1.get_left_down_corner().x <= object2.get_right_up_corner().x and \
            object2.get_left_up_corner().y <= object1.get_left_down_corner().y <= object2.get_right_down_corner().y:
            return True

        one = object2.get_left_down_corner().x <= object1.get_right_up_corner().x <= object2.get_right_down_corner().x
        two = object2.get_left_up_corner().y <= object1.get_right_up_corner().y <= object2.get_left_down_corner().y

        # check if top right corner of object 1 is in the square of object 2
        if  object2.get_left_down_corner().x <= object1.get_right_up_corner().x <= object2.get_right_down_corner().x and \
            object2.get_left_up_corner().y <= object1.get_right_up_corner().y <= object2.get_left_down_corner().y:
            return True

        one = object2.get_left_down_corner().x <= object1.get_right_up_corner().x <= object2.get_right_down_corner().x
        two = object2.get_left_up_corner().y <= object1.get_right_up_corner().y <= object2.get_left_down_corner().y

        # check if top left corner of object 1 is in the square of object 2
        if  object2.get_left_down_corner().x <= object1.get_left_up_corner().x <= object2.get_right_down_corner().x and \
            object2.get_right_up_corner().y <= object1.get_left_up_corner().y <= object2.get_right_down_corner().y:
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