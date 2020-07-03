import pygame
import math
import random
from PIL import Image, ImageDraw

pygame.init()

display_width = 1000
display_height = 1000

brown = (153, 76, 0)
dark_red = (175, 0, 0)
dark_green = (0, 150, 0)
light_green = (0, 255, 0)
dark_blue = (0, 76, 153)
middle_blue = (0, 128, 255)
light_blue = (102, 178, 255)
yellow = (255, 255, 51)
gray = (128, 128, 128)
black = (0, 0, 0)
light_black = (50, 50, 50)
white = (255, 255, 255)
grey = (127, 127, 127)
bright_red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
dirt_color = (205, 133, 63)
crosshair_width = 70
crosshair_height = 70
pixel_guy_width = 128
pixel_guy_height = 128
gun_zombie_width = 80
gun_zombie_height = 80
pixel_pellet_width = 15
pixel_pellet_height = 15
pixel_bullet_width = 35
pixel_bullet_height = 14
wall_width = 50
wall_height = 50
guy_square_dimension = 181
pixel_heart_width = 45
pixel_heart_height = 45
melee_swoosh_width = 100
melee_swoosh_height = 50
coin_width = 25
coin_height = 25
big_coin_width = 40
big_coin_height = 40
big_pellet_width = 100
big_pellet_height = 100
item_width = 135
item_height = 135

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dungeon_Explorer")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

pixel_guy_north = pygame.image.load("pixel_guy_thin_gun.png").convert_alpha()
pixel_guy_north = pygame.transform.scale(pixel_guy_north, (pixel_guy_width, pixel_guy_height))
tiny_pixel_guy = pygame.transform.scale(pixel_guy_north, (26, 26))
pixel_guy_east = pygame.transform.rotate(pixel_guy_north, -90)
pixel_crosshair = pygame.image.load("pixil-frame-0.png").convert_alpha()
pixel_crosshair = pygame.transform.scale(pixel_crosshair, (crosshair_width, crosshair_height))
pixel_bullet = pygame.image.load("pixel_bullet.png").convert_alpha()
big_pixel_bullet = pygame.transform.scale(pixel_bullet, (pixel_bullet_width * 5, pixel_bullet_height * 5))
pixel_bullet = pygame.transform.scale(pixel_bullet, (pixel_bullet_width, pixel_bullet_height))
big_pixel_bullet_highlighted = pygame.image.load("pixel_bullet_highlighted.png").convert_alpha()
big_pixel_bullet_highlighted = pygame.transform.scale(big_pixel_bullet_highlighted, (pixel_bullet_width * 5, pixel_bullet_height * 5))
blue_pixel_bullet = pygame.image.load("blue_pixel_bullet.png").convert_alpha()
big_blue_pixel_bullet = pygame.transform.scale(blue_pixel_bullet, (pixel_bullet_width * 5, pixel_bullet_height * 5))
big_blue_pixel_bullet_highlighted = pygame.image.load("blue_pixel_bullet_highlighted.png").convert_alpha()
big_blue_pixel_bullet_highlighted = pygame.transform.scale(big_blue_pixel_bullet_highlighted, (pixel_bullet_width * 5, pixel_bullet_height * 5))
blue_pixel_bullet = pygame.transform.scale(blue_pixel_bullet, (pixel_bullet_width, pixel_bullet_height))
stone_wall = pygame.image.load("stone_wall.png").convert_alpha()
stone_wall = pygame.transform.scale(stone_wall, (wall_width, wall_height))
gun_zombie_image = pygame.image.load("pixel_zombie_with_guns.png").convert_alpha()
gun_zombie_image = pygame.transform.scale(gun_zombie_image, (gun_zombie_width, gun_zombie_height))
gun_zombie_red_image = pygame.image.load("pixel_zombie_red.png").convert_alpha()
gun_zombie_red_image = pygame.transform.scale(gun_zombie_red_image, (gun_zombie_width, gun_zombie_height))
gun_zombie_frozen_image = pygame.image.load("pixel_frozem_zombie.png").convert_alpha()
gun_zombie_frozen_image = pygame.transform.scale(gun_zombie_frozen_image, (gun_zombie_width, gun_zombie_height))
red_pixel_pellet = pygame.image.load("red_pixel_pellet.png").convert_alpha()
red_pixel_pellet = pygame.transform.scale(red_pixel_pellet, (pixel_pellet_width, pixel_pellet_height))
heart = pygame.image.load("full_pixel_heart.png").convert_alpha()
heart = pygame.transform.scale(heart, (pixel_heart_width, pixel_heart_height))
half_heart = pygame.image.load("half_pixel_heart.png").convert_alpha()
half_heart = pygame.transform.scale(half_heart, (pixel_heart_width, pixel_heart_height))
pixel_guy_swinging = pygame.image.load("pixel_guy_360_swing.png").convert_alpha()
pixel_guy_swinging = pygame.transform.scale(pixel_guy_swinging, (pixel_guy_width, pixel_guy_height))
pixel_guy_swinging = pygame.transform.rotate(pixel_guy_swinging, -90)
pixel_question_mark = pygame.image.load("pixel_question_mark.png").convert_alpha()
pixel_question_mark = pygame.transform.scale(pixel_question_mark, (150, 150))
pixel_boss_logo = pygame.image.load("pixel_boss_logo.png").convert_alpha()
pixel_boss_logo = pygame.transform.scale(pixel_boss_logo, (150, 150))
pixel_shop_logo = pygame.image.load("pixel_shop_logo.png").convert_alpha()
pixel_shop_logo = pygame.transform.scale(pixel_shop_logo, (150, 150))
pixel_coin = pygame.image.load("pixel_coin.png").convert_alpha()
pixel_coin = pygame.transform.scale(pixel_coin, (coin_width, coin_height))
bigger_coin = pygame.transform.scale(pixel_coin, (big_coin_width, big_coin_height))
pixel_gun_side = pygame.image.load("pixel_gun_side_fixed.png").convert_alpha()
pixel_gun_side = pygame.transform.scale(pixel_gun_side, (1000, 400))
pixel_red_dot_sight = pygame.image.load("pixel_red_dot_sight.png").convert_alpha()
pixel_red_dot_sight = pygame.transform.scale(pixel_red_dot_sight, (1000, 400))
pixel_red_dot_sight_highlighted = pygame.image.load("red_dot_sight_highlighted.png").convert_alpha()
pixel_red_dot_sight_highlighted = pygame.transform.scale(pixel_red_dot_sight_highlighted, (1000, 400))
blank_image = pygame.image.load("blank_image.png").convert_alpha()
pixel_extended_magazine = pygame.image.load("extended_magazine.png").convert_alpha()
pixel_extended_magazine = pygame.transform.scale(pixel_extended_magazine, (1000, 400))
pixel_extended_magazine_highlighted = pygame.image.load("extended_magazine_highlighted.png").convert_alpha()
pixel_extended_magazine_highlighted = pygame.transform.scale(pixel_extended_magazine_highlighted, (1000, 400))
pixel_magazine_highlighted = pygame.image.load("pixel_magazine_highlighted.png").convert_alpha()
pixel_magazine_highlighted = pygame.transform.scale(pixel_magazine_highlighted, (1000, 400))
pixel_default_barrel_extension = pygame.image.load("pixel_barrel_extention.png").convert_alpha()
pixel_default_barrel_extension = pygame.transform.scale(pixel_default_barrel_extension, (1000, 400))
pixel_default_barrel_extension_highlighted = pygame.image.load("pixel_barrel_extension_highlighted.png").convert_alpha()
pixel_default_barrel_extension_highlighted = pygame.transform.scale(pixel_default_barrel_extension_highlighted, (1000, 400))
pixel_potion_red = pygame.image.load("pixel_red_potion.png").convert_alpha()
pixel_potion_red = pygame.transform.scale(pixel_potion_red, (item_width, item_height))
pixel_potion_red_highlighted = pygame.image.load("pixel_potion_red_highlighted.png").convert_alpha()
pixel_potion_red_highlighted = pygame.transform.scale(pixel_potion_red_highlighted, (item_width, item_height))
pixel_potion_yellow = pygame.image.load("pixel_potion_yellow.png").convert_alpha()
pixel_potion_yellow = pygame.transform.scale(pixel_potion_yellow, (item_width, item_height))
pixel_potion_yellow_highlighted = pygame.image.load("pixel_potion_yellow_highlighted.png").convert_alpha()
pixel_potion_yellow_highlighted = pygame.transform.scale(pixel_potion_yellow_highlighted, (item_width, item_height))
pixel_heart_amulet = pygame.image.load("healing_amulet.png").convert_alpha()
pixel_heart_amulet = pygame.transform.scale(pixel_heart_amulet, (item_width, item_height))
pixel_heart_amulet_highlighted = pygame.image.load("healing_amulet_highlighted.png").convert_alpha()
pixel_heart_amulet_highlighted = pygame.transform.scale(pixel_heart_amulet_highlighted, (item_width, item_height))
pixel_arrow_amulet = pygame.image.load("dashing_amulet.png").convert_alpha()
pixel_arrow_amulet = pygame.transform.scale(pixel_arrow_amulet, (item_width, item_height))
pixel_arrow_amulet_highlighted = pygame.image.load("dashing_amulet_highlighted.png").convert_alpha()
pixel_arrow_amulet_highlighted = pygame.transform.scale(pixel_arrow_amulet_highlighted, (item_width, item_height))
pixel_wrench_amulet = pygame.image.load("pixel_wrench_amulet.png").convert_alpha()
pixel_wrench_amulet = pygame.transform.scale(pixel_wrench_amulet, (item_width, item_height))
pixel_wrench_amulet_highlighted = pygame.image.load("pixel_wrench_amulet_highlighted.png").convert_alpha()
pixel_wrench_amulet_highlighted = pygame.transform.scale(pixel_wrench_amulet_highlighted, (item_width, item_height))
pixel_steel_sword = pygame.image.load("pixel_sword.png").convert_alpha()
pixel_steel_sword = pygame.transform.scale(pixel_steel_sword, (item_width, item_height))
pixel_steel_sword_highlighted = pygame.image.load("pixel_sword_highlighted.png").convert_alpha()
pixel_steel_sword_highlighted = pygame.transform.scale(pixel_steel_sword_highlighted, (item_width, item_height))
pixel_ice_sword = pygame.image.load("pixel_ice_sword.png").convert_alpha()
pixel_ice_sword = pygame.transform.scale(pixel_ice_sword, (item_width, item_height))
pixel_ice_sword_highlighted = pygame.image.load("pixel_ice_sword_highlighted.png").convert_alpha()
pixel_ice_sword_highlighted = pygame.transform.scale(pixel_ice_sword_highlighted, (item_width, item_height))
pixel_hammer = pygame.image.load("pixel_hammer.png").convert_alpha()
pixel_hammer = pygame.transform.scale(pixel_hammer, (item_width, item_height))
pixel_hammer_highlighted = pygame.image.load("pixel_hammer_highlighted.png").convert_alpha()
pixel_hammer_highlighted = pygame.transform.scale(pixel_hammer_highlighted, (item_width, item_height))
pixel_melee_fists_north = pygame.image.load("pixel_melee_fists.png").convert_alpha()
pixel_melee_fists_north = pygame.transform.scale(pixel_melee_fists_north, (pixel_guy_width, pixel_guy_height))
pixel_melee_fists = pygame.transform.rotate(pixel_melee_fists_north, -90)
pixel_melee_hammer_north = pygame.image.load("pixel_melee_hammer.png").convert_alpha()
pixel_melee_hammer_north = pygame.transform.scale(pixel_melee_hammer_north, (pixel_guy_width, pixel_guy_height))
pixel_melee_hammer = pygame.transform.rotate(pixel_melee_hammer_north, -90)
pixel_melee_ice_sword_north = pygame.image.load("pixel_melee_ice_sword.png").convert_alpha()
pixel_melee_ice_sword_north = pygame.transform.scale(pixel_melee_ice_sword_north, (pixel_guy_width, pixel_guy_height))
pixel_melee_ice_sword = pygame.transform.rotate(pixel_melee_ice_sword_north, -90)

border_0 = pygame.image.load("border_top_left.png").convert_alpha()
border_0 = pygame.transform.scale(border_0, (display_width, display_height))
border_1 = pygame.image.load("border_top.png").convert_alpha()
border_1 = pygame.transform.scale(border_1, (display_width, display_height))
border_2 = pygame.image.load("border_top_right.png").convert_alpha()
border_2 = pygame.transform.scale(border_2, (display_width, display_height))
border_3 = pygame.image.load("border_left.png").convert_alpha()
border_3 = pygame.transform.scale(border_3, (display_width, display_height))
border_4 = pygame.image.load("border_center.png").convert_alpha()
border_4 = pygame.transform.scale(border_4, (display_width, display_height))
border_5 = pygame.image.load("border_right.png").convert_alpha()
border_5 = pygame.transform.scale(border_5, (display_width, display_height))
border_6 = pygame.image.load("border_bottom_left.png").convert_alpha()
border_6 = pygame.transform.scale(border_6, (display_width, display_height))
border_7 = pygame.image.load("border_bottom.png").convert_alpha()
border_7 = pygame.transform.scale(border_7, (display_width, display_height))
border_8 = pygame.image.load("border_bottom_right.png").convert_alpha()
border_8 = pygame.transform.scale(border_8, (display_width, display_height))
border_list = [border_0, border_1, border_2, border_3, border_4, border_5, border_6, border_7, border_8]


gun_zombie_list_list_x_bottom = [
    [6, 13],
    [6, 13],
    [2, 17],
    [3, 17],
    [3, 16],
    [3, 16],
    [4, 15]
]

gun_zombie_list_list_y_bottom = [
    [1, 1],
    [2, 2],
    [5, 5],
    [1, 1],
    [3, 3],
    [3, 3],
    [4, 4]
]

wall_list_list_x_bottom = [
    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [0, 1, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17, 18, 19, 7, 8, 9, 10, 11, 12],
    [0, 1, 2, 3, 4, 5, 5, 5, 14, 14, 14, 15, 16, 17, 18, 19],
    [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19],
    [3, 4, 5, 6, 6, 6, 6, 13, 13, 13, 13, 14, 15, 16],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [0, 1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19]
]

wall_list_list_y_bottom = [
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0, 10, 10, 10, 10, 10, 10],
    [7, 7, 7, 7, 7, 7, 6, 5, 5, 6, 7, 7, 7, 7, 7, 7],
    [4, 4, 4, 4, 4, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 4, 4, 4, 4, 4],
    [6, 6, 6, 6, 5, 4, 3, 3, 4, 5, 6, 6, 6, 6],
    [7, 7, 7, 7, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 7, 7, 7, 7],
    [3, 4, 5, 6, 7, 6, 5, 4, 4, 5, 6, 7, 6, 5, 4, 3]
]

gun_zombie_list_list_x_top = [
    [13, 6],
    [13, 6],
    [17, 2],
    [16, 2],
    [16, 3],
    [16, 3],
    [15, 4]
]

gun_zombie_list_list_y_top = [
    [18, 18],
    [17, 17],
    [14, 14],
    [18, 18],
    [16, 16],
    [16, 16],
    [15, 15]
]

wall_list_list_x_top = [
     [14, 13, 12, 11, 10, 9, 8, 7, 6, 5],
     [19, 18, 17, 16, 15, 14, 13, 6, 5, 4, 3, 2, 1, 0, 12, 11, 10, 9, 8, 7],
     [19, 18, 17, 16, 15, 14, 14, 14, 5, 5, 5, 4, 3, 2, 1, 0],
     [19, 18, 17, 16, 15, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 4, 3, 2, 1, 0],
     [16, 15, 14, 13, 13, 13, 13, 6, 6, 6, 6, 5, 4, 3],
     [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
     [19, 18, 17, 16, 15, 14, 13, 12, 7, 6, 5, 4, 3, 2, 1, 0]
]

wall_list_list_y_top = [
    [16, 16, 16, 16, 16, 16, 16, 16, 16, 16],
    [19, 18, 17, 16, 15, 14, 13, 13, 14, 15, 16, 17, 18, 19, 9, 9, 9, 9, 9, 9],
    [12, 12, 12, 12, 12, 12, 13, 14, 14, 13, 12, 12, 12, 12, 12, 12],
    [15, 15, 15, 15, 15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15],
    [13, 13, 13, 13, 14, 15, 16, 16, 15, 14, 13, 13, 13, 13],
    [12, 12, 12, 12, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 12, 12, 12, 12],
    [16, 15, 14, 13, 12, 13, 14, 15, 15, 14, 13, 12, 13, 14, 15, 16]

]

gun_zombie_list_list_x_left = [
    [18, 18],
    [17, 17],
    [14, 14],
    [18, 18],
    [16, 16],
    [16, 16],
    [15, 15]
]

gun_zombie_list_list_y_left = [
    [13, 6],
    [13, 6],
    [17, 2],
    [16, 2],
    [16, 3],
    [16, 3],
    [15, 4]

]

wall_list_list_x_left = [
    [16, 16, 16, 16, 16, 16, 16, 16, 16, 16],
    [19, 18, 17, 16, 15, 14, 13, 13, 14, 15, 16, 17, 18, 19, 9, 9, 9, 9, 9, 9],
    [12, 12, 12, 12, 12, 12, 13, 14, 14, 13, 12, 12, 12, 12, 12, 12],
    [15, 15, 15, 15, 15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15],
    [13, 13, 13, 13, 14, 15, 16, 16, 15, 14, 13, 13, 13, 13],
    [12, 12, 12, 12, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 12, 12, 12, 12],
    [16, 15, 14, 13, 12, 13, 14, 15, 15, 14, 13, 12, 13, 14, 15, 16]


]

wall_list_list_y_left = [
    [14, 13, 12, 11, 10, 9, 8, 7, 6, 5],
    [19, 18, 17, 16, 15, 14, 13, 6, 5, 4, 3, 2, 1, 0, 12, 11, 10, 9, 8, 7],
    [19, 18, 17, 16, 15, 14, 14, 14, 5, 5, 5, 4, 3, 2, 1, 0],
    [19, 18, 17, 16, 15, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 4, 3, 2, 1, 0],
    [16, 15, 14, 13, 13, 13, 13, 6, 6, 6, 6, 5, 4, 3],
    [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    [19, 18, 17, 16, 15, 14, 13, 12, 7, 6, 5, 4, 3, 2, 1, 0]

]

gun_zombie_list_list_x_right = [
    [1, 1],
    [2, 2],
    [5, 5],
    [1, 1],
    [3, 3],
    [3, 3],
    [4, 4]
]

gun_zombie_list_list_y_right = [
    [6, 13],
    [6, 13],
    [2, 17],
    [3, 17],
    [3, 16],
    [3, 16],
    [4, 15]
]

wall_list_list_x_right = [
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0, 10, 10, 10, 10, 10, 10],
    [7, 7, 7, 7, 7, 7, 6, 5, 5, 6, 7, 7, 7, 7, 7, 7],
    [4, 4, 4, 4, 4, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 4, 4, 4, 4, 4],
    [6, 6, 6, 6, 5, 4, 3, 3, 4, 5, 6, 6, 6, 6],
    [7, 7, 7, 7, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 7, 7, 7, 7],
    [3, 4, 5, 6, 7, 6, 5, 4, 4, 5, 6, 7, 6, 5, 4, 3]

]

wall_list_list_y_right = [
    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [0, 1, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17, 18, 19, 7, 8, 9, 10, 11, 12],
    [0, 1, 2, 3, 4, 5, 5, 5, 14, 14, 14, 15, 16, 17, 18, 19],
    [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19],
    [3, 4, 5, 6, 6, 6, 6, 13, 13, 13, 13, 14, 15, 16],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [0, 1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19]

]


gun_zombie_dictionary_x = {
    "bottom": gun_zombie_list_list_x_bottom,
    "top": gun_zombie_list_list_x_top,
    "left": gun_zombie_list_list_x_left,
    "right": gun_zombie_list_list_x_right
}

gun_zombie_dictionary_y = {
    "bottom": gun_zombie_list_list_y_bottom,
    "top": gun_zombie_list_list_y_top,
    "left": gun_zombie_list_list_y_left,
    "right": gun_zombie_list_list_y_right
}

wall_dictionary_x = {
    "bottom": wall_list_list_x_bottom,
    "top": wall_list_list_x_top,
    "left": wall_list_list_x_left,
    "right": wall_list_list_x_right
}

wall_dictionary_y = {
    "bottom": wall_list_list_y_bottom,
    "top": wall_list_list_y_top,
    "left": wall_list_list_y_left,
    "right": wall_list_list_y_right
}


def boss_square():
    border_width = 10
    pygame.draw.rect(game_display, bright_red, (400, 400, 200, 200))
    pygame.draw.rect(game_display, black, (400 + border_width, 400 + border_width, 200 - 2 * border_width, 200 - 2 * border_width))
    game_display.blit(pixel_boss_logo, (425, 425))


def shop_square():
    border_width = 10
    pygame.draw.rect(game_display, yellow, (700, 700, 200, 200))
    pygame.draw.rect(game_display, black, (700 + border_width, 700 + border_width, 200 - 2 * border_width, 200 - 2 * border_width))
    game_display.blit(pixel_shop_logo, (725, 725))


def map_square(room, x, y, state):
    if state["room"] == room:
        pygame.draw.rect(game_display, dirt_color, (x, y, 200, 200))
        for i in range(state["num_of_walls"]):
            pygame.draw.rect(game_display, gray, (x + state["wall_list_x"][i] * 10, y + state["wall_list_y"][i] * 10, 10, 10))
        for i in range(state["num_of_gun_zombies"]):
            if state["gun_zombie_exist"][i]:
                pygame.draw.rect(game_display, green, (x + math.floor(state["gun_zombie_x"][i] / 5), y + math.floor(state["gun_zombie_y"][i] / 5), 16, 16))
        game_display.blit(tiny_pixel_guy, (x + math.floor(state["pixel_guy_x"] / 5), y + math.floor(state["pixel_guy_y"] / 5)))

    elif get_room_entered(room, state):
        pygame.draw.rect(game_display, green, (x, y, 200, 200))
        for i in range(len(wall_dictionary_x[get_room_rotation(room, state)][get_room_type(room, state)])):
            pygame.draw.rect(game_display, gray, (x + wall_dictionary_x[get_room_rotation(room, state)][get_room_type(room, state)][i] * 10, y + wall_dictionary_y[get_room_rotation(room, state)][get_room_type(room, state)][i] * 10, 10, 10))
    else:
        pygame.draw.rect(game_display, bright_red, (x, y, 200, 200))
        game_display.blit(pixel_question_mark, (x + 25, y + 25))


def map_screen(state):
    map_screening = True
    map_cooldown = 5
    while map_screening:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                state["map_cooldown"] = 10
                if event.key == pygame.K_m and map_cooldown == 0:
                    map_screening = False
        if map_cooldown > 0:
            map_cooldown -= 1
        game_display.fill(black)
        map_square(0, 100, 100, state)
        map_square(1, 400, 100, state)
        map_square(2, 700, 100, state)
        map_square(3, 100, 400, state)
        map_square(5, 700, 400, state)
        map_square(6, 100, 700, state)
        map_square(7, 400, 700, state)
        boss_square()
        shop_square()

        pygame.display.update()
        clock.tick(60)


def display_stuff(state):
    for i in range(state["num_of_coins"]):
        if state["coin_exist"][i]:
            game_display.blit(pixel_coin, (state["coin_x"][i], state["coin_y"][i]))
    if state["melee_timer"] > 0:
        blit_rotate_center(game_display, state["equipped_melee_dict"]["swinging_image"], (state["pixel_guy_x"], state["pixel_guy_y"]), state["pixel_guy_rotation"])
    else:
        blit_rotate_center(game_display, pixel_guy_east, (state["pixel_guy_x"], state["pixel_guy_y"]), state["pixel_guy_rotation"])
    for i in range(state["num_of_pixel_bullets"]):
        if state["bullet_exist"][i]:
            bullet(state["equipped_bullet_dict"]["image"], state["pixel_bullet_x"][i], state["pixel_bullet_y"][i], state["bullet_rotation"][i])
    for i in range(state["num_of_red_pixel_pellets"]):
        if state["red_pellet_exist"][i]:
            bullet(red_pixel_pellet, state["red_pellet_x"][i], state["red_pellet_y"][i], 0)
    for i in range(state["num_of_walls"]):
        wall(state["wall_list_x"][i], state["wall_list_y"][i])
    for i in range(state["num_of_gun_zombies"]):
        if state["gun_zombie_exist"][i]:
            if state["gun_zombie_shot_timer"][i] > 0:
                gun_zombie_red(state["gun_zombie_x"][i], state["gun_zombie_y"][i], state["gun_zombie_rotation"][i])
            elif state["gun_zombie_frozen_timer"][i] > 0:
                gun_zombie_frozen(state["gun_zombie_x"][i], state["gun_zombie_y"][i], state["gun_zombie_rotation"][i])
            else:
                gun_zombie(state["gun_zombie_x"][i], state["gun_zombie_y"][i], state["gun_zombie_rotation"][i])
    game_display.blit(border_list[state["room"]], (0, 0))
    show_money(state["coins_possessed"])
    show_health(state["pixel_guy_health"])
    show_ammo_bar(state["ammo"])
    give_prompt(state["prompt"])
    if not state["reloading"]:
        crosshair(state["crosshair_coordinates"])
    else:
        game_display.blit(state["reload_pie"], state["image_rect"])
    show_dash_bar(state["dashing_cooldown"])


def red_pellet_hit_guy(state):
    if state["dashing_timer"] == 0:
        for j in range(state["num_of_red_pixel_pellets"]):
            if state["red_pellet_exist"][j]:
                if find_if_overlapping(state["red_pellet_x"][j], state["red_pellet_y"][j], pixel_pellet_width, pixel_pellet_height, state["pixel_guy_x"], state["pixel_guy_y"], pixel_guy_width, pixel_guy_height):
                    state["red_pellet_exist"][j] = False
                    state["pixel_guy_health"] -= 1
                    if state["pixel_guy_health"] <= 0:
                        death_screen()


def bullet_hit_zombie(state):
    for i in range(state["num_of_gun_zombies"]):
        for j in range(state["num_of_pixel_bullets"]):
            if state["gun_zombie_exist"][i]:
                if state["bullet_exist"][j]:
                    if find_if_overlapping(state["pixel_bullet_x"][j], state["pixel_bullet_y"][j], pixel_bullet_width, pixel_bullet_height, state["gun_zombie_x"][i], state["gun_zombie_y"][i], gun_zombie_width, gun_zombie_height):
                        state["bullet_exist"][j] = False
                        state["gun_zombie_shot_timer"][i] = state["damage_image_length"]
                        state["gun_zombie_health"][i] -= state["equipped_bullet_dict"]["damage"]
                        if state["equipped_bullet_dict"]["name"] == "Ice Ammo":
                            state["gun_zombie_frozen_timer"][i] += 120
                        if state["gun_zombie_health"][i] <= 0:
                            state["gun_zombie_exist"][i] = False
                            if random.randrange(0, 3) == 2:
                                state["coin_x"].append(state["gun_zombie_x"][i] + gun_zombie_width / 2)
                                state["coin_y"].append(state["gun_zombie_y"][i] + gun_zombie_height / 2)
                                state["coin_exist"].append(True)
                                state["num_of_coins"] += 1


def reload(state):
    if state["reloading"] and state["reloading_timer"] == 0:
        state["reloading"] = False
        state["ammo"] = state["max_ammo"]


def move_stuff(state):
    for i in range(state["num_of_gun_zombies"]):
        if state["gun_zombie_exist"]:
            state["gun_zombie_x"][i] += state["gun_zombie_speed_x"][i]
            state["gun_zombie_y"][i] += state["gun_zombie_speed_y"][i]
    for i in range(state["num_of_pixel_bullets"]):
        if state["bullet_exist"][i]:
            state["pixel_bullet_x"][i] += state["bullet_direction_x"][i]
            state["pixel_bullet_y"][i] += state["bullet_direction_y"][i]
    for i in range(state["num_of_red_pixel_pellets"]):
        if state["red_pellet_exist"][i]:
            state["red_pellet_x"][i] += state["red_pellet_direction_x"][i]
            state["red_pellet_y"][i] += state["red_pellet_direction_y"][i]
    state["pixel_guy_x"] += state["pixel_guy_x_speed"]
    state["pixel_guy_y"] += state["pixel_guy_y_speed"]


def starting_move_timer(state):
    if state["starting_game_timer"] > 0:
        state["pixel_guy_y_speed"] = -1
        state["pixel_guy_x_speed"] = 0


def stop_stuff_at_wall(state):
    for j in range(state["num_of_gun_zombies"]):
        for i in range(state["num_of_walls"]):
            if state["gun_zombie_exist"][j]:
                if find_if_overlapping(state["gun_zombie_x"][j] + state["gun_zombie_speed_x"][j], state["gun_zombie_y"][j], gun_zombie_width, gun_zombie_height, state["wall_list_x"][i] * wall_width, state["wall_list_y"][i] * wall_height, wall_width, wall_height):
                    state["gun_zombie_speed_x"][j] = 0
                if find_if_overlapping(state["gun_zombie_x"][j], state["gun_zombie_y"][j] + state["gun_zombie_speed_y"][j], gun_zombie_width, gun_zombie_height, state["wall_list_x"][i] * wall_width, state["wall_list_y"][i] * wall_height, wall_width, wall_height):
                    state["gun_zombie_speed_y"][j] = 0

    for i in range(state["num_of_walls"]):
        if find_if_overlapping(state["pixel_guy_x"] + state["pixel_guy_x_speed"], state["pixel_guy_y"], pixel_guy_width,pixel_guy_height, state["wall_list_x"][i] * wall_width,state["wall_list_y"][i] * wall_height, wall_width, wall_height):
            state["pixel_guy_x_speed"] = 0
        if find_if_overlapping(state["pixel_guy_x"], state["pixel_guy_y"] + state["pixel_guy_y_speed"], pixel_guy_width,pixel_guy_height, state["wall_list_x"][i] * wall_width,state["wall_list_y"][i] * wall_height, wall_width, wall_height):
            state["pixel_guy_y_speed"] = 0

    for i in range(state["num_of_walls"]):
        for j in range(state["num_of_pixel_bullets"]):
            if find_if_overlapping(state["pixel_bullet_x"][j], state["pixel_bullet_y"][j], pixel_bullet_width, pixel_bullet_height, state["wall_list_x"][i] * wall_width, state["wall_list_y"][i] * wall_height, wall_width, wall_height):
                state["bullet_exist"][j] = False
        for k in range(state["num_of_red_pixel_pellets"]):
            if find_if_overlapping(state["red_pellet_x"][k], state["red_pellet_y"][k], pixel_pellet_width, pixel_pellet_height, state["wall_list_x"][i] * wall_width, state["wall_list_y"][i] * wall_height, wall_width, wall_height):
                state["red_pellet_exist"][k] = False


def zombie_decide_if_to_move(state):
    for i in range(state["num_of_gun_zombies"]):
        if not state["gun_zombie_has_los"][i]:
            if state["gun_zombie_exist"][i]:
                state["gun_zombie_speed_x"][i] = state["gun_zombie_speed"][i] * math.cos(math.radians(state["gun_zombie_rotation"][i]))
                state["gun_zombie_speed_y"][i] = -1 * state["gun_zombie_speed"][i] * math.sin(math.radians(state["gun_zombie_rotation"][i]))
        else:
            state["gun_zombie_speed_x"][i] = 0
            state["gun_zombie_speed_y"][i] = 0


def gun_zombies_shoot(state):
    for i in range(state["num_of_gun_zombies"]):
        if state["gun_zombie_has_los"][i]:
            if state["gun_zombie_exist"][i]:
                if state["gun_zombie_timer"][i] == 0:
                    state["red_pellet_x"].append(state["gun_zombie_x"][i] + 40 + 25 * math.cos(math.radians(state["gun_zombie_rotation"][i])) + 25 * math.sin(math.radians(state["gun_zombie_rotation"][i])))
                    state["red_pellet_y"].append(state["gun_zombie_y"][i] + 40 + -25 * math.sin(math.radians(state["gun_zombie_rotation"][i])) + 25 * math.cos(math.radians(state["gun_zombie_rotation"][i])))
                    state["red_pellet_direction_x"].append(7 * math.cos(math.radians(state["gun_zombie_rotation"][i])))
                    state["red_pellet_direction_y"].append(-7 * math.sin(math.radians(state["gun_zombie_rotation"][i])))
                    state["red_pellet_exist"].append(True)
                    state["num_of_red_pixel_pellets"] += 1
                    state["red_pellet_x"].append(state["gun_zombie_x"][i] + 40 + 25 * math.cos(math.radians(state["gun_zombie_rotation"][i])) - 25 * math.sin(math.radians(state["gun_zombie_rotation"][i])))
                    state["red_pellet_y"].append(state["gun_zombie_y"][i] + 40 + -25 * math.sin(math.radians(state["gun_zombie_rotation"][i])) - 25 * math.cos(math.radians(state["gun_zombie_rotation"][i])))
                    state["red_pellet_direction_x"].append(7 * math.cos(math.radians(state["gun_zombie_rotation"][i])))
                    state["red_pellet_direction_y"].append(-7 * math.sin(math.radians(state["gun_zombie_rotation"][i])))
                    state["red_pellet_exist"].append(True)
                    state["num_of_red_pixel_pellets"] += 1
                    if state["gun_zombie_frozen_timer"][i] > 0:
                        state["gun_zombie_timer"][i] = 90
                    else:
                        state["gun_zombie_timer"][i] = 45


def find_if_los(state):
    for j in range(state["num_of_walls"]):
        for i in range(state["num_of_gun_zombies"]):
            for k in range(0, int(math.floor(calculate_distance(state["gun_zombie_x"][i] + gun_zombie_width / 2, state["gun_zombie_y"][i] + gun_zombie_height / 2, state["wall_list_x"][j] * wall_width + wall_width / 2,state["wall_list_y"][j] * wall_height + wall_height / 2))), 7):
                if find_if_overlapping(state["gun_zombie_x"][i] + 40 + k * math.cos(math.radians(state["gun_zombie_rotation"][i])), state["gun_zombie_y"][i] + 40 + -1 * k * math.sin(math.radians(state["gun_zombie_rotation"][i])), 0, 0, state["wall_list_x"][j] * wall_width, state["wall_list_y"][j] * wall_height, wall_width, wall_height):
                    state["gun_zombie_has_los"][i] = False


def melee(state):
    if state["mouse_click"][2] == 1 and state["melee_cooldown"] == 0 and state["dashing_timer"] == 0:
        state["melee_cooldown"] = state["equipped_melee_dict"]["delay"]
        state["melee_timer"] = 20
        for i in range(state["num_of_gun_zombies"]):
            if find_if_overlapping(state["pixel_guy_x"], state["pixel_guy_y"], pixel_guy_width, pixel_guy_height, state["gun_zombie_x"][i], state["gun_zombie_y"][i], gun_zombie_width,gun_zombie_height):
                state["gun_zombie_health"][i] -= state["equipped_melee_dict"]["damage"]
                state["gun_zombie_shot_timer"][i] = state["damage_image_length"]
                if state["equipped_melee_dict"]["name"] == "Frost Sword":
                    state["gun_zombie_frozen_timer"][i] += 180
                if state["gun_zombie_health"][i] <= 0:
                    state["gun_zombie_exist"][i] = False
                    if random.randrange(0, 3) == 2:
                        state["coin_x"].append(state["gun_zombie_x"][i] + gun_zombie_width / 2)
                        state["coin_y"].append(state["gun_zombie_y"][i] + gun_zombie_height / 2)
                        state["coin_exist"].append(True)
                        state["num_of_coins"] += 1


def fire_bullet(state):
    if state["mouse_click"][0] == 1 and state["bullet_delay"] == 0 and state["ammo"] > 0 and state["dashing_timer"] == 0:
        state["pixel_bullet_x"].append(state["pixel_guy_x"] + pixel_guy_width / 2 + 70 * math.cos(math.radians(state["pixel_guy_rotation"])))
        state["pixel_bullet_y"].append(state["pixel_guy_y"] + pixel_guy_height / 2 + -70 * math.sin(math.radians(state["pixel_guy_rotation"])))
        state["bullet_direction_x"].append(7 * math.cos(math.radians(state["pixel_guy_rotation"])))
        state["bullet_direction_y"].append(-7 * math.sin(math.radians(state["pixel_guy_rotation"])))
        state["bullet_exist"].append(True)
        state["bullet_rotation"].append(state["pixel_guy_rotation"])
        state["num_of_pixel_bullets"] += 1
        state["bullet_delay"] = state["equipped_bullet_dict"]["fire_delay"]
        state["ammo"] -= 1


def dont_let_go_off_screen(state):
    if state["pixel_guy_y"] <= 0 and state["pixel_guy_y_speed"] <= 0:
        state["pixel_guy_y_speed"] = 0
    if state["pixel_guy_y"] >= 1000 - pixel_guy_height and state["pixel_guy_y_speed"] >= 0:
        state["pixel_guy_y_speed"] = 0
    if state["pixel_guy_x"] <= 0 and state["pixel_guy_x_speed"] <= 0:
        state["pixel_guy_x_speed"] = 0
    if state["pixel_guy_x"] >= 1000 - pixel_guy_width and state["pixel_guy_x_speed"] >= 0:
        state["pixel_guy_x_speed"] = 0


def event_handling(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                state["pixel_guy_y_speed"] = 0
            if event.key == pygame.K_a:
                state["pixel_guy_x_speed"] = 0
            if event.key == pygame.K_s:
                state["pixel_guy_y_speed"] = 0
            if event.key == pygame.K_d:
                state["pixel_guy_x_speed"] = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                inventory_screen(state)
            if event.key == pygame.K_m and state["map_cooldown"] == 0:
                map_screen(state)
            if event.key == pygame.K_r:
                if state["reloading_timer"] == 0:
                    state["reloading_timer"] += state["reloading_length"]
                    state["reloading"] = True
            if event.key == pygame.K_LSHIFT:
                if state["dashing_cooldown"] == 0:
                    state["dashing_timer"] = 12
                    state["dashing_cooldown"] = 60
                    state["pixel_guy_x_speed"] *= 4
                    state["pixel_guy_y_speed"] *= 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                state["e_just_pressed"] = False

    if state["dashing_timer"] == 0:
        if pygame.key.get_pressed()[pygame.K_w]:
            state["pixel_guy_y_speed"] = -1 * state["pixel_guy_speed"]
        if pygame.key.get_pressed()[pygame.K_a]:
            state["pixel_guy_x_speed"] = -1 * state["pixel_guy_speed"]
        if pygame.key.get_pressed()[pygame.K_s]:
            state["pixel_guy_y_speed"] = state["pixel_guy_speed"]
        if pygame.key.get_pressed()[pygame.K_d]:
            state["pixel_guy_x_speed"] = state["pixel_guy_speed"]


def set_aiming_variables(state):
    state["mouse_click"] = pygame.mouse.get_pressed()
    state["mouse_coordinates"] = pygame.mouse.get_pos()
    state["crosshair_coordinates"] = (state["mouse_coordinates"][0] - crosshair_width / 2, state["mouse_coordinates"][1] - crosshair_height / 2)
    state["aim_x"] = state["crosshair_coordinates"][0] - (state["pixel_guy_x"] + 40)
    state["aim_y"] = state["crosshair_coordinates"][1] - (state["pixel_guy_y"] + 40)

    for i in range(state["num_of_gun_zombies"]):
        state["gun_zombie_aim_x"][i] = state["pixel_guy_x"] - state["gun_zombie_x"][i]
        state["gun_zombie_aim_y"][i] = state["pixel_guy_y"] - state["gun_zombie_y"][i]
        state["gun_zombie_rotation"][i] = find_rotation(state["gun_zombie_aim_x"][i], state["gun_zombie_aim_y"][i])

    state["pil_size"] = 75
    state["pil_image"] = Image.new("RGBA", (state["pil_size"], state["pil_size"]))
    pil_draw = ImageDraw.Draw(state["pil_image"])
    pil_draw.pieslice((0, 0, state["pil_size"] - 1, state["pil_size"] - 1),
                      (state["reloading_timer"] * (360 / state["reloading_length"])), 0, fill=grey)
    state["mode"] = state["pil_image"].mode
    state["size"] = state["pil_image"].size
    state["data"] = state["pil_image"].tobytes()

    state["reload_pie"] = pygame.image.fromstring(state["data"], state["size"], state["mode"])

    state["image_rect"] = state["reload_pie"].get_rect(center=state["crosshair_coordinates"])

    state["pixel_guy_rotation"] = find_rotation(state["aim_x"], state["aim_y"])


def set_loop_variables(state):
    state["current_room_cleared"] = True
    state["prompt"] = None

    for i in range(state["num_of_gun_zombies"]):
        state["gun_zombie_has_los"][i] = True
        if state["gun_zombie_exist"][i]:
            state["current_room_cleared"] = False
        if state["gun_zombie_timer"][i] > 0:
            state["gun_zombie_timer"][i] -= 1
        if state["gun_zombie_shot_timer"][i] > 0:
            state["gun_zombie_shot_timer"][i] -= 1
        if state["gun_zombie_frozen_timer"][i] > 0:
            state["gun_zombie_frozen_timer"][i] -= 1
            state["gun_zombie_speed"][i] = 1
        else:
            state["gun_zombie_speed"][i] = 2

    if state["starting_game_timer"] > 0:
        state["starting_game_timer"] -= 1
    if state["map_cooldown"] > 0:
        state["map_cooldown"] -= 1
    if state["melee_timer"] > 0:
        state["melee_timer"] -= 1
    if state["melee_cooldown"] > 0:
        state["melee_cooldown"] -= 1
    if state["dashing_cooldown"] > 0:
        state["dashing_cooldown"] -= 1
    if state["dashing_timer"] > 0:
        state["dashing_timer"] -= 1
    if state["ammo"] == 0 and not state["reloading"]:
        state["prompt"] = "Press R To Reload"
    if state["bullet_delay"] > 0:
        state["bullet_delay"] -= 1
    if state["reloading"]:
        state["reloading_timer"] -= 1

    if state["room"] == 0:
        state["can_enter_top"] = False
        state["can_enter_left"] = False
        state["can_enter_right"] = True
        state["can_enter_bottom"] = True
    if state["room"] == 1:
        state["can_enter_top"] = False
        state["can_enter_left"] = True
        state["can_enter_right"] = True
        state["can_enter_bottom"] = False
    if state["room"] == 2:
        state["can_enter_top"] = False
        state["can_enter_left"] = True
        state["can_enter_right"] = False
        state["can_enter_bottom"] = True
    if state["room"] == 3:
        state["can_enter_top"] = True
        state["can_enter_left"] = False
        state["can_enter_right"] = False
        state["can_enter_bottom"] = True
    if state["room"] == 5:
        state["can_enter_top"] = True
        state["can_enter_left"] = False
        state["can_enter_right"] = False
        state["can_enter_bottom"] = False
    if state["room"] == 6:
        state["can_enter_top"] = True
        state["can_enter_left"] = False
        state["can_enter_right"] = True
        state["can_enter_bottom"] = False
    if state["room"] == 7:
        state["can_enter_top"] = False
        state["can_enter_left"] = True
        state["can_enter_right"] = False
        state["can_enter_bottom"] = False

    for i in range(len(state["ammo_list"])):
        if state["ammo_list"][i]["equipped"]:
            state["equipped_bullet_dict"] = state["ammo_list"][i]

    for i in range(len(state["melee_list"])):
        if state["melee_list"][i]["equipped"]:
            state["equipped_melee_dict"] = state["melee_list"][i]
            break
        else:
            state["equipped_melee_dict"] = state["fists"]


def set_room_types(state):
    type_chosen = random.randrange(0, state["num_of_room_types"])
    type_taken = False
    for i in range(len(state["types_taken"])):
        if type_chosen == state["types_taken"][i]:
            type_taken = True
    if not type_taken:
        return type_chosen
    else:
        return set_room_types(state)


def set_pre_level_variables(state):
    for i in range(9):
        if i != 4 and i != 8:
            type_chosen = set_room_types(state)
            state["types_taken"].append(type_chosen)
            state["room_list"][i]["room_type"] = type_chosen

    state["ammo"] = state["max_ammo"]
    state["wall_list_x"] = wall_list_list_x_bottom[get_room_type(state["room"], state)]
    state["wall_list_y"] = wall_list_list_y_bottom[get_room_type(state["room"], state)]
    state["gun_zombie_x"] = gun_zombie_list_list_x_bottom[get_room_type(state["room"], state)]
    state["gun_zombie_y"] = gun_zombie_list_list_y_bottom[get_room_type(state["room"], state)]
    state["num_of_gun_zombies"] = len(state["gun_zombie_x"])

    for i in range(state["num_of_gun_zombies"]):
        state["gun_zombie_health"].append(state["gun_zombie_max_health"])
        state["gun_zombie_exist"].append(True)
        state["gun_zombie_aim_x"].append(5)
        state["gun_zombie_aim_y"].append(5)
        state["gun_zombie_rotation"].append(90)
        state["gun_zombie_has_los"].append(True)
        state["gun_zombie_timer"].append(0)
        state["gun_zombie_shot_timer"].append(0)
        state["gun_zombie_frozen_timer"].append(0)
        state["gun_zombie_speed_x"].append(0)
        state["gun_zombie_speed_y"].append(0)
        state["gun_zombie_speed"].append(2)
        state["gun_zombie_x"][i] *= wall_width
        state["gun_zombie_y"][i] *= wall_height

    state["num_of_walls"] = len(state["wall_list_x"])


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def give_prompt(prompt):
    if prompt is not None:
        large_text = pygame.font.SysFont("comicsansms", 70)
        text_surf, text_rect = text_objects(prompt, large_text, black)
        text_rect.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surf, text_rect)
        pygame.display.update()


def show_ammo_bar(ammo):
    if ammo == 15:
        color = green
    else:
        color = blue
    rect_width = 6 * ammo
    large_text = pygame.font.SysFont("comicsansms", 30)
    text_surf, text_rect = text_objects("Ammo: ", large_text, black)
    text_rect.center = (display_width - 340, display_height - 30)
    game_display.blit(text_surf, text_rect)
    pygame.draw.rect(game_display, color, (display_width - 300, display_height - 37, rect_width, 20))


def show_dash_bar(dash_cooldown):
    if dash_cooldown == 0:
        color = green
    else:
        color = bright_red
    rect_width = 1.5 * (60 - dash_cooldown)
    large_text = pygame.font.SysFont("comicsansms", 30)
    text_surf, text_rect = text_objects("Dash:", large_text, black)
    text_rect.center = (display_width - 150, display_height - 30)
    game_display.blit(text_surf, text_rect)
    pygame.draw.rect(game_display, color, (display_width - 110, display_height - 37, rect_width, 20))
    pygame.display.update()


def death_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill(white)
        large_text = pygame.font.SysFont("comicsansms", 100)
        text_surf, text_rect = text_objects("You Died :(", large_text, black)
        text_rect.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surf, text_rect)
        pygame.display.update()


def show_money(coins):
    game_display.blit(bigger_coin, (10, 10))
    font = pygame.font.SysFont("comicsansms", 41)
    text = font.render(str(coins), True, black)
    game_display.blit(text, (20 + big_coin_width, 0))


def show_health(health):
    if health == 1:
        game_display.blit(half_heart, (10, display_height - pixel_heart_height))
    if health >= 2:
        game_display.blit(heart, (10, display_height - pixel_heart_height))
    if health == 3:
        game_display.blit(half_heart, (10 + 10 + pixel_heart_width, display_height - pixel_heart_height))
    if health >= 4:
        game_display.blit(heart, (10 + 10 + pixel_heart_width, (display_height - pixel_heart_height)))
    if health == 5:
        game_display.blit(half_heart, (10 + 2 * (10 + pixel_heart_width), (display_height - pixel_heart_height)))
    if health >= 6:
        game_display.blit(heart, (10 + 2 * (10 + pixel_heart_width), (display_height - pixel_heart_height)))
    if health == 7:
        game_display.blit(half_heart, (10 + 3 * (10 + pixel_heart_width), (display_height - pixel_heart_height)))
    if health >= 8:
        game_display.blit(heart, (10 + 3 * (10 + pixel_heart_width), (display_height - pixel_heart_height)))
    if health == 9:
        game_display.blit(half_heart, (10 + 4 * (10 + pixel_heart_width), (display_height - pixel_heart_height)))
    if health >= 10:
        game_display.blit(heart, (10 + 4 * (10 + pixel_heart_width), (display_height - pixel_heart_height)))


def find_if_overlapping(x1, y1, w1, h1, x2, y2, w2, h2):
    if x2 < x1 < x2 + w2:
        if y2 < y1 < y2 + h2:
            return True
    if x2 < x1 + w1 < x2 + w2:
        if y2 < y1 < y2 + h2:
            return True
    if x2 < x1 + w1 < x2 + w2:
        if y2 < y1 + h1 < y2 + h2:
            return True
    if x2 < x1 < x2 + w2:
        if y2 < y1 + h1 < y2 + h2:
            return True
    if x2 < x1 < x2 + w2:
        if y1 + h1 > y2 and y1 < y2 + h2:
            return True
    if x2 < x1 + w1 < x2 + w2:
        if y1 + h1 > y2 and y1 < y2 + h2:
            return True
    if x1 + w1 > x2 and x1 < x2 + w2:
        if y2 < y1 < y2 + h2:
            return True
    if x1 + w1 > x2 and x1 < x2 + w2:
        if y2 < y1 + h1 < y2 + h2:
            return True
    if x1 + w1 > x2 and x1 < x2 + w2:
        if y1 + h1 > y2 and y1 < y2 + h2:
            return True


def find_rotation(aim_x, aim_y):
    if aim_y == 0 and aim_x > 0:
        return 0
    elif aim_y == 0 and aim_x < 0:
        return 180
    elif aim_x == 0 and aim_y > 0:
        return 270
    elif aim_x == 0 and aim_y < 0:
        return 90
    elif aim_x > 0 and aim_y > 0:
        return math.degrees(math.atan2(-1 * aim_y, aim_x))
    elif aim_x > 0 > aim_y:
        return math.degrees(math.atan2(-1 * aim_y, aim_x))
    elif aim_x < 0 < aim_y:
        return math.degrees(math.atan2(-1 * aim_y, aim_x))
    elif aim_x < 0 and aim_y < 0:
        return math.degrees(math.atan2(-1 * aim_y, aim_x))


def calculate_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist


def wall(x, y):
    wall_coordinates = (x * wall_width, y * wall_height)
    game_display.blit(stone_wall, wall_coordinates)


def blit_rotate_center(surf, image, topleft, angle=1):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect.topleft)


def gun_zombie(x, y, rotation):
    blit_rotate_center(game_display, gun_zombie_image, (x, y), rotation)


def gun_zombie_frozen(x, y, rotation):
    blit_rotate_center(game_display, gun_zombie_frozen_image, (x, y), rotation)


def gun_zombie_red(x, y, rotation):
    blit_rotate_center(game_display, gun_zombie_red_image, (x, y), rotation)


def bullet(image, x, y, rotation):
    blit_rotate_center(game_display, image, (x, y), rotation)


def crosshair(coords):
    game_display.blit(pixel_crosshair, coords)


def pixel_guy(image, x, y):
    game_display.blit(image, (x, y))


def get_room_type(room, state):
    return state["room_list"][room]["room_type"]


def get_room_rotation(room, state):
    return state["room_list"][room]["room_rotation"]


def get_room_entered(room, state):
    return state["room_list"][room]["entered"]


def button(msg, x, y, w, h, ic, ac, action=None, param=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + 50 > mouse[1] > y:
        pygame.draw.rect(game_display, ac, (x, y, w, h))
        if click[0] == 1 and action is not None and param is not None:
            action(param)
        elif click[0] == 1 and action is not None and param is None:
            action()
    else:
        pygame.draw.rect(game_display, ic, (x, y, w, h))

    small_text = pygame.font.SysFont("comicsansms", 20)
    text_surf, text_rect = text_objects(msg, small_text, black)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    game_display.blit(text_surf, text_rect)


def inactive_button(msg, x, y, w, h, c):
    pygame.draw.rect(game_display, c, (x, y, w, h))

    small_text = pygame.font.SysFont("comicsansms", 20)
    text_surf, text_rect = text_objects(msg, small_text, black)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    game_display.blit(text_surf, text_rect)


def edit_ammo(params):
    state = params[0]
    drop_dist = params[1]
    ammo_index = params[2]
    state["ammo_editing"][0] = True
    state["ammo_editing"][1] = drop_dist
    state["ammo_editing"][2] = ammo_index


def ammo_drop_down(state):
    drop_dist = 0
    for i in range(len(state["ammo_list"])):
        if state["ammo_list"][i]["owned"] and not state["ammo_list"][i]["equipped"]:
            button(state["ammo_list"][i]["name"], 100, 500 + drop_dist, 200, 50, grey, white, edit_ammo, [state, drop_dist, [i]])
            drop_dist += 50


def start_ammo_drop_down(state):
    state["ammo_drop_downing"] = True
    state["sights_drop_downing"] = False
    state["sights_editing"] = [False, 0, ""]
    state["magazines_drop_downing"] = False
    state["magazines_editing"] = [False, 0, ""]
    state["barrel_drop_downing"] = False
    state["barrel_editing"] = [False, 0, ""]


def equip_ammo(params):
    state = params[0]
    i = params[1][0]
    for j in range(len(state["ammo_list"])):
        state["ammo_list"][j]["equipped"] = False
    state["ammo_list"][i]["equipped"] = True
    state["ammo_editing"] = [False, 0, ""]


def discard_ammo(params):
    state = params[0]
    i = params[1][0]
    state["ammo_list"][i]["owned"] = False
    state["ammo_editing"] = [False, 0, ""]


def edit_magazines(params):
    state = params[0]
    drop_dist = params[1]
    magazines_index = params[2]
    state["magazines_editing"][0] = True
    state["magazines_editing"][1] = drop_dist
    state["magazines_editing"][2] = magazines_index


def magazines_drop_down(state):
    drop_dist = 0
    for i in range(len(state["magazines_list"])):
        if state["magazines_list"][i]["owned"] and not state["magazines_list"][i]["equipped"]:
            button(state["magazines_list"][i]["name"], 100, 750 + drop_dist, 200, 50, grey, white, edit_magazines, [state, drop_dist, [i]])
            drop_dist += 50


def start_magazines_drop_down(state):
    state["magazines_drop_downing"] = True
    state["sights_drop_downing"] = False
    state["sights_editing"] = [False, 0, ""]
    state["ammo_drop_downing"] = False
    state["ammo_editing"] = [False, 0, ""]
    state["barrel_drop_downing"] = False
    state["barrel_editing"] = [False, 0, ""]


def equip_magazines(params):
    state = params[0]
    i = params[1][0]
    for j in range(len(state["magazines_list"])):
        state["magazines_list"][j]["equipped"] = False
    state["magazines_list"][i]["equipped"] = True
    state["magazines_editing"] = [False, 0, ""]


def discard_magazines(params):
    state = params[0]
    i = params[1][0]
    state["magazines_list"][i]["owned"] = False
    state["magazines_editing"] = [False, 0, ""]


def edit_sights(params):
    state = params[0]
    drop_dist = params[1]
    ammo_index = params[2]
    state["sights_editing"][0] = True
    state["sights_editing"][1] = drop_dist
    state["sights_editing"][2] = ammo_index


def sights_drop_down(state):
    drop_dist = 0
    for i in range(len(state["sights_list"])):
        if state["sights_list"][i]["owned"] and not state["sights_list"][i]["equipped"]:
            button(state["sights_list"][i]["name"], 700, 500 + drop_dist, 200, 50, grey, white, edit_sights, [state, drop_dist, [i]])
            drop_dist += 50


def start_sights_drop_down(state):
    state["sights_drop_downing"] = True
    state["ammo_drop_downing"] = False
    state["ammo_editing"] = [False, 0, ""]
    state["magazines_drop_downing"] = False
    state["magazines_editing"] = [False, 0, ""]
    state["barrel_drop_downing"] = False
    state["barrel_editing"] = [False, 0, ""]


def equip_sights(params):
    state = params[0]
    i = params[1][0]
    for j in range(len(state["sights_list"])):
        state["sights_list"][j]["equipped"] = False
    state["sights_list"][i]["equipped"] = True
    state["sights_editing"] = [False, 0, ""]


def discard_sights(params):
    state = params[0]
    i = params[1][0]
    state["sights_list"][i]["owned"] = False
    state["sights_editing"] = [False, 0, ""]


def edit_barrel(params):
    state = params[0]
    drop_dist = params[1]
    barrel_index = params[2]
    state["barrel_editing"][0] = True
    state["barrel_editing"][1] = drop_dist
    state["barrel_editing"][2] = barrel_index


def barrel_drop_down(state):
    drop_dist = 0
    for i in range(len(state["barrels_list"])):
        if state["barrels_list"][i]["owned"] and not state["barrels_list"][i]["equipped"]:
            button(state["barrels_list"][i]["name"], 700, 750 + drop_dist, 200, 50, grey, white, edit_barrel, [state, drop_dist, [i]])
            drop_dist += 50


def start_barrel_drop_down(state):
    state["barrel_drop_downing"] = True
    state["sights_drop_downing"] = False
    state["sights_editing"] = [False, 0, ""]
    state["magazines_drop_downing"] = False
    state["magazines_editing"] = [False, 0, ""]
    state["ammo_drop_downing"] = False
    state["ammo_editing"] = [False, 0, ""]


def equip_barrel(params):
    state = params[0]
    i = params[1][0]
    for j in range(len(state["barrels_list"])):
        state["barrels_list"][j]["equipped"] = False
    state["barrels_list"][i]["equipped"] = True
    state["barrel_editing"] = [False, 0, ""]


def discard_barrel(params):
    state = params[0]
    i = params[1][0]
    state["barrel_list"][i]["owned"] = False
    state["barrel_editing"] = [False, 0, ""]


def switch_to_item_screen(state):
    state["screen"] = "items"


def switch_to_attachment_screen(state):
    state["screen"] = "attachments"


def amulet_square(x, y, amulet_dict, state, mouse_x, mouse_y, i):
    if find_if_overlapping(mouse_x, mouse_y, 0, 0, x, y, 155, 155):
        pygame.draw.rect(game_display, light_black, (x, y, 155, 155))
        pygame.draw.rect(game_display, dirt_color, (x + 3, y + 3, 149, 149))
        pygame.draw.rect(game_display, light_blue, (x + 10, y + 10, 135, 135))
        game_display.blit(amulet_dict["highlighted_image"], (x + 10, y + 20))
        if pygame.mouse.get_pressed()[0] == 1 and state["mouse_unclicked"] and not state["amulets_list"][i]["equipped"]:
            state["amulets_editing"] = [True, i]

    elif state["amulets_editing"] == [True, i]:
        pygame.draw.rect(game_display, light_black, (x, y, 155, 155))
        pygame.draw.rect(game_display, yellow, (x + 3, y + 3, 149, 149))
        pygame.draw.rect(game_display, light_blue, (x + 10, y + 10, 135, 135))
        game_display.blit(amulet_dict["highlighted_image"], (x + 10, y + 20))

    else:
        pygame.draw.rect(game_display, black, (x, y, 155, 155))
        pygame.draw.rect(game_display, brown, (x + 3, y + 3, 149, 149))
        pygame.draw.rect(game_display, light_blue, (x + 10, y + 10, 135, 135))
        game_display.blit(amulet_dict["image"], (x + 10, y + 20))

    large_text = pygame.font.SysFont("comicsansms", 20)
    text_surf, text_rect = text_objects(amulet_dict["name"], large_text, black)
    text_rect.center = (x + 77.5, y + 170)
    game_display.blit(text_surf, text_rect)


def melee_square(x, y, melee_dict, state, mouse_x, mouse_y, i):
    if find_if_overlapping(mouse_x, mouse_y, 0, 0, x, y, 155, 155):
        pygame.draw.rect(game_display, light_black, (x, y, 155, 155))
        pygame.draw.rect(game_display, dirt_color, (x + 3, y + 3, 149, 149))
        pygame.draw.rect(game_display, light_blue, (x + 10, y + 10, 135, 135))
        game_display.blit(melee_dict["highlighted_image"], (x + 10, y + 10))
        if pygame.mouse.get_pressed()[0] == 1 and state["mouse_unclicked"] and not state["melee_list"][i]["equipped"]:
            state["melee_editing"] = [True, i]

    elif state["melee_editing"] == [True, i]:
        pygame.draw.rect(game_display, light_black, (x, y, 155, 155))
        pygame.draw.rect(game_display, yellow, (x + 3, y + 3, 149, 149))
        pygame.draw.rect(game_display, light_blue, (x + 10, y + 10, 135, 135))
        game_display.blit(melee_dict["highlighted_image"], (x + 10, y + 10))

    else:
        pygame.draw.rect(game_display, black, (x, y, 155, 155))
        pygame.draw.rect(game_display, brown, (x + 3, y + 3, 149, 149))
        pygame.draw.rect(game_display, light_blue, (x + 10, y + 10, 135, 135))
        game_display.blit(melee_dict["image"], (x + 10, y + 10))

    large_text = pygame.font.SysFont("comicsansms", 20)
    text_surf, text_rect = text_objects(melee_dict["name"], large_text, black)
    text_rect.center = (x + 77.5, y + 170)
    game_display.blit(text_surf, text_rect)


def potion_square(x, y, potion_dict, state, mouse_x, mouse_y, i, j):
    if find_if_overlapping(mouse_x, mouse_y, 0, 0, x, y, 155, 155):
        pygame.draw.rect(game_display, light_black, (x, y, 155, 155))
        pygame.draw.rect(game_display, dirt_color, (x + 3, y + 3, 149, 149))
        pygame.draw.rect(game_display, light_blue, (x + 10, y + 10, 135, 135))
        game_display.blit(potion_dict["highlighted_image"], (x + 10, y + 30))
        if pygame.mouse.get_pressed()[0] == 1 and state["mouse_unclicked"]:
            state["potions_editing"] = [True, i, j]

    elif state["potions_editing"] == [True, i, j]:
        pygame.draw.rect(game_display, light_black, (x, y, 155, 155))
        pygame.draw.rect(game_display, yellow, (x + 3, y + 3, 149, 149))
        pygame.draw.rect(game_display, light_blue, (x + 10, y + 10, 135, 135))
        game_display.blit(potion_dict["highlighted_image"], (x + 10, y + 30))

    else:
        pygame.draw.rect(game_display, black, (x, y, 155, 155))
        pygame.draw.rect(game_display, brown, (x + 3, y + 3, 149, 149))
        pygame.draw.rect(game_display, light_blue, (x + 10, y + 10, 135, 135))
        game_display.blit(potion_dict["image"], (x + 10, y + 30))

    large_text = pygame.font.SysFont("comicsansms", 20)
    text_surf, text_rect = text_objects(potion_dict["name"], large_text, black)
    text_rect.center = (x + 77.5, y + 170)
    game_display.blit(text_surf, text_rect)


def drink_potion(params):
    state = params[1]
    potion_dict = state["potions_list"][params[0]]
    potion_dict["effect_timer"] = potion_dict["effect_length"]
    state["potions_editing"] = [False, 0, 0]
    potion_dict["quantity"] -= 1


def discard_potion(params):
    state = params[1]
    potion_dict = state["potions_list"][params[0]]
    state["potions_editing"] = [False, 0, 0]
    potion_dict["quantity"] -= 1


def equip_amulet(params):
    state = params[1]
    amulet_dict = state["amulets_list"][params[0]]
    state["amulets_editing"] = [False, 0]
    for i in range(len(state["amulets_list"])):
        state["amulets_list"][i]["equipped"] = False
    amulet_dict["equipped"] = True


def discard_amulet(params):
    state = params[1]
    amulet_dict = state["amulets_list"][params[0]]
    state["amulets_editing"] = [False, 0]
    amulet_dict["owned"] = False
    amulet_dict["equipped"] = False


def unequip_amulet(amulet_dict):
    amulet_dict["equipped"] = False


def equip_melee(params):
    state = params[1]
    melee_dict = state["melee_list"][params[0]]
    state["melee_editing"] = [False, 0]
    for i in range(len(state["melee_list"])):
        state["melee_list"][i]["equipped"] = False
    melee_dict["equipped"] = True


def discard_melee(params):
    state = params[1]
    melee_dict = state["melee_list"][params[0]]
    state["melee_editing"] = [False, 0]
    melee_dict["owned"] = False
    melee_dict["equipped"] = False


def unequip_melee(melee_dict):
    melee_dict["equipped"] = False


def inventory_screen(state):
    pygame.mouse.set_visible(True)
    screening = True
    while screening:
        if pygame.mouse.get_pressed()[0] == 0:
            state["mouse_unclicked"] = True
        mouse = pygame.mouse.get_pos()

        if state["screen"] == "attachments":
            state["description"] = ""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        state["sights_drop_downing"] = False
                        state["sights_editing"] = [False, 0, ""]
                        state["ammo_drop_downing"] = False
                        state["ammo_editing"] = [False, 0, ""]
                        state["magazines_drop_downing"] = False
                        state["magazines_editing"] = [False, 0, ""]
                        state["barrel_drop_downing"] = False
                        state["barrel_editing"] = [False, 0, ""]
                        pygame.mouse.set_visible(False)
                        screening = False
                    if event.key == pygame.K_ESCAPE:
                        state["sights_drop_downing"] = False
                        state["sights_editing"] = [False, 0, ""]
                        state["ammo_drop_downing"] = False
                        state["ammo_editing"] = [False, 0, ""]
                        state["magazines_drop_downing"] = False
                        state["magazines_editing"] = [False, 0, ""]
                        state["barrel_drop_downing"] = False
                        state["barrel_editing"] = [False, 0, ""]

            game_display.fill(light_blue)

            button("", 500, 0, 500, 50, dark_blue, middle_blue, switch_to_item_screen, state)

            large_text = pygame.font.SysFont("comicsansms", 30)
            text_surf, text_rect = text_objects("Attachments", large_text, black)
            text_rect.center = (250, 25)
            game_display.blit(text_surf, text_rect)
            text_surf, text_rect = text_objects("Items", large_text, black)
            text_rect.center = (750, 25)
            game_display.blit(text_surf, text_rect)
            game_display.blit(pixel_gun_side, (0, 50))

            for i in range(len(state["magazines_list"])):
                if state["magazines_list"][i]["equipped"]:
                    if find_if_overlapping(mouse[0], mouse[1], 0, 0, 360, 230, 160, 180):
                        game_display.blit(state["magazines_list"][i]["highlighted_image"], (0, 50))
                        state["description"] = state["magazines_list"][i]["description"]
                    else:
                        game_display.blit(state["magazines_list"][i]["image"], (0, 50))

            for i in range(len(state["ammo_list"])):
                if state["ammo_list"][i]["equipped"]:
                    if find_if_overlapping(mouse[0], mouse[1], 0, 0, 175, 300, pixel_bullet_width * 5, pixel_bullet_height * 5):
                        game_display.blit(state["ammo_list"][i]["highlighted_image"], (175, 300))
                        state["description"] = state["ammo_list"][i]["description"]
                    else:
                        game_display.blit(state["ammo_list"][i]["big_image"], (175, 300))

            for i in range(len(state["sights_list"])):
                if state["sights_list"][i]["equipped"]:
                    if find_if_overlapping(mouse[0], mouse[1], 0, 0, 420, 40, 200, 80):
                        game_display.blit(state["sights_list"][i]["highlighted_image"], (0, 50))
                        state["description"] = state["sights_list"][i]["description"]
                    else:
                        game_display.blit(state["sights_list"][i]["image"], (0, 50))

            for i in range(len(state["barrels_list"])):
                if state["barrels_list"][i]["equipped"]:
                    if find_if_overlapping(mouse[0], mouse[1], 0, 0, 20, 170, 140, 100):
                        game_display.blit(state["barrels_list"][i]["highlighted_image"], (0, 50))
                        state["description"] = state["barrels_list"][i]["description"]
                    else:
                        game_display.blit(state["barrels_list"][i]["image"], (0, 50))

            if state["ammo_editing"][0]:
                button("Equip", 300, 475 + state["ammo_editing"][1], 200, 50, dark_green, light_green, equip_ammo, [state, state["ammo_editing"][2]])
                button("Discard", 300, 525 + state["ammo_editing"][1], 200, 50, dark_red, bright_red, discard_ammo, [state, state["ammo_editing"][2]])
            if state["sights_editing"][0]:
                button("Equip", 500, 475 + state["sights_editing"][1], 200, 50, dark_green, light_green, equip_sights, [state, state["sights_editing"][2]])
                if state["sights_editing"][2] != [0]:
                    button("Discard", 500, 525 + state["sights_editing"][1], 200, 50, dark_red, bright_red, discard_sights, [state, state["sights_editing"][2]])
            if state["magazines_editing"][0]:
                button("Equip", 300, 725 + state["magazines_editing"][1], 200, 50, dark_green, light_green, equip_magazines, [state, state["magazines_editing"][2]])
                button("Discard", 300, 775 + state["magazines_editing"][1], 200, 50, dark_red, bright_red, discard_magazines, [state, state["magazines_editing"][2]])
            if state["barrel_editing"][0]:
                button("Equip", 500, 725 + state["barrel_editing"][1], 200, 50, dark_green, light_green, equip_barrel, [state, state["barrel_editing"][2]])
                if state["barrel_editing"][2] != [0]:
                    button("Discard", 500, 775 + state["barrel_editing"][1], 200, 50, dark_red, bright_red, discard_barrel, [state, state["barrel_editing"][2]])

            button("Ammo", 100, 450, 200, 50, dark_green, light_green, start_ammo_drop_down, state)
            button("Sights", 700, 450, 200, 50, dark_green, light_green, start_sights_drop_down, state)
            button("Magazines", 100, 700, 200, 50, dark_green, light_green, start_magazines_drop_down, state)
            button("Barrel Attachments", 700, 700, 200, 50, dark_green, light_green, start_barrel_drop_down, state)

            large_text = pygame.font.SysFont("comicsansms", 35)
            text_surf, text_rect = text_objects(state["description"], large_text, black)
            text_rect.center = (display_width / 2, 950)
            game_display.blit(text_surf, text_rect)

            if state["ammo_drop_downing"]:
                ammo_drop_down(state)
            if state["sights_drop_downing"]:
                sights_drop_down(state)
            if state["magazines_drop_downing"]:
                magazines_drop_down(state)
            if state["barrel_drop_downing"]:
                barrel_drop_down(state)

            clock.tick(60)

            pygame.display.update()

        if state["screen"] == "items":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        state["potions_editing"] = [False, 0, 0]
                        state["amulets_editing"] = [False, 0]
                        state["melee_editing"] = [False, 0]
                        pygame.mouse.set_visible(False)
                        screening = False
                    if event.key == pygame.K_ESCAPE:
                        state["potions_editing"] = [False, 0, 0]
                        state["amulets_editing"] = [False, 0]
                        state["melee_editing"] = [False, 0]

            game_display.fill(light_blue)

            button("", 0, 0, 500, 50, dark_blue, middle_blue, switch_to_attachment_screen, state)

            large_text = pygame.font.SysFont("comicsansms", 30)
            text_surf, text_rect = text_objects("Attachments", large_text, black)
            text_rect.center = (250, 25)
            game_display.blit(text_surf, text_rect)
            text_surf, text_rect = text_objects("Items", large_text, black)
            text_rect.center = (750, 25)
            game_display.blit(text_surf, text_rect)
            large_text_underlined = pygame.font.SysFont("comicsansms", 38)
            pygame.font.Font.set_underline(large_text_underlined, True)
            text_surf, text_rect = text_objects("Potions", large_text_underlined, black)
            text_rect.center = (435, 90)
            game_display.blit(text_surf, text_rect)
            large_text_underlined = pygame.font.SysFont("comicsansms", 38)
            pygame.font.Font.set_underline(large_text_underlined, True)
            text_surf, text_rect = text_objects("Effects", large_text_underlined, black)
            text_rect.center = (910, 90)
            game_display.blit(text_surf, text_rect)

            large_text_underlined = pygame.font.SysFont("comicsansms", 38)
            pygame.font.Font.set_underline(large_text_underlined, True)
            text_surf, text_rect = text_objects("Amulets", large_text_underlined, black)
            text_rect.center = (332.5, 530)
            game_display.blit(text_surf, text_rect)

            large_text_underlined = pygame.font.SysFont("comicsansms", 38)
            pygame.font.Font.set_underline(large_text_underlined, True)
            text_surf, text_rect = text_objects("Melee Weapons", large_text_underlined, black)
            text_rect.center = (332.5, 530 + 230)
            game_display.blit(text_surf, text_rect)

            pygame.draw.rect(game_display, black, (840, 120, 140, 360))
            pygame.draw.rect(game_display, light_blue, (845, 125, 130, 350))

            effect_drop_dist = 0

            for i in range(len(state["potions_list"])):
                if state["potions_list"][i]["effect_timer"] > 0:
                    effect_timer_minutes = str(math.floor(state["potions_list"][i]["effect_timer"] / 3600))
                    effect_timer_seconds = str(math.floor(math.floor(state["potions_list"][i]["effect_timer"] % 3600) / 60))
                    large_text = pygame.font.SysFont("comicsansms", 18)
                    text_surf, text_rect = text_objects(state["potions_list"][i]["effect_name"] + "- " + effect_timer_minutes + ":" + effect_timer_seconds, large_text, black)
                    game_display.blit(text_surf, (845, 120 + effect_drop_dist))
                    effect_drop_dist += 30

            potion_spot_x = 50
            potion_spot_y = 125
            for i in range(len(state["potions_list"])):
                for j in range(state["potions_list"][i]["quantity"]):
                    potion_square(potion_spot_x, potion_spot_y, state["potions_list"][i], state,  mouse[0], mouse[1], i, j)
                    potion_spot_x += 205
                    if potion_spot_x == 870:
                        potion_spot_x = 50
                        potion_spot_y += 205

            amulet_spot_x = 50
            amulet_spot_y = 560
            for i in range(len(state["amulets_list"])):
                if state["amulets_list"][i]["owned"] and not state["amulets_list"][i]["equipped"]:
                    amulet_square(amulet_spot_x, amulet_spot_y, state["amulets_list"][i], state,  mouse[0], mouse[1], i)
                    amulet_spot_x += 205
                elif state["amulets_list"][i]["owned"] and state["amulets_list"][i]["equipped"]:
                    amulet_square(795, amulet_spot_y, state["amulets_list"][i], state,  mouse[0], mouse[1], i)

            melee_spot_x = 50
            melee_spot_y = 560 + 230
            for i in range(len(state["melee_list"])):
                if state["melee_list"][i]["owned"] and not state["melee_list"][i]["equipped"]:
                    melee_square(melee_spot_x, melee_spot_y, state["melee_list"][i], state, mouse[0], mouse[1], i)
                    melee_spot_x += 205
                elif state["melee_list"][i]["owned"] and state["melee_list"][i]["equipped"]:
                    melee_square(795, melee_spot_y, state["melee_list"][i], state, mouse[0], mouse[1], i)

            if state["potions_editing"][0]:
                button("Drink", potion_spot_x + 27.5, potion_spot_y + 15, 100, 50, dark_green, light_green, drink_potion, (state["potions_editing"][1], state))
                button("Discard", potion_spot_x + 27.5, potion_spot_y + 90, 100, 50, dark_red, bright_red, discard_potion, (state["potions_editing"][1], state))

            if state["amulets_editing"][0]:
                button("Equip", amulet_spot_x + 27.5, amulet_spot_y + 15, 100, 50, dark_green, light_green, equip_amulet, (state["amulets_editing"][1], state))
                button("Discard", amulet_spot_x + 27.5, amulet_spot_y + 90, 100, 50, dark_red, bright_red, discard_amulet, (state["amulets_editing"][1], state))
            else:
                for i in range(len(state["amulets_list"])):
                    if state["amulets_list"][i]["owned"] and state["amulets_list"][i]["equipped"]:
                        button("Unequip", 795 - 27.5 - 100, amulet_spot_y + 52.5, 100, 50, dark_red, bright_red, unequip_amulet, state["amulets_list"][i])

            if state["melee_editing"][0]:
                button("Equip", melee_spot_x + 27.5, melee_spot_y + 15, 100, 50, dark_green, light_green, equip_melee, (state["melee_editing"][1], state))
                button("Discard", melee_spot_x + 27.5, melee_spot_y + 90, 100, 50, dark_red, bright_red, discard_melee, (state["melee_editing"][1], state))
            else:
                for i in range(len(state["melee_list"])):
                    if state["melee_list"][i]["owned"] and state["melee_list"][i]["equipped"]:
                        button("Unequip", 795 - 27.5 - 100, melee_spot_y + 52.5, 100, 50, dark_red, bright_red, unequip_melee, state["melee_list"][i])

            pygame.display.update()

            clock.tick(60)


def enter_room(state):
    if state["current_room_cleared"]:
        if state["can_enter_right"] and find_if_overlapping(state["pixel_guy_x"], state["pixel_guy_y"], pixel_guy_width, pixel_guy_height, display_width - 100, display_height / 2 - 50, 100, 100) and not state["e_just_pressed"]:
            if pygame.key.get_pressed()[pygame.K_e]:
                new_room(state["room"] + 1, state["room_list"][state["room"] + 1]["entered"], state, "left")
        elif state["can_enter_bottom"] and find_if_overlapping(state["pixel_guy_x"], state["pixel_guy_y"], pixel_guy_width, pixel_guy_height, display_width / 2 - 50, display_height - 100, 100, 100) and not state["e_just_pressed"]:
            if pygame.key.get_pressed()[pygame.K_e]:
                new_room(state["room"] + 3, state["room_list"][state["room"] + 3]["entered"], state, "top")
        elif state["can_enter_left"] and find_if_overlapping(state["pixel_guy_x"], state["pixel_guy_y"], pixel_guy_width, pixel_guy_height, 0, display_height / 2 - 50, 100, 100) and not state["e_just_pressed"]:
            if pygame.key.get_pressed()[pygame.K_e]:
                new_room(state["room"] - 1, state["room_list"][state["room"] - 1]["entered"], state, "right")
        elif state["can_enter_top"] and find_if_overlapping(state["pixel_guy_x"], state["pixel_guy_y"], pixel_guy_width, pixel_guy_height, display_width / 2 - 50, 0, 100, 100) and not state["e_just_pressed"]:
            if pygame.key.get_pressed()[pygame.K_e]:
                new_room(state["room"] - 3, state["room_list"][state["room"] - 3]["entered"], state, "bottom")


def pick_up_coins(state):
    for i in range(state["num_of_coins"]):
        if state["coin_exist"][i]:
            if find_if_overlapping(state["pixel_guy_x"], state["pixel_guy_y"], pixel_guy_width, pixel_guy_height, state["coin_x"][i], state["coin_y"][i], coin_width, coin_height):
                state["coins_possessed"] += 1
                state["coin_exist"][i] = False


def new_room(new_room_number, entered, state, side_entered):
    state["room"] = new_room_number
    state["current_room_cleared"] = False
    state["room_list"][new_room_number]["entered"] = True

    if not entered:
        state["room_list"][state["room"]]["room_rotation"] = side_entered
        state["gun_zombie_x"] = gun_zombie_dictionary_x[get_room_rotation(state["room"], state)][get_room_type(state["room"], state)]
        state["gun_zombie_y"] = gun_zombie_dictionary_y[get_room_rotation(state["room"], state)][get_room_type(state["room"], state)]
    else:
        state["gun_zombie_x"] = []
        state["gun_zombie_y"] = []

    state["wall_list_x"] = wall_dictionary_x[get_room_rotation(state["room"], state)][get_room_type(state["room"], state)]
    state["wall_list_y"] = wall_dictionary_y[get_room_rotation(state["room"], state)][get_room_type(state["room"], state)]

    if side_entered == "bottom":
        state["pixel_guy_x"] = (display_width - pixel_guy_width) / 2
        state["pixel_guy_y"] = display_height - pixel_guy_height

    if side_entered == "top":
        state["pixel_guy_x"] = (display_width - pixel_guy_width) / 2
        state["pixel_guy_y"] = 0

    if side_entered == "left":
        state["pixel_guy_x"] = 0
        state["pixel_guy_y"] = (display_height - pixel_guy_height) / 2

    if side_entered == "right":
        state["pixel_guy_x"] = display_width - pixel_guy_width
        state["pixel_guy_y"] = (display_height - pixel_guy_height) / 2

    state["pixel_guy_speed"] = 5
    state["pixel_guy_x_speed"] = 0
    state["pixel_guy_y_speed"] = 0
    state["starting_game_timer"] = 1
    state["melee_timer"] = 0
    state["melee_cooldown"] = 0
    state["dashing_cooldown"] = 0
    state["dashing_timer"] = 0

    state["pixel_bullet_x"] = []
    state["pixel_bullet_y"] = []
    state["bullet_direction_x"] = []
    state["bullet_direction_y"] = []
    state["bullet_exist"] = []

    state["red_pellet_x"] = []
    state["red_pellet_y"] = []
    state["red_pellet_direction_x"] = []
    state["red_pellet_direction_y"] = []
    state["red_pellet_exist"] = []

    state["num_of_red_pixel_pellets"] = 0
    state["num_of_pixel_bullets"] = 0
    state["bullet_delay"] = 0
    state["reloading_timer"] = 0
    state["reloading"] = False

    state["gun_zombie_health"] = []
    state["gun_zombie_exist"] = []
    state["gun_zombie_aim_x"] = []
    state["gun_zombie_aim_y"] = []
    state["gun_zombie_rotation"] = []
    state["gun_zombie_has_los"] = []
    state["gun_zombie_timer"] = []
    state["gun_zombie_speed_x"] = []
    state["gun_zombie_speed_y"] = []
    state["gun_zombie_speed"] = []
    state["gun_zombie_frozen_timer"] = []
    state["gun_zombie_shot_timer"] = []
    state["bullet_rotation"] = []
    state["num_of_gun_zombies"] = len(state["gun_zombie_x"])
    state["e_just_pressed"] = True

    state["coin_x"] = []
    state["coin_y"] = []
    state["coin_exist"] = []
    state["num_of_coins"] = 0

    for i in range(state["num_of_gun_zombies"]):
        state["gun_zombie_health"].append(state["gun_zombie_max_health"])
        state["gun_zombie_exist"].append(True)
        state["gun_zombie_aim_x"].append(5)
        state["gun_zombie_rotation"].append(90)
        state["gun_zombie_has_los"].append(True)
        state["gun_zombie_aim_y"].append(5)
        state["gun_zombie_timer"].append(0)
        state["gun_zombie_speed_x"].append(0)
        state["gun_zombie_speed_y"].append(0)
        state["gun_zombie_speed"].append(2)
        state["gun_zombie_x"][i] *= wall_width
        state["gun_zombie_y"][i] *= wall_height
        state["gun_zombie_shot_timer"].append(0)
        state["gun_zombie_frozen_timer"].append(0)

    state["num_of_walls"] = len(state["wall_list_x"])


def new_level():
    fists = {
        "name": "Fists",
        "owned": True,
        "equipped": False,
        "swinging_image": pixel_melee_fists,
        "damage": 1,
        "delay": 35
    }
    steel_sword = {
        "name": "Steel Sword",
        "description": "Deals 3 damage with an average swinging rate.",
        "image": pixel_steel_sword,
        "highlighted_image": pixel_steel_sword_highlighted,
        "swinging_image": pixel_guy_swinging,
        "owned": True,
        "equipped": False,
        "damage": 3,
        "delay": 60
    }

    ice_sword = {
        "name": "Frost Sword",
        "description": "Deals 2 damage with an average swinging rate and slows enemies.",
        "image": pixel_ice_sword,
        "highlighted_image": pixel_ice_sword_highlighted,
        "swinging_image": pixel_melee_ice_sword,
        "owned": True,
        "equipped": False,
        "damage": 2,
        "delay": 60
    }

    hammer = {
        "name": "Hammer",
        "description": "Deals 5 damage with an slow swinging rate.",
        "image": pixel_hammer,
        "highlighted_image": pixel_hammer_highlighted,
        "swinging_image": pixel_melee_hammer,
        "owned": True,
        "equipped": False,
        "damage": 5,
        "delay": 180
    }

    speed_potion = {
        "name": "Potion of Celerity",
        "description": "Increases your speed by 3.",
        "image": pixel_potion_yellow,
        "highlighted_image": pixel_potion_yellow_highlighted,
        "quantity": 4,
        "effect_type": "speed",
        "effect_length": 5400,
        "effect_name": "Speed",
        "effect_timer": 0
    }

    strength_potion = {
        "name": "Potion of Strength",
        "description": "Increases your melee damage by one.",
        "image": pixel_potion_red,
        "highlighted_image": pixel_potion_red_highlighted,
        "quantity": 3,
        "effect_type": "strength",
        "effect_length": 5400,
        "effect_name": "Strength",
        "effect_timer": 0
    }

    amulet_of_wrenches = {
        "name": "Amulet of Wrenches",
        "description": "Not yet desided",
        "image": pixel_wrench_amulet,
        "highlighted_image": pixel_wrench_amulet_highlighted,
        "owned": True,
        "equipped": False
    }

    amulet_of_healing = {
        "name": "Amulet of Healing",
        "description": "Refills your health after clearing a level.",
        "image": pixel_heart_amulet,
        "highlighted_image": pixel_heart_amulet_highlighted,
        "owned": True,
        "equipped": False
    }

    amulet_of_dashing = {
        "name": "Amulet of Dashing",
        "description": "Allows you to dash much faster.",
        "image": pixel_arrow_amulet,
        "highlighted_image": pixel_arrow_amulet_highlighted,
        "owned": True,
        "equipped": False
    }

    no_sight = {
        "name": "No Sight",
        "description": "",
        "image": blank_image,
        "highlighted_image": blank_image,
        "owned": True,
        "equipped": True
    }

    red_dot_sight = {
        "name": "Red Dot Sight",
        "description": "Displays a red line on your screen to help you aim.",
        "image": pixel_red_dot_sight,
        "highlighted_image": pixel_red_dot_sight_highlighted,
        "owned": True,
        "equipped": False
    }

    default_magazine = {
        "name": "Stater Clip",
        "description": "Capacity: 15",
        "image": blank_image,
        "highlighted_image": pixel_magazine_highlighted,
        "owned": True,
        "equipped": True
    }

    extended_magazine = {
        "name": "Extended Magazine",
        "description": "Capacity: 25",
        "image": pixel_extended_magazine,
        "highlighted_image": pixel_extended_magazine_highlighted,
        "owned": True,
        "equipped": False
    }

    default_ammo = {
        "name": "Basic Ammo",
        "description": "Damage: 1 - Fire Rate: Average",
        "image": pixel_bullet,
        "big_image": big_pixel_bullet,
        "highlighted_image": big_pixel_bullet_highlighted,
        "owned": True,
        "equipped": True,
        "damage": 1,
        "fire_delay": 15
    }

    ice_ammo = {
        "name": "Ice Ammo",
        "description": "Damage: 1 - Fire Rate: Average - Slows down enemies",
        "image": blue_pixel_bullet,
        "big_image": big_blue_pixel_bullet,
        "highlighted_image": big_blue_pixel_bullet_highlighted,
        "owned": True,
        "equipped": False,
        "damage": 1,
        "fire_delay": 15
    }

    default_barrel = {
        "name": "No Attachment",
        "description": "",
        "image": blank_image,
        "highlighted_image": blank_image,
        "owned": True,
        "equipped": True
    }

    default_barrel_extension = {
        "name": "Basic Extension",
        "description": "Fire Rate: -15% - Bullet Speed: + 30%",
        "image": pixel_default_barrel_extension,
        "highlighted_image": pixel_default_barrel_extension_highlighted,
        "owned": True,
        "equipped": False
    }

    room_0 = {
        "room_type": "",
        "room_rotation": "bottom",
        "entered": True
    }
    room_1 = {
        "room_type": "",
        "room_rotation": "",
        "entered": False
    }
    room_2 = {
        "room_type": "",
        "room_rotation": "",
        "entered": False
    }
    room_3 = {
        "room_type": "",
        "room_rotation": "",
        "entered": False
    }
    room_4 = {
        "room_type": "",
        "room_rotation": "",
        "entered": False
    }
    room_5 = {
        "room_type": "",
        "room_rotation": "",
        "entered": False
    }
    room_6 = {
        "room_type": "",
        "room_rotation": "",
        "entered": False
    }
    room_7 = {
        "room_type": "",
        "room_rotation": "",
        "entered": False
    }
    room_8 = {
        "room_type": "",
        "room_rotation": "",
        "entered": False
    }
    state = {
        "room": 0,
        "room_list": [room_0, room_1, room_2, room_3, room_4, room_5, room_6, room_7, room_8],
        "screen": "attachments",
        "mouse_unclicked": True,
        "amulets_editing": [False, 0],
        "fists": fists,
        "equipped_melee_dict": "",
        "melee_list": [steel_sword, ice_sword, hammer],
        "melee_editing": [False, 0],
        "amulets_list": [amulet_of_healing, amulet_of_wrenches, amulet_of_dashing],
        "potions_editing": [False, 0, 0],
        "potions_list": [strength_potion, speed_potion],
        "sights_list": [no_sight, red_dot_sight],
        "ammo_list": [default_ammo, ice_ammo],
        "ammo_editing": [False, 0, ""],
        "ammo_drop_downing": False,
        "sights_editing": [False, 0, ""],
        "sights_drop_downing": False,
        "magazines_editing": [False, 0, ""],
        "magazines_drop_downing": False,
        "barrel_editing": [False, 0, ""],
        "barrel_drop_downing": False,
        "magazines_list": [default_magazine, extended_magazine],
        "barrels_list": [default_barrel, default_barrel_extension],
        "num_of_room_types": len(wall_list_list_x_bottom),
        "current_room_cleared": True,
        "types_taken": [],
        "description": "",
        "can_enter_top": False,
        "can_enter_bottom": False,
        "can_enter_left": False,
        "can_enter_right": False,
        "pixel_guy_x": (display_width - pixel_guy_width) / 2,
        "pixel_guy_y": display_height - pixel_guy_height,
        "pixel_guy_speed": 5,
        "pixel_guy_x_speed": 0,
        "pixel_guy_y_speed": 0,
        "pixel_guy_health": 100,
        "starting_game_timer": 1,
        "melee_timer": 0,
        "melee_cooldown": 0,
        "dashing_cooldown": 0,
        "dashing_timer": 0,
        "map_cooldown": 0,

        "pixel_bullet_x": [],
        "pixel_bullet_y": [],
        "bullet_direction_x": [],
        "bullet_direction_y": [],
        "bullet_exist": [],
        "bullet_rotation": [],

        "red_pellet_x": [],
        "red_pellet_y": [],
        "red_pellet_direction_x": [],
        "red_pellet_direction_y": [],
        "red_pellet_exist": [],

        "num_of_red_pixel_pellets": 0,
        "num_of_pixel_bullets": 0,
        "bullet_delay": 0,
        "max_ammo": 15,
        "ammo": 15,
        "reloading_timer": 0,
        "reloading_length": 90,
        "reloading": False,

        "wall_list_x": [],
        "wall_list_y": [],
        "gun_zombie_x": [],
        "gun_zombie_y": [],
        "gun_zombie_health": [],
        "gun_zombie_max_health": 5,
        "num_of_gun_zombies": 0,
        "gun_zombie_exist": [],
        "gun_zombie_aim_x": [],
        "gun_zombie_aim_y": [],
        "gun_zombie_rotation": [],
        "gun_zombie_has_los": [],
        "gun_zombie_timer": [],
        "gun_zombie_speed_x": [],
        "gun_zombie_speed_y": [],
        "gun_zombie_speed": [],
        "gun_zombie_shot_timer": [],
        "gun_zombie_frozen_timer": [],

        "coin_x": [],
        "coin_y": [],
        "coin_exist": [],
        "num_of_coins": 0,
        "coins_possessed": 0,

        "prompt": "",
        "mouse_click": "",
        "crosshair_coordinates": "",
        "aim_x": "",
        "aim_y": "",
        "pil_size": "",
        "pil_image": "",
        "pil_draw": "",
        "mode": "",
        "size": "",
        "data": "",
        "reload_pie": "",
        "image_rect": "",
        "pixel_guy_rotation": "",
        "e_just_pressed": "",
        "equipped_bullet_dict": "",
        "damage_image_length": 15
    }

    set_pre_level_variables(state)

    while True:
        set_loop_variables(state)

        game_display.fill(dirt_color)

        set_aiming_variables(state)

        event_handling(state)

        dont_let_go_off_screen(state)

        fire_bullet(state)

        melee(state)

        find_if_los(state)

        gun_zombies_shoot(state)

        zombie_decide_if_to_move(state)

        stop_stuff_at_wall(state)

        pick_up_coins(state)

        starting_move_timer(state)

        move_stuff(state)

        reload(state)

        bullet_hit_zombie(state)

        red_pellet_hit_guy(state)

        display_stuff(state)

        pygame.display.update()

        clock.tick(60)

        enter_room(state)


new_level()
