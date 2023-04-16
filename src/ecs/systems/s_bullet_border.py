

import pygame
import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_bullet import CTagBullet


def system_bullet_bordering(world:esper.World, screen:pygame.Surface, bullet_count: int) -> int:
    screen_rect = screen.get_rect()
    components = world.get_components(CTransform, CSurface, CTagBullet)

    c_t:CTransform
    c_s:CSurface
    for bullet_entity, (c_t, c_s, c_b) in components:
        cuad_rect = c_s.surf.get_rect(topleft=c_t.pos)
        if cuad_rect.left < 0 or cuad_rect.right > screen_rect.width:
            world.delete_entity(bullet_entity)
            bullet_count -= 1

        if cuad_rect.top < 0 or cuad_rect.bottom > screen_rect.height:
            world.delete_entity(bullet_entity)
            bullet_count -= 1
            
    return bullet_count