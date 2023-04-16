import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_bullet import CTagBullet
from src.ecs.components.tags.c_tag_enemy import CTagEnemy

def system_collision_enemy(world: esper.World, player_entity: int, level_cfg: dict, bullet_count: int):
    
    componentsE = world.get_components(CSurface, CTransform, CTagEnemy)
    componentsB = world.get_components(CSurface, CTransform, CTagBullet)
    pl_t = world.component_for_entity(player_entity, CTransform)
    pl_s = world.component_for_entity(player_entity, CSurface)
    pl_rect = pl_s.surf.get_rect(topleft = pl_t.pos)
    
    for enemy_entity, (ce_s, ce_t, _) in componentsE:
        ene_rect = ce_s.surf.get_rect(topleft = ce_t.pos)
        if ene_rect.colliderect(pl_rect):
            world.delete_entity(enemy_entity)
            pl_t.pos.x = level_cfg["player_spawn"]["position"]["x"] - pl_s.surf.get_width() / 2
            pl_t.pos.y = level_cfg["player_spawn"]["position"]["y"] - pl_s.surf.get_height() / 2
        for bullet, (cb_s, cb_t, _) in componentsB:
            bul_rect = cb_s.surf.get_rect(topleft = cb_t.pos)
            if ene_rect.colliderect(bul_rect):
                world.delete_entity(enemy_entity)
                world.delete_entity(bullet)
                bullet_count -= 1
                
    return bullet_count