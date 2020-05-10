import pygame
import math
import random
from PIL import Image, ImageDraw

pygame.init()

display_width = 1000
display_height = 1000

yellow = (255, 255, 51)
gray = (128, 128, 128)
black = (0, 0, 0)
white = (255, 255, 255)
grey = (127, 127, 127)
red = (255, 0, 0)
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
wall_width = 50
wall_height = 50
guy_square_dimension = 181
pixel_heart_width = 45
pixel_heart_height = 45
melee_swoosh_width = 100
melee_swoosh_height = 50

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dungeon_Explorer")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

pixel_guy_north = pygame.image.load("pixel_guy.png").convert_alpha()
pixel_guy_north = pygame.transform.scale(pixel_guy_north, (pixel_guy_width, pixel_guy_height))
tiny_pixel_guy = pygame.transform.scale(pixel_guy_north, (26, 26))
pixel_guy_east = pygame.transform.rotate(pixel_guy_north, -90)
pixel_crosshair = pygame.image.load("pixil-frame-0.png").convert_alpha()
pixel_crosshair = pygame.transform.scale(pixel_crosshair, (crosshair_width, crosshair_height))
pixel_pellet = pygame.image.load("pixel_pellet.png").convert_alpha()
pixel_pellet = pygame.transform.scale(pixel_pellet, (pixel_pellet_width, pixel_pellet_height))
stone_wall = pygame.image.load("stone_wall.png").convert_alpha()
stone_wall = pygame.transform.scale(stone_wall, (wall_width, wall_height))
gun_zombie_image = pygame.image.load("pixel_zombie_with_guns.png").convert_alpha()
gun_zombie_image = pygame.transform.scale(gun_zombie_image, (gun_zombie_width, gun_zombie_height))
red_pixel_pellet = pygame.image.load("red_pixel_pellet.png").convert_alpha()
red_pixel_pellet = pygame.transform.scale(red_pixel_pellet, (pixel_pellet_width, pixel_pellet_height))
heart = pygame.image.load("full_pixel_heart.png").convert_alpha()
heart = pygame.transform.scale(heart, (pixel_heart_width, pixel_heart_height))
half_heart = pygame.image.load("half_pixel_heart.png").convert_alpha()
half_heart = pygame.transform.scale(half_heart, (pixel_heart_width, pixel_heart_height))
pixel_guy_swinging = pygame.image.load("pixel_guy_360_swing.png").convert_alpha()
pixel_guy_swinging = pygame.transform.scale(pixel_guy_swinging, (pixel_guy_width, pixel_guy_height))
pixel_guy_swinging = pygame.transform.rotate(pixel_guy_swinging, -90)
pixel_question_mark = pygame.image.load("pixel_question_mark.png")
pixel_question_mark = pygame.transform.scale(pixel_question_mark, (150, 150))
pixel_boss_logo = pygame.image.load("pixel_boss_logo.png")
pixel_boss_logo = pygame.transform.scale(pixel_boss_logo, (150, 150))
pixel_coin = pygame.image.load("pixel_coin.png")
pixel_coin = pygame.transform.scale(pixel_coin, (150, 150))

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
    pygame.draw.rect(game_display, red, (400, 400, 200, 200))
    pygame.draw.rect(game_display, black, (400 + border_width, 400 + border_width, 200 - 2 * border_width, 200 - 2 * border_width))
    game_display.blit(pixel_boss_logo, (425, 425))


def shop_square():
    border_width = 10
    pygame.draw.rect(game_display, yellow, (700, 700, 200, 200))
    pygame.draw.rect(game_display, black, (700 + border_width, 700 + border_width, 200 - 2 * border_width, 200 - 2 * border_width))
    game_display.blit(pixel_coin, (725, 725))


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
        for i in range(len(wall_dictionary_x[get_room_rotation(state["room"], state)][get_room_type(state["room"], state)])):
            pygame.draw.rect(game_display, gray, (x + wall_dictionary_x[get_room_rotation(state["room"], state)][get_room_type(state["room"], state)][i] * 10, y + wall_dictionary_x[get_room_rotation(state["room"], state)][get_room_type(state["room"], state)][i] * 10, 10, 10))
    else:
        pygame.draw.rect(game_display, red, (x, y, 200, 200))
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
        map_square(4, 700, 400, state)
        map_square(5, 100, 700, state)
        map_square(6, 400, 700, state)
        boss_square()
        shop_square()

        pygame.display.update()
        clock.tick(60)


def display_stuff(state):
    if state["melee_timer"] > 0:
        blit_rotate_center(game_display, pixel_guy_swinging, (state["pixel_guy_x"], state["pixel_guy_y"]), state["pixel_guy_rotation"])
    else:
        blit_rotate_center(game_display, pixel_guy_east, (state["pixel_guy_x"], state["pixel_guy_y"]), state["pixel_guy_rotation"])
    for i in range(state["num_of_pixel_pellets"]):
        if state["pellet_exist"][i]:
            bullet(pixel_pellet, state["pixel_pellet_x"][i], state["pixel_pellet_y"][i])
    for i in range(state["num_of_red_pixel_pellets"]):
        if state["red_pellet_exist"][i]:
            bullet(red_pixel_pellet, state["red_pellet_x"][i], state["red_pellet_y"][i])
    for i in range(state["num_of_walls"]):
        wall(state["wall_list_x"][i], state["wall_list_y"][i])
    for i in range(state["num_of_gun_zombies"]):
        if state["gun_zombie_exist"][i]:
            gun_zombie(state["gun_zombie_x"][i], state["gun_zombie_y"][i], state["gun_zombie_rotation"][i])
    game_display.blit(border_list[state["room"]], (0, 0))
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


def pellet_hit_zombie(state):
    for i in range(state["num_of_gun_zombies"]):
        for j in range(state["num_of_pixel_pellets"]):
            if state["gun_zombie_exist"][i]:
                if state["pellet_exist"][j]:
                    if find_if_overlapping(state["pixel_pellet_x"][j], state["pixel_pellet_y"][j], pixel_pellet_width, pixel_pellet_height, state["gun_zombie_x"][i], state["gun_zombie_y"][i], gun_zombie_width, gun_zombie_height):
                        state["pellet_exist"][j] = False
                        state["gun_zombie_health"][i] -= 1
                        if state["gun_zombie_health"][i] <= 0:
                            state["gun_zombie_exist"][i] = False


def reload(state):
    if state["reloading"] and state["reloading_timer"] == 0:
        state["reloading"] = False
        state["ammo"] = state["max_ammo"]


def move_stuff(state):
    for i in range(state["num_of_gun_zombies"]):
        if state["gun_zombie_exist"]:
            state["gun_zombie_x"][i] += state["gun_zombie_speed_x"][i]
            state["gun_zombie_y"][i] += state["gun_zombie_speed_y"][i]
    for i in range(state["num_of_pixel_pellets"]):
        if state["pellet_exist"][i]:
            state["pixel_pellet_x"][i] += state["pellet_direction_x"][i]
            state["pixel_pellet_y"][i] += state["pellet_direction_y"][i]
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
                if find_if_overlapping(state["gun_zombie_x"][j] + state["gun_zombie_speed_x"][j],state["gun_zombie_y"][j], gun_zombie_width, gun_zombie_height, state["wall_list_x"][i] * wall_width, state["wall_list_y"][i] * wall_height, wall_width, wall_height):
                    state["gun_zombie_speed_x"][j] = 0
                if find_if_overlapping(state["gun_zombie_x"][j], state["gun_zombie_y"][j] + state["gun_zombie_speed_y"][j], gun_zombie_width, gun_zombie_height, state["wall_list_x"][i] * wall_width, state["wall_list_y"][i] * wall_height, wall_width, wall_height):
                    state["gun_zombie_speed_y"][j] = 0

    for i in range(state["num_of_walls"]):
        if find_if_overlapping(state["pixel_guy_x"] + state["pixel_guy_x_speed"], state["pixel_guy_y"], pixel_guy_width,pixel_guy_height, state["wall_list_x"][i] * wall_width,state["wall_list_y"][i] * wall_height, wall_width, wall_height):
            state["pixel_guy_x_speed"] = 0
        if find_if_overlapping(state["pixel_guy_x"], state["pixel_guy_y"] + state["pixel_guy_y_speed"], pixel_guy_width,pixel_guy_height, state["wall_list_x"][i] * wall_width,state["wall_list_y"][i] * wall_height, wall_width, wall_height):
            state["pixel_guy_y_speed"] = 0

    for i in range(state["num_of_walls"]):
        for j in range(state["num_of_pixel_pellets"]):
            if find_if_overlapping(state["pixel_pellet_x"][j], state["pixel_pellet_y"][j], pixel_pellet_width,
                                   pixel_pellet_height, state["wall_list_x"][i] * wall_width,
                                   state["wall_list_y"][i] * wall_height, wall_width, wall_height):
                state["pellet_exist"][j] = False
        for k in range(state["num_of_red_pixel_pellets"]):
            if find_if_overlapping(state["red_pellet_x"][k], state["red_pellet_y"][k], pixel_pellet_width,
                                   pixel_pellet_height, state["wall_list_x"][i] * wall_width,
                                   state["wall_list_y"][i] * wall_height, wall_width, wall_height):
                state["red_pellet_exist"][k] = False


def zombie_decide_if_to_move(state):
    for i in range(state["num_of_gun_zombies"]):
        if not state["gun_zombie_has_los"][i]:
            if state["gun_zombie_exist"][i]:
                state["gun_zombie_speed_x"][i] = 2 * math.cos(math.radians(state["gun_zombie_rotation"][i]))
                state["gun_zombie_speed_y"][i] = -2 * math.sin(math.radians(state["gun_zombie_rotation"][i]))
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
                    state["gun_zombie_timer"][i] = 45


def find_if_los(state):
    for j in range(state["num_of_walls"]):
        for i in range(state["num_of_gun_zombies"]):
            for k in range(0, int(math.floor(calculate_distance(state["gun_zombie_x"][i] + gun_zombie_width / 2, state["gun_zombie_y"][i] + gun_zombie_height / 2, state["wall_list_x"][j] * wall_width + wall_width / 2,state["wall_list_y"][j] * wall_height + wall_height / 2))), 7):
                if find_if_overlapping(state["gun_zombie_x"][i] + 40 + k * math.cos(math.radians(state["gun_zombie_rotation"][i])), state["gun_zombie_y"][i] + 40 + -1 * k * math.sin(math.radians(state["gun_zombie_rotation"][i])), 0, 0, state["wall_list_x"][j] * wall_width, state["wall_list_y"][j] * wall_height, wall_width, wall_height):
                    state["gun_zombie_has_los"][i] = False


def melee(state):
    if state["mouse_click"][2] == 1 and state["melee_cooldown"] == 0 and state["dashing_timer"] == 0:
        state["melee_cooldown"] = 60
        state["melee_timer"] = 20
        for i in range(state["num_of_gun_zombies"]):
            if find_if_overlapping(state["pixel_guy_x"], state["pixel_guy_y"], pixel_guy_width, pixel_guy_height,state["gun_zombie_x"][i], state["gun_zombie_y"][i], gun_zombie_width,gun_zombie_height):
                state["gun_zombie_health"][i] -= 5
                if state["gun_zombie_health"][i] <= 0:
                    state["gun_zombie_exist"][i] = False


def fire_pellet(state):
    if state["mouse_click"][0] == 1 and state["pellet_delay"] == 0 and state["ammo"] > 0 and state["dashing_timer"] == 0:
        state["pixel_pellet_x"].append(state["pixel_guy_x"] + 40 + 25 * math.cos(math.radians(state["pixel_guy_rotation"])))
        state["pixel_pellet_y"].append(state["pixel_guy_y"] + 40 + -25 * math.sin(math.radians(state["pixel_guy_rotation"])))
        state["pellet_direction_x"].append(7 * math.cos(math.radians(state["pixel_guy_rotation"])))
        state["pellet_direction_y"].append(-7 * math.sin(math.radians(state["pixel_guy_rotation"])))
        state["pellet_exist"].append(True)
        state["num_of_pixel_pellets"] += 1
        state["pellet_delay"] = 15
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
    if state["pellet_delay"] > 0:
        state["pellet_delay"] -= 1
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
        state["can_enter_bottom"] = True
    if state["room"] == 6:
        state["can_enter_top"] = True
        state["can_enter_left"] = False
        state["can_enter_right"] = True
        state["can_enter_bottom"] = False
    if state["room"] == 7:
        state["can_enter_top"] = False
        state["can_enter_left"] = True
        state["can_enter_right"] = True
        state["can_enter_bottom"] = False


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
        state["gun_zombie_speed_x"].append(0)
        state["gun_zombie_speed_y"].append(0)
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
        color = red
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


def bullet(image, x, y):
    game_display.blit(image, (x, y))


def crosshair(coords):
    game_display.blit(pixel_crosshair, coords)


def pixel_guy(image, x, y):
    game_display.blit(image, (x, y))


def new_room(new_room_number, entered, state, side_entered):
    state["room"] = new_room_number
    state["current_room_cleared"] = False
    state["room_list"][new_room_number]["entered"] = True

    if not entered:
        state["room_list"][state["room"]]["room_rotation"] = side_entered
        state["gun_zombie_x"] = gun_zombie_dictionary_x[get_room_rotation(state["room"], state)][get_room_type(state["room"], state)]
        state["gun_zombie_y"] = gun_zombie_dictionary_y[get_room_rotation(state["room"], state)][get_room_type(state["room"], state)]

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

    state["pixel_pellet_x"] = []
    state["pixel_pellet_y"] = []
    state["pellet_direction_x"] = []
    state["pellet_direction_y"] = []
    state["pellet_exist"] = []

    state["red_pellet_x"] = []
    state["red_pellet_y"] = []
    state["red_pellet_direction_x"] = []
    state["red_pellet_direction_y"] = []
    state["red_pellet_exist"] = []

    state["num_of_red_pixel_pellets"] = 0
    state["num_of_pixel_pellets"] = 0
    state["pellet_delay"] = 0
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

    for i in range(state["num_of_gun_zombies"]):
        state["gun_zombie_health"].append(state["gun_zombie_max_health"])
        state["gun_zombie_exist"].append(True)
        state["gun_zombie_aim_x"].append(5)
        state["gun_zombie_aim_y"].append(5)
        state["gun_zombie_rotation"].append(90)
        state["gun_zombie_has_los"].append(True)
        state["gun_zombie_timer"].append(0)
        state["gun_zombie_speed_x"].append(0)
        state["gun_zombie_speed_y"].append(0)
        state["gun_zombie_x"][i] *= wall_width
        state["gun_zombie_y"][i] *= wall_height

    state["num_of_walls"] = len(state["wall_list_x"])


def get_room_type(room, state):
    return state["room_list"][room]["room_type"]


def get_room_rotation(room, state):
    return state["room_list"][room]["room_rotation"]


def get_room_entered(room, state):
    return state["room_list"][room]["entered"]


def new_level():
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
        "num_of_room_types": len(wall_list_list_x_bottom),
        "current_room_cleared": True,
        "types_taken": [],
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

        "pixel_pellet_x": [],
        "pixel_pellet_y": [],
        "pellet_direction_x": [],
        "pellet_direction_y": [],
        "pellet_exist": [],

        "red_pellet_x": [],
        "red_pellet_y": [],
        "red_pellet_direction_x": [],
        "red_pellet_direction_y": [],
        "red_pellet_exist": [],

        "num_of_red_pixel_pellets": 0,
        "num_of_pixel_pellets": 0,
        "pellet_delay": 0,
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
        "pixel_guy_rotation": ""
    }

    set_pre_level_variables(state)

    while True:
        set_loop_variables(state)

        game_display.fill(dirt_color)

        set_aiming_variables(state)

        event_handling(state)

        dont_let_go_off_screen(state)

        fire_pellet(state)

        melee(state)

        find_if_los(state)

        gun_zombies_shoot(state)

        zombie_decide_if_to_move(state)

        stop_stuff_at_wall(state)

        starting_move_timer(state)

        move_stuff(state)

        reload(state)

        pellet_hit_zombie(state)

        red_pellet_hit_guy(state)

        display_stuff(state)

        pygame.display.update()

        clock.tick(60)

        if state["current_room_cleared"]:
            if state["can_enter_right"]:
                if find_if_overlapping(state["pixel_guy_x"], state["pixel_guy_y"], pixel_guy_width, pixel_guy_height, display_width - 100, display_height / 2 - 50, 100, 100):
                    if pygame.key.get_pressed()[pygame.K_e]:
                        new_room(state["room"] + 1, state["room_list"][state["room"] + 1]["entered"], state, "left")
            elif state["can_enter_bottom"]:
                if find_if_overlapping(state["pixel_guy_x"], state["pixel_guy_y"], pixel_guy_width, pixel_guy_height, display_width / 2 - 50, display_height - 100, 100, 100):
                    if pygame.key.get_pressed()[pygame.K_e]:
                        new_room(state["room"] + 3, state["room_list"][state["room"] + 3]["entered"], state, "top")
            elif state["can_enter_left"]:
                if find_if_overlapping(state["pixel_guy_x"], state["pixel_guy_y"], pixel_guy_width, pixel_guy_height, 0, display_height / 2 - 50, 100, 100):
                    if pygame.key.get_pressed()[pygame.K_e]:
                        new_room(state["room"] - 1, state["room_list"][state["room"] - 1]["entered"], state, "right")
            elif state["can_enter_top"]:
                if find_if_overlapping(state["pixel_guy_x"], state["pixel_guy_y"], pixel_guy_width, pixel_guy_height, display_width / 2 - 50, 0, 100, 100):
                    if pygame.key.get_pressed()[pygame.K_e]:
                        new_room(state["room"] - 3, state["room_list"][state["room"] - 3]["entered"], state, "bottom")


new_level()
