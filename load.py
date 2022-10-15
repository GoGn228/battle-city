import pygame
player_image=[pygame.image.load("image/player/player 1.png").convert_alpha(),
              pygame.image.load("image/player/player 2.png").convert_alpha()]
player_bullet=pygame.image.load("image/player/player bullet.png").convert_alpha()
enemy_image=pygame.image.load("image/enemy/enemy.png").convert_alpha()
enemy_bullet=pygame.image.load("image/enemy/enemy bullet.png").convert_alpha()
brick_image=pygame.image.load("image/blocks/brick block.png").convert_alpha()
iron_image=pygame.image.load("image/blocks/iron block.png").convert_alpha()
bush_image=pygame.image.load("image/blocks/bush block.png").convert_alpha()
water_image=pygame.image.load("image/blocks/water block.png").convert_alpha()
flag_image=pygame.image.load("image/blocks/flag.png").convert_alpha()
start_image=pygame.image.load("image/dop/start.png").convert_alpha()
exit_image=pygame.image.load("image/dop/exit.png").convert_alpha()
records_image=pygame.image.load("image/dop/records.png").convert_alpha()
menu_image=pygame.image.load("image/dop/fon.png").convert_alpha()
back_image=pygame.image.load("image/dop/back.png").convert_alpha()
bullet_image=[pygame.image.load("image/dop/1.png").convert_alpha(),
              pygame.image.load("image/dop/2.png").convert_alpha(),
              pygame.image.load("image/dop/3.png").convert_alpha(),
              pygame.image.load("image/dop/4.png").convert_alpha()]
shot_sound=pygame.mixer.Sound("sound/shot.mp3")
boom_sound=pygame.mixer.Sound("sound/boom.mp3")
