from battle.spellaction import SpellAction
from game.action.gameaction import GameAction
from game.gameobject import GameObject
from game.projectile.lightningbolt import LightningBolt
from move.movevector import MoveVector


class ProjectileAction(SpellAction):
    def __init__(self, projectile_type: type, direction: MoveVector, x: int, y: int) -> None:
        super().__init__()
        self.projectile_type = projectile_type
        self.move_vector = direction
        self.x = x
        self.y = y

    def build_projectile_object(self) -> GameObject:
        if self.projectile_type == LightningBolt:
            return LightningBolt(self.move_vector, self.x, self.y)
        # TODO: have something other than a lightningbolt be the default - adding this here just so mypy stops complaining
        return LightningBolt(self.move_vector, self.x, self.y)
