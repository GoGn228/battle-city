import pygame
import os
import sys
import random

file=r'sound/tanchiki-tanchiki-mp3.mp3'
pygame.mixer.init()
track = pygame.mixer.music.load(file)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
pygame.font.init()
pygame.init()
current_path=os.path.dirname(__file__)
os.chdir(current_path)
WIDTH=1200
HEIGHT=800
FPS=60
record=0
sc=pygame.display.set_mode((WIDTH, HEIGHT))
clock=pygame.time.Clock()
lvl="menu"

from load import *


def startMenu():
    global lvl
    sc.blit(menu_image, (0, 0))
    sc.blit(start_image, (100, 200))
    sc.blit(records_image, (100, 300))
    sc.blit(exit_image, (100, 400))
    pos_mouse=pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if 100<pos_mouse[0]<400:
            if 200<pos_mouse[1]<275:
                restart()
                drawMaps("1.txt")
                lvl="Game"
            elif 300<pos_mouse[1]<375:
                lvl="record"
                sc.fill("black")
                f1 = pygame.font.Font(None, 36)
                text1 = f1.render("Ваш рекорд: 0", 1, (180, 180, 180))
                sc.blit(text1, (500, 400))
                sc.blit(back_image, (1100, 50))
                pos_mouse_2 = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0]:
                    if 1100 < pos_mouse_2[1] < 1150:
                        print("jnkm")
                        if 50 < pos_mouse_2[1] < 100:
                            lvl="menu"
                            print("hdvbn")
            elif 400<pos_mouse[1]<475:
                pygame.quit()
                sys.exit()
    pygame.display.update()

def lvlGame():
    sc.fill("black")
    brick_group.update()
    brick_group.draw(sc)
    iron_group.update()
    iron_group.draw(sc)
    water_group.update()
    water_group.draw(sc)
    enemy_group.update()
    enemy_group.draw(sc)
    player_group.update()
    player_group.draw(sc)
    flag_group.update()
    flag_group.draw(sc)
    bullet_player_group.update()
    bullet_player_group.draw(sc)
    bullet_enemy_group.update()
    bullet_enemy_group.draw(sc)
    bush_group.update()
    bush_group.draw(sc)
    pygame.display.update()

def drawMaps(nameFile):
    maps=[]
    source="maps/" + str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 20):
            maps.append(file.readline().replace("\n", "").split(",")[0:-1])

    pos=[0, 0]
    for i in range(0, len(maps)):
        pos[1] = i *40
        for j in range(0, len(maps[0])):
           pos[0]=40 * j
           if maps[i][j]=="1":
              brick=Brick(brick_image, pos)
              brick_group.add(brick)
           elif maps[i][j]=="2":
              bush=Bush(bush_image, pos)
              bush_group.add(bush)
           elif maps[i][j]=="4":
              iron=Iron(iron_image, pos)
              iron_group.add(iron)
           elif maps[i][j]=="5":
              water=Water(water_image, pos)
              water_group.add(water)
           elif maps[i][j] == "6":
               enemy = Enemy(enemy_image, pos)
               enemy_group.add(enemy)
           elif maps[i][j]=="3":
              flag=Flag(flag_image, pos)
              flag_group.add(flag)



class Brick(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y=pos[1]
    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if player.dir=="left":
                player.rect.left=self.rect.right
            elif player.dir=="right":
                player.rect.right=self.rect.left
            elif player.dir=="up":
                player.rect.top=self.rect.bottom
            elif player.dir=="down":
                player.rect.bottom=self.rect.top
        pygame.sprite.groupcollide(bullet_player_group, brick_group, True, True)
        pygame.sprite.groupcollide(bullet_enemy_group, brick_group, True, True)

class Bush(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

class Iron(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if player.dir=="left":
                player.rect.left=self.rect.right
            elif player.dir=="right":
                player.rect.right=self.rect.left
            elif player.dir=="up":
                player.rect.top=self.rect.bottom
            elif player.dir=="down":
                player.rect.bottom=self.rect.top
        pygame.sprite.groupcollide(bullet_player_group, iron_group, True, False)
        pygame.sprite.groupcollide(bullet_enemy_group, iron_group, True, False)

class Water(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if player.dir=="left":
                player.rect.left=self.rect.right
            elif player.dir=="right":
                player.rect.right=self.rect.left
            elif player.dir=="up":
                player.rect.top=self.rect.bottom
            elif player.dir=="down":
                player.rect.bottom=self.rect.top

class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.speed=5
        self.dir="top"
        self.timer_shot=0
        self.frame=0
        self.timer_anime=0
        self.anime=False

    def update(self):
        self.anime = False
        self.timer_shot+=1
        key=pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.timer_shot>40:
            bullet=Bullet_player(player_bullet, self.rect.center, self.dir)
            bullet_player_group.add(bullet)
            self.timer_shot=0
            shot_sound.play()
        if key[pygame.K_a]:
            self.image=pygame.transform.rotate(player_image[self.frame], 90)
            self.rect.x-=self.speed
            self.dir="left"
            self.anime = True
        elif key[pygame.K_d]:
            self.image=pygame.transform.rotate(player_image[self.frame], -90)
            self.rect.x+=self.speed
            self.dir="right"
            self.anime = True
        elif key[pygame.K_w]:
            self.image=pygame.transform.rotate(player_image[self.frame], 0)
            self.rect.y-=self.speed
            self.dir="up"
            self.anime = True
        elif key[pygame.K_s]:
            self.image=pygame.transform.rotate(player_image[self.frame], 180)
            self.rect.y+=self.speed
            self.dir="down"
            self.anime = True
        if self.anime:
            self.timer_anime+=1
            if self.timer_anime/FPS>0.1:
                if self.frame==len(player_image)-1:
                    self.frame=0
                else:
                    self.frame+=1
                self.timer_anime=0
        if pygame.sprite.groupcollide(bullet_enemy_group, player_group, True, True):
            global lvl
            lvl="menu"

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.speed=1
        self.dir="up"
        self.timer_move=0
        self.timer_shot = 0

    def update(self):
        self.timer_move += 1
        self.timer_shot += 1
        if self.timer_shot/FPS>2:
            bullet_enemy = Bullet_enemy(enemy_bullet, self.rect.center, self.dir)
            bullet_enemy_group.add(bullet_enemy)
            self.timer_shot = 0
        if self.timer_move/FPS>2:
            if random.randint(1, 4)==1:
                self.dir="up"
            elif random.randint(1, 4)==2:
                self.dir="down"
            elif random.randint(1, 4)==3:
                self.dir="left"
            elif random.randint(1, 4)==4:
                self.dir="right"
            self.timer_move = 0
        if self.dir=="up":
            self.image=pygame.transform.rotate(enemy_image, 0)
            self.rect.y-=self.speed
        elif self.dir=="down":
            self.image=pygame.transform.rotate(enemy_image, 180)
            self.rect.y+=self.speed
        elif self.dir=="left":
            self.image=pygame.transform.rotate(enemy_image, 90)
            self.rect.x-=self.speed
        elif self.dir=="right":
            self.image=pygame.transform.rotate(enemy_image, -90)
            self.rect.x+=self.speed
        if pygame.sprite.spritecollide(self, brick_group, False):
            self.timer_move=0
            if self.dir=="up":
                self.dir="down"
            elif self.dir=="down":
                self.dir="up"
            elif self.dir=="left":
                self.dir="right"
            elif self.dir=="right":
                self.dir="left"
        elif pygame.sprite.spritecollide(self, iron_group, False):
            self.timer_move=0
            if self.dir=="up":
                self.dir="down"
            elif self.dir=="down":
                self.dir="up"
            elif self.dir=="left":
                self.dir="right"
            elif self.dir=="right":
                self.dir="left"
        elif pygame.sprite.spritecollide(self, water_group, False):
            self.timer_move=0
            if self.dir=="up":
                self.dir="down"
            elif self.dir=="down":
                self.dir="up"
            elif self.dir=="left":
                self.dir="right"
            elif self.dir=="right":
                self.dir="left"

class Bullet_player(pygame.sprite.Sprite):
    def __init__(self, image, pos, dir):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.speed=5
        self.dir=dir
        self.anime=False
        self.timer_anime=0
        self.frame=0
        self.boom=False

    def update(self):
        if self.dir=="up":
            self.rect.y -= self.speed
        elif self.dir=="down":
            self.rect.y += self.speed
        elif self.dir=="right":
            self.rect.x += self.speed
        elif self.dir=="left":
            self.rect.x -= self.speed
        if pygame.sprite.spritecollide(self, enemy_group, True):
            global record
            self.anime=True
            self.speed=0
            self.boom = True
            record+=1
        if self.anime:
            self.timer_anime+=1
            if self.timer_anime/FPS>0.1:
                if self.frame==len(bullet_image)-1:
                    self.frame=0
                    self.rect.center=(-1000, 0)
                    self.kill()
                else:
                    self.frame+=1
                self.timer_anime=0
            self.image=bullet_image[self.frame]
        if self.boom:
            boom_sound.play()
            self.boom=False

class Bullet_enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos, dir):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.speed=5
        self.dir=dir

    def update(self):
        if self.dir=="up":
            self.rect.y -= self.speed
        elif self.dir=="down":
            self.rect.y += self.speed
        elif self.dir=="right":
            self.rect.x += self.speed
        elif self.dir=="left":
            self.rect.x -= self.speed

class Flag(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
    def update(self):
        global lvl
        if pygame.sprite.groupcollide(bullet_player_group, flag_group, True, True):
            lvl="menu"
        if pygame.sprite.groupcollide(bullet_enemy_group, flag_group, True, True):
            lvl="menu"

class restart():
    global bullet_enemy_group
    global water_group, brick_group, bush_group, iron_group
    global player_group, enemy_group, flag_group, bullet_player_group, player
    brick_group = pygame.sprite.Group()
    bush_group = pygame.sprite.Group()
    iron_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    flag_group = pygame.sprite.Group()
    bullet_player_group = pygame.sprite.Group()
    bullet_enemy_group = pygame.sprite.Group()
    player=Player(player_image[0], (400, 640))
    player_group.add(player)






while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    if lvl=="Game":
        lvlGame()
    elif lvl=="menu":
        startMenu()
    clock.tick(FPS)