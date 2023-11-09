import pygame
import sys

pygame.init()

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def restart_game():
    global player_lives, mario_x, mario_y, jumping, jump_direction, game_over, player_won
    player_lives = 3
    life_positions.clear()
    life_positions.extend([(800 + i * 35, 20) for i in range(player_lives)])

    mario_x = 820
    mario_y = 670
    jumping = False
    jump_direction = 1

    game_over = False
    player_won = False

player_lives=3
life_positions = [(800 + i * 35, 20) for i in range(player_lives)]

width = 1000
height = 770
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game Frame")

life_icon = pygame.image.load("lives.png")
life_icon = pygame.transform.scale(life_icon, (30, 30))

background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (width, height))
background_rect = background_image.get_rect()

victory=pygame.image.load("victory.png")
victory1 = pygame.transform.scale(victory, (width-200, height - 200))
victory_rect = victory1.get_rect()

barr = pygame.image.load("barrel2.png")
new_barr_width = 50
new_barr_height = 50
barr = pygame.transform.scale(barr, (new_barr_width, new_barr_height))

kong = pygame.image.load("dk3.png")
newkongw = 100
newkongh = 100
kong = pygame.transform.scale(kong, (newkongw, newkongh))

peach = pygame.image.load("peach1.png")
newp = 60
newph = 100
peach = pygame.transform.scale(peach, (newp, newph))

mario = pygame.image.load("standing.png")
m1 = 40
m2 = 75
mario = pygame.transform.scale(mario, (m1, m2))

roll = pygame.image.load("barrel.png")
m12 = 60
m22 = 40
rollu = pygame.transform.scale(roll, (m12, m22))

ladd = pygame.image.load("ladder.png")
newla = 100
newlh = 185
ladd = pygame.transform.scale(ladd, (newla, newlh))

newlaw = 100
newlhh = 170
ladder = pygame.transform.scale(ladd, (newlaw, newlhh))

lw = 100
lh = 150
ladd2 = pygame.transform.scale(ladd, (lw, lh))

num_bridges = 5
bridge_width = 150

flame= pygame.image.load("fireballdown.png")
flame1 = pygame.transform.scale(flame,(30,30))

border_part_image = pygame.image.load("plat2.png")
border1_part_image = pygame.image.load("plat.png")

border_tile_width = border_part_image.get_width()
border_tile_height = border_part_image.get_height()

border1_tile_width = border1_part_image.get_width()
border1_tile_height = border1_part_image.get_height()

tryagain=pygame.image.load("tryagain.png")
try1=pygame.transform.scale(tryagain, (100, 100))
trypos=(700, 500)

next=pygame.image.load("next.png")
next1=pygame.transform.scale(next, (100, 100))
nextpos=(700, 500)

num_horizontal_repeats = width // border_tile_width
num_vertical_repeats = height // border1_tile_height

left_frame_x = 0
right_frame_x = width - border_tile_width
bottom_frame_y = height - border1_tile_height

small_bridge_part_image = pygame.image.load("plat.png")

barrel_x = 455
barrel_y = 225

jumping = False
jump_count = 8
jump_direction = 1

mario_x = 820
mario_y = 670
climbing = False

player_won = False

gover=pygame.image.load("gameover.png")
game_rect = gover.get_rect(center=(width // 2, height // 2 - 50))

ladders = [(400, 115), (780, 250), (110, 370), (800, 485), (200, 610)]
barrels=[(455,225),(330,345),(700,464),(310,580),(670,695)]
flames=[(710,230),(570,345),(220,464),(550,585),(100,695)]

x_position = 25
x1 = 120
game_over= False

flames_x,flames_y=650,225

running = True

while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if trypos[0] <= event.pos[0] <= trypos[0] + tryagain.get_width() and \
                    trypos[1] <= event.pos[1] <= trypos[1] + tryagain.get_height():
                restart_game()
                game_over = False
        elif player_won and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if nextpos[0] <= event.pos[0] <= nextpos[0] + next1.get_width() and \
                nextpos[1] <= event.pos[1] <= nextpos[1] + next1.get_height():
                restart_game()
                player_won = False

    if player_lives <= 0:
        game_over = True


    if not game_over:
        keys = pygame.key.get_pressed()
    
    for barrel_x, barrel_y in barrels:
        barrel_rect = pygame.Rect(barrel_x, barrel_y, m12, m22)
        player_rect = pygame.Rect(mario_x, mario_y, m1, m2)

        if check_collision(player_rect, barrel_rect) and mario_y < barrel_y:
            player_lives -= 1
            life_positions.pop()
            mario_x = 820
            mario_y = 670
            jumping = False
            jump_direction=1

    for flames_x, flames_y in flames:
        flame_rect = pygame.Rect(flames_x, flames_y, flame1.get_width(), flame1.get_height())

        if check_collision(player_rect, flame_rect):
            player_lives -= 1
            life_positions.pop()
            mario_x = 820
            mario_y = 670
            jumping = False
            jump_direction=1

    near_ladder = False
    for ladder_x, ladder_y in ladders:
        if (
            ladder_x - m1 < mario_x < ladder_x + newlaw
            and ladder_y - m2 < mario_y < ladder_y + newlhh
        ):
            near_ladder = True
            break

    if near_ladder and keys[pygame.K_UP]:
        climbing = True

        mario_x = ladder_x
        mario_y -= 3
    elif near_ladder and keys[pygame.K_DOWN]:
        climbing = True
        mario_x = ladder_x
        mario_y += 3
    else:
        climbing = False

        if keys[pygame.K_LEFT]:
            
            if mario_x > left_frame_x:
                mario_x -= 3

        if keys[pygame.K_RIGHT]:
            
            if mario_x < right_frame_x:
                mario_x += 3

        if keys[pygame.K_DOWN]:
            
            if mario_y < bottom_frame_y:
                mario_y += 3

    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
            if keys[pygame.K_LEFT]:
                jump_direction = -1
            elif keys[pygame.K_RIGHT]:
                jump_direction = 1

    if jumping:
        if jump_count >= -8:
            neg = 1
            if jump_count < 0:
                neg = -1
            mario_x += jump_direction * 7
            mario_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 8
            jump_direction = 1

    if check_collision(player_rect, (320, 30, newp, newph)):
        player_won = True

    screen.fill((0, 0, 0))
    screen.blit(background_image, background_rect)

    for x in range(num_horizontal_repeats):
        screen.blit(border1_part_image, (x * border_tile_width, height - border1_tile_height))

    for x in range(num_horizontal_repeats):
        screen.blit(border1_part_image, (300, 130))

    for y in range(num_vertical_repeats):
        screen.blit(border_part_image, (0, y * border1_tile_height))
        screen.blit(border_part_image, (width - border_tile_width, y * 18))

    num_bridge_parts = 10
    angle_in_degrees = 1
    top1 = 250
    y_position_top = 360
    ymid = 490
    ymid1 = 600
    y_position_bottom = 720

    horizontal_offset = small_bridge_part_image.get_width()
    vertical_offset = int(horizontal_offset * (1 / abs(angle_in_degrees)))

    bridge_width = num_bridge_parts * (horizontal_offset - 55)
    bridge_width1 = num_bridge_parts * horizontal_offset

    bridge_surface = pygame.Surface((bridge_width, vertical_offset), pygame.SRCALPHA)
    bridge_surface1 = pygame.Surface((bridge_width1, vertical_offset), pygame.SRCALPHA)

    for i in reversed(range(num_bridge_parts)):
        small_bridge_part_rotated = pygame.transform.rotate(small_bridge_part_image, angle_in_degrees)
        bridge_surface.blit(small_bridge_part_rotated, (i * (horizontal_offset - 60), 0))
        bridge_surface1.blit(small_bridge_part_rotated, (i * horizontal_offset, 0))

    b1 = pygame.transform.rotate(bridge_surface, -angle_in_degrees)
    b2 = pygame.transform.rotate(bridge_surface1, angle_in_degrees)
    b3 = pygame.transform.rotate(bridge_surface, -angle_in_degrees)
    b4 = pygame.transform.rotate(bridge_surface1, angle_in_degrees)
    b5 = pygame.transform.rotate(bridge_surface1, -angle_in_degrees)

    screen.blit(b1, (x_position, top1))
    screen.blit(b2, (x1, y_position_top))
    screen.blit(b3, (x_position, ymid))
    screen.blit(b4, (x1, ymid1))
    screen.blit(b5, (x_position, y_position_bottom))

    screen.blit(barr, (30, 210))
    screen.blit(barr, (30, 178))
    
    screen.blit(peach, (320, 30))
    screen.blit(kong, (90, 155))

    screen.blit(ladder, (400, 115))
    screen.blit(ladder, (780, 250))

    screen.blit(ladder, (115, 370))
    screen.blit(ladder, (800, 485))
    screen.blit(ladder, (200, 610))

    screen.blit(mario, (mario_x, mario_y))
    for barrel_x, barrel_y in barrels:
        screen.blit(rollu, (barrel_x, barrel_y))

    for flames_x, flames_y in flames:
        screen.blit(flame1, (flames_x,flames_y))

    for x, y in life_positions:
        screen.blit(life_icon, (x, y))

    if game_over:
        screen.blit(gover, game_rect)
        screen.blit(try1, trypos)

    if player_won:
        screen.blit(victory1, (100, 100))
        screen.blit(next1, nextpos)

    pygame.display.flip()

pygame.quit()
sys.exit()