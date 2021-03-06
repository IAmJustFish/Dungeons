import pygame
import math
from settings import *
from map import walls_collision
from Guns import Gun


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups, imr, iml, weapon, all_sprites, player_pos, collisions):
        super().__init__(*groups)

        self.fire = False
        self.x, self.y = player_pos
        self.angle = player_angle
        self.lives = player_lives
        self.m_lives = player_lives

        # animation
        self.animation = {}
        for step, anim in enumerate(imr[:]):
            self.animation['r_' + str(step)] = \
                pygame.transform.scale(anim,
                                       (anim.get_width() * 80 // TILE, anim.get_height() * 80 // TILE))
        for step, anim in enumerate(iml[:]):
            self.animation['l_' + str(step)] = \
                pygame.transform.scale(anim,
                                       (anim.get_width() * 80 // TILE, anim.get_height() * 80 // TILE))

        self.anim_step = 0
        self.anim_turn = 'r_'
        self.max_steps = len(imr) // 2 * player_speed

        # rect and im
        self.image = pygame.transform.scale(imr[0],
                                            (imr[0].get_width() * 80 // TILE, imr[0].get_height() * 80 // TILE))
        self.rect = pygame.rect.Rect(self.x, self.y, self.image.get_width(), self.image.get_height() // 2)
        self.rect.center = player_pos

        # rect for world collision
        self.w_rect = pygame.rect.Rect(self.x, self.y, self.image.get_width(), self.image.get_height() // 2)
        self.w_rect.center = player_pos

        walls_collision.append(self.w_rect)

        self.all_sprites = all_sprites
        self.weapon = Gun(weapon[0], weapon[1], all_sprites, player=self)

    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def bullet_name(self):
        return 'bullet.png'

    @property
    def turn(self):
        return 'player'

    def is_empty(self, dx, dy):
        next_rect = self.w_rect.move(dx, dy)
        hit_indexes = next_rect.collidelistall(walls_collision)

        if len(hit_indexes) > 1:
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = walls_collision[hit_index]
                if hit_rect != self.w_rect:
                    if dx > 0:
                        delta_x += next_rect.right - hit_rect.left
                    else:
                        delta_x += hit_rect.right - next_rect.left
                    if dy > 0:
                        delta_y += next_rect.bottom - hit_rect.top
                    else:
                        delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.rect.x += dx
        self.rect.y += dy
        self.x += dx
        self.y += dy

    def movement(self):
        keys = pygame.key.get_pressed()
        step = self.anim_step
        if keys[pygame.K_w]:
            self.is_empty(0, -player_speed)
            step += 1
        if keys[pygame.K_s]:
            self.is_empty(0, player_speed)
            step += 1
        if keys[pygame.K_a]:
            self.is_empty(-player_speed, 0)
            step += 1
        if keys[pygame.K_d]:
            self.is_empty(player_speed, 0)
            step += 1

        self.w_rect.center = self.x, self.y

        if step != self.anim_step:
            self.anim_step = self.anim_step + 1
        else:
            self.anim_step = 0

        self.do_animation()
        
        if pygame.mouse.get_focused():
            x2, y2 = pygame.mouse.get_pos()
            x1, y1 = self.rect.x, self.rect.y
            h = y2 - y1
            w = x2 - x1
            t = math.atan2(h, w)
            self.angle = t
            if x2 <= HALF_WIDTH:
                self.anim_turn = 'l_'
            else:
                self.anim_turn = 'r_'

    def do_animation(self):
        self.image = self.animation[self.anim_turn + str(self.anim_step // 10)]
        if self.anim_step // 10 == self.max_steps:
            self.anim_step = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def start_fire(self):
        self.fire = True

    def stop_fire(self):
        self.fire = False

    def hit(self, *args, **kwarks):
        if args[0] == 'monster':
            self.lives -= args[1]
            if not self.is_live:
                self.dead()
            return True
        return False

    def dead(self):
        pass

    @property
    def is_live(self):
        if self.lives > 0:
            return True
        return False

    def update(self):
        self.movement()
        if self.fire:
            self.weapon.fire()

    def get_weapon(self, weapon):
        self.weapon = weapon
