from battle.spellaction import SpellAction
from game.action.gameaction import GameAction
from game.gameobject import GameObject
from game.projectile.lightningbolt import LightningBolt
from move.movevector import MoveVector


class ProjectileAction(SpellAction):
    def __init__(self, projectile_type: type, direction: MoveVector) -> None:
        super().__init__()
        self.projectile_type = projectile_type
        self.move_vector = direction

    def build_projectile_object(self) -> GameObject:
        if self.projectile_type == LightningBolt:
            return LightningBolt(self.move_vector)
