import pygame
import os
import random
from settings import *
from map import walls_collision
from Guns import Gun


def load_image(name, colorkey=-1):
    fullname = os.path.join('data', *name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit('main.py')
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((5, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Monster(pygame.sprite.Sprite):
    def __init__(self, *groups, lvl, pos, monster_type, weapon=None, collisions):
        super().__init__(*groups)

        imr = [load_image(('sprites', 'monsters', monster_type['name'], 'R', f'{i}.png')) for i in
               range(int(monster_type['R']))]
        iml = [load_image(('sprites', 'monsters', monster_type['name'], 'L', f'{i}.png')) for i in
               range(int(monster_type['L']))]
        imf = [load_image(('sprites', 'monsters', monster_type['name'], 'F', f'{i}.png')) for i in
               range(int(monster_type['F']))]
        imd = load_image(('sprites', 'monsters', monster_type['name'], 'D', 'dead.png'))

        # animation
        self.animation = {}
        for step, anim in enumerate(imr[:]):
            self.animation['r_' + str(step)] = \
                pygame.transform.scale(anim,
                                       (anim.get_width() * 150 // TILE, anim.get_height() * 150 // TILE))
        for step, anim in enumerate(iml[:]):
            self.animation['l_' + str(step)] = \
                pygame.transform.scale(anim,
                                       (anim.get_width() * 150 // TILE, anim.get_height() * 150 // TILE))
        for step, anim in enumerate(imf[:]):
            self.animation['f_' + str(step)] = \
                pygame.transform.scale(anim,
                                       (anim.get_width() * 150 // TILE, anim.get_height() * 150 // TILE))
        self.animation['d'] = pygame.transform.scale(imd,
                                       (imd.get_width() * 150 // TILE, imd.get_height() * 150 // TILE))

        self.anim_step = 0
        self.anim_turn = 'r_'
        self.max_steps = len(imr) // 2 * player_speed

        # rect and im
        self.image = pygame.transform.scale(imr[0],
                                            (imr[0].get_width() * 150 // TILE, imr[0].get_height() * 150 // TILE))

        self.x, self.y = pos
        self.rect = pygame.rect.Rect(self.x, self.y, self.image.get_width(), self.image.get_height() // 2)
        self.rect.center = pos
        self.w_rect = pygame.rect.Rect(self.x, self.y, self.image.get_width(), self.image.get_height() // 2)
        self.w_rect.center = pos
        walls_collision.append(self.w_rect)
        self.angle = 45
        self.set_lives(lvl)

        self.weapon = Gun(weapon[0], weapon[1], groups[0], self)
        self.fire = False
        self.settings = {'lvl': lvl,
                         'type': monster_type}

    @property
    def pos(self):
        return self.x, self.y

    @property
    def turn(self):
        return 'monster'

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
        self.w_rect.center = self.x, self.y

    def do_animation(self):
        if self.is_live:
            if self.fire and self.weapon.can_fire():
                if self.anim_step // 15 == self.settings['type']['F']:
                    self.anim_step = 0
                    self.stop_fire()
                    self.do_fire()
                self.image = self.animation['f_' + str(self.anim_step // 15)]
            else:
                if self.anim_step // 10 == self.settings['type'][self.anim_turn[0].upper()]:
                    self.anim_step = 0
                self.image = self.animation[self.anim_turn + str(self.anim_step // 10)]
        else:
            self.image = self.animation['d']

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def start_fire(self):
        self.fire = True

    def stop_fire(self):
        self.fire = False

    def do_fire(self):
        self.weapon.fire()

    def hit(self, *args, **kwarks):
        if args[0] == 'player':
            self.lives -= args[1]
            if not self.is_live:
                self.dead()
            return True
        return False

    def update(self):
        self.movement()

    @property
    def is_live(self):
        if self.lives > 0:
            return True
        return False

    def dead(self):
        self.weapon.dead()

    def set_lives(self, lvl):
        pass


class Virus(Monster):
    def set_lives(self, lvl):
        self.lives = 7 + (lvl * 0.5)
        self.m_lives = self.lives

    def movement(self):
        if self.is_live:
            dx = 0
            dy = 0

            x, y = HALF_WIDTH - self.rect.x, HALF_HEIGHT - self.rect.y
            if abs(x) > 250:
                if x > 0:
                    dx += enemie_speed
                else:
                    dx -= enemie_speed
            elif abs(x) < 100 and abs(y) < 100:
                if x > 0:
                    dx -= enemie_speed / 2
                else:
                    dx += enemie_speed / 2

            if abs(y) > 250:
                if y > 0:
                    dy += enemie_speed
                else:
                    dy -= enemie_speed
            elif abs(x) < 100 and abs(y) < 100:
                if y > 0:
                    dy -= enemie_speed / 2
                else:
                    dy += enemie_speed / 2

            if x < 600 and y < 600:
                self.fire = True
            else:
                self.fire = False

            self.is_empty(dx, dy)

            self.w_rect.center = self.x, self.y

            self.anim_step += 1

            self.do_animation()

            if self.rect.x <= HALF_WIDTH:
                self.anim_turn = 'l_'
            else:
                self.anim_turn = 'r_'

            x2, y2 = HALF_WIDTH, HALF_HEIGHT
            x1, y1 = self.rect.x, self.rect.y
            h = y2 - y1
            w = x2 - x1
            t = math.atan2(h, w)
            self.angle = t
        else:
            self.do_animation()

    @property
    def bullet_name(self):
        return 'virus.png'
