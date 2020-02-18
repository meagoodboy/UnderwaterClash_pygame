import pygame
import random
import math
import os
import configparser

configparser = configparser.RawConfigParser()
configFilePath = os.path.join(os.path.dirname(__file__), 'myconfig.cfg')
configparser.read(configFilePath)
gameName = configparser.get("basicinfo", "name")
gaovt1 = configparser.get("gameoverinfo", "g1t")
gaovt2 = configparser.get("gameoverinfo", "g2t")
gaovt3 = configparser.get("gameoverinfo", "g3t")
gaovt4 = configparser.get("gameoverinfo", "g4t")
gaovt5 = configparser.get("gameoverinfo", "g5t")
gaovt6 = configparser.get("gameoverinfo", "g6t")
gaovt7 = configparser.get("gameoverinfo", "g7t")
gfont = configparser.get("basicinfo",  "gamefont")
gamelevel = configparser.get("basicinfo", "lvl")
sp = configparser.getint("basicinfo", "plsp")
speedobj = configparser.getfloat("basicinfo", "obsp")
colout_mutable = []
coloutlist = str(configparser.get("basicinfo", "black")).split(',')
for val in coloutlist:
    colout_mutable.append(int(val))
coloutb = tuple(colout_mutable)
colout_mutablew = []
coloutlistw = str(configparser.get("basicinfo", "white")).split(',')
for val in coloutlistw:
    colout_mutablew.append(int(val))
coloutw = tuple(colout_mutablew)

pygame.init()
runalways = 1
while runalways:
    gameoverfont = pygame.font.Font(gfont, 30)
    gameoverfont2 = pygame.font.Font(gfont, 64)
    scr_width = 1000
    scr_length = 840
    bgroundimage = pygame.image.load('editit.png')

    screen = pygame.display.set_mode((scr_width, scr_length))

    # game title
    pygame.display.set_caption(gameName)
    icon = pygame.image.load('diver.png')
    pygame.display.set_icon(icon)

    class playerdata:
        def __init__(
            self,
            pimage,
            pxcor,
            pycor,
            pmovx,
            pmovy,
            pmovs,
            plxmin,
            plxmax,
            plymin,
            plymax
        ):
            self.plimg = pimage
            self.plxico = pxcor
            self.plyico = pycor
            self.plmovx = pmovx
            self.plmovy = pmovy
            self.plspeed = pmovs
            self.xmin = plxmin
            self.ymin = plymin
            self.xmax = plxmax
            self.ymax = plymax
            self.lost = 0
            self.won = 0
            self.l1 = 0
            self.l2 = 0
            self.l3 = 0
            self.l4 = 0
            self.l5 = 0
            self.l6 = 0
            self.l7 = 0
            self.l8 = 0
            self.l9 = 0
            self.l10 = 0
            self.score = 0
            self.ptime = 0

        def resetp(self, xax, yax):
            plxico = xax
            plyico = yax
            plmovx = 0
            plmovy = 0
            self.l1 = 0
            self.l2 = 0
            self.l3 = 0
            self.l4 = 0
            self.l5 = 0
            self.l6 = 0
            self.l7 = 0
            self.l8 = 0
            self.l9 = 0
            self.l10 = 0

        def cals(self):
            self.score += (self.l1 + self.l2 + self.l3 + self.l4) * 5
            self.score += (self.l5 + self.l6 + self.l7) * 10
            self.score += (self.l8 + self.l9) * 10
            self.score += self.l10 * 20

        def playerbound(self):
            if self.plxico <= self.xmin:
                self.plxico = self.xmin
            if self.plxico >= self.xmax:
                self.plxico = self.xmax
            if self.plyico <= self.ymin:
                self.plyico = self.ymin
            if self.plyico >= self.ymax:
                self.plyico = self.ymax

        def pos_update(self):
            self.plxico += self.plmovx * self.plspeed
            self.plyico += self.plmovy * self.plspeed

        def screen_update(self):
            screen.blit(self.plimg, (self.plxico, self.plyico))

    crab = pygame.image.load('crab.png')
    octopus = pygame.image.load('octopus.png')
    dragon = pygame.image.load('dragon.png')
    crocodile = pygame.image.load('croc.png')
    shark = pygame.image.load('shark.png')
    pufferfish = pygame.image.load('animal.png')
    dead = pygame.image.load('death.png')

    stat_obj = [crab, octopus, pufferfish]

    # players
    player1image = pygame.image.load('submarine.png')
    player2image = pygame.image.load('submarine1.png')
    player1 = playerdata(player1image, 468, 736, 0, 0, sp, 0, 936, 40, 736)
    player2 = playerdata(player2image, 468, 40, 0, 0, sp, 0, 936, 40, 736)

    # start_time = pygame.time.get_ticks()
    # end_time = pygame.time.get_ticks()
    starttime = 0
    starttime = 0

    class moving_obj:
        def __init__(self, rndno, pos, xchan, speedo, start):
            self.objimg = rndno
            self.yaxis = pos
            self.speedob = speedo
            self.xchange = xchan
            self.xaxis = start

        def changespeed(self, newspeed):
            if newspeed > 0:
                self.xchange = newspeed
            else:
                self.xchange = 0.5

        def pos_updateo(self):
            self.xaxis += self.xchange * self.speedob

        def objectbound(self):
            if self.xaxis >= 1000:
                self.xaxis = 0

        def screen_updateo(self):
            screen.blit(self.objimg, (self.xaxis, self.yaxis))

    var = 0
    randomno1 = random.randint(0, 100)
    randomno2 = random.randint(0, 100)
    randomno3 = random.randint(0, 100)
    randomno4 = random.randint(0, 100)
    randomno5 = random.randint(0, 100)
    randomno6 = random.randint(0, 100)
    randomno1 %= 2
    randomno2 %= 2
    randomno3 %= 2
    randomno4 %= 2
    randomno5 %= 2
    randomno6 %= 2
    randomno1 += 1
    randomno2 += 1
    randomno3 += 1
    randomno4 += 1
    randomno5 += 1
    randomno6 += 1

    numb = 10
    numb1 = 6
    turn1 = 0
    turn2 = 0
    cox = 0
    cox2 = 0
    var1 = random.randint(0, 936)
    var2 = random.randint(0, 936)
    var3 = random.randint(0, 936)
    var4 = random.randint(0, 936)
    var5 = random.randint(0, 936)
    var6 = random.randint(0, 936)
    var7 = random.randint(0, 936)
    var8 = random.randint(0, 936)
    var8 = random.randint(0, 936)
    var9 = random.randint(0, 936)
    var10 = random.randint(0, 936)
    var11 = random.randint(0, 936)
    var12 = random.randint(0, 936)
    var13 = random.randint(0, 936)
    var14 = random.randint(0, 936)
    var15 = random.randint(0, 936)
    var16 = random.randint(0, 936)
    var17 = random.randint(0, 936)
    var18 = random.randint(0, 936)
    var19 = random.randint(0, 936)
    var20 = random.randint(0, 936)
    var21 = random.randint(0, 936)
    var22 = random.randint(0, 936)
    var23 = random.randint(0, 936)
    var24 = random.randint(0, 936)
# print(var2)
    object1 = moving_obj(crocodile, 104, speedobj, 2, -var3)
    object11 = moving_obj(crocodile, 104, speedobj, 1, -var13)
    object111 = moving_obj(crocodile, 104, speedobj, 2, -var23)
    object2 = moving_obj(shark, 239, speedobj, 3, -var5)
    object22 = moving_obj(shark, 239, speedobj, 3, -var15)
    object3 = moving_obj(dragon, 374, speedobj, 4, -var8)
    object33 = moving_obj(dragon, 374, speedobj, 3.5, -var18)
    object4 = moving_obj(shark, 509, speedobj, 3, -var1)
    object44 = moving_obj(shark, 509, speedobj, 3, -var11)
    object5 = moving_obj(crocodile, 644, speedobj, 2, -var20)
    object55 = moving_obj(crocodile, 644, speedobj, 1, -var17)
    object555 = moving_obj(crocodile, 644, speedobj, 2, -var24)

    start = 0
    player1time = 0
    # game main loop
    gamerun = True

    while gamerun:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill(coloutb)
        screen.blit(bgroundimage, (0, 40))
        if start == 0:

            gamestartf = pygame.font.Font(gfont, 64)
            gamestart = gamestartf.render(gameName, True, coloutw)
            screen.blit(gamestart, (150, 400))
            start = 1
            pygame.display.update()
            pygame.time.delay(3000)

        screen.blit(stat_obj[randomno1], (var1, 175))
        screen.blit(stat_obj[randomno2], (var2, 310))
        screen.blit(stat_obj[randomno3], (var3, 445))
        screen.blit(stat_obj[randomno4], (var4, 580))
        screen.blit(stat_obj[randomno1], (var5, 175))
        screen.blit(stat_obj[randomno2], (var6, 310))
        screen.blit(stat_obj[randomno3], (var7, 445))
        screen.blit(stat_obj[randomno4], (var8, 580))
        screen.blit(stat_obj[randomno1], (var9, 175))
        screen.blit(stat_obj[randomno2], (var10, 310))
        screen.blit(stat_obj[randomno3], (var11, 445))
        screen.blit(stat_obj[randomno4], (var12, 580))
        screen.blit(stat_obj[randomno1], (var13, 175))
        screen.blit(stat_obj[randomno2], (var14, 310))
        screen.blit(stat_obj[randomno3], (var15, 445))
        screen.blit(stat_obj[randomno4], (var16, 580))
        screen.blit(stat_obj[randomno1], (var17, 175))
        screen.blit(stat_obj[randomno2], (var18, 310))
        screen.blit(stat_obj[randomno3], (var19, 445))
        screen.blit(stat_obj[randomno4], (var20, 580))
        screen.blit(stat_obj[randomno1], (var21, 175))
        screen.blit(stat_obj[randomno2], (var22, 310))
        screen.blit(stat_obj[randomno3], (var23, 445))
        screen.blit(stat_obj[randomno4], (var24, 580))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        if player1.lost == 0 and (player1.won == 0 or player2.lost == 1):
            player1.ptime += 1
            gamespeed = turn1
            lvl = gameoverfont.render(
                gamelevel + str(turn1 + 1), True, coloutw)
            screen.blit(lvl, (500, 810))
            object1.changespeed(gamespeed)
            object11.changespeed(gamespeed)
            object111.changespeed(gamespeed)
            object2.changespeed(gamespeed)
            object22.changespeed(gamespeed)
            object3.changespeed(gamespeed)
            object33.changespeed(gamespeed)
            object4.changespeed(gamespeed)
            object44.changespeed(gamespeed)
            object5.changespeed(gamespeed)
            object55.changespeed(gamespeed)
            object555.changespeed(gamespeed)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1.plmovx = -0.1
                if event.key == pygame.K_RIGHT:
                    player1.plmovx = 0.1
                if event.key == pygame.K_UP:
                    player1.plmovy = -0.1
                if event.key == pygame.K_DOWN:
                    player1.plmovy = 0.1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player1.plmovx = 0
                if event.key == pygame.K_RIGHT:
                    player1.plmovx = 0
                if event.key == pygame.K_UP:
                    player1.plmovy = 0
                if event.key == pygame.K_DOWN:
                    player1.plmovy = 0

            if (
                pow(var1 - player1.plxico, 2) < 3000 and
                pow(175 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var2 - player1.plxico, 2) < 3000 and
                pow(310 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var3 - player1.plxico, 2) < 3000 and
                pow(445 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var4 - player1.plxico, 2) < 3000 and
                pow(580 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var5 - player1.plxico, 2) < 3000 and
                pow(175 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var6 - player1.plxico, 2) < 3000 and
                pow(310 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var7 - player1.plxico, 2) < 3000 and
                pow(445 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var8 - player1.plxico, 2) < 3000 and
                pow(580 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var9 - player1.plxico, 2) < 3000 and
                pow(175 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var10 - player1.plxico, 2) < 3000 and
                pow(310 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var11 - player1.plxico, 2) < 3000 and
                pow(445 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var12 - player1.plxico, 2) < 3000 and
                pow(580 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var13 - player1.plxico, 2) < 3000 and
                pow(175 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var14 - player1.plxico, 2) < 3000 and
                pow(310 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var15 - player1.plxico, 2) < 3000 and
                pow(445 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var16 - player1.plxico, 2) < 3000 and
                pow(580 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var17 - player1.plxico, 2) < 3000 and
                pow(175 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var18 - player1.plxico, 2) < 3000 and
                pow(310 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var19 - player1.plxico, 2) < 3000 and
                pow(445 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var20 - player1.plxico, 2) < 3000 and
                pow(580 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var21 - player1.plxico, 2) < 3000 and
                pow(175 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var22 - player1.plxico, 2) < 3000 and
                pow(310 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var23 - player1.plxico, 2) < 3000 and
                pow(445 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(var24 - player1.plxico, 2) < 3000 and
                pow(580 - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(object1.xaxis - player1.plxico, 2) < 3000 and
                pow(object1.yaxis - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(object11.xaxis - player1.plxico, 2) < 3000 and
                pow(object11.yaxis - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(object111.xaxis - player1.plxico, 2) < 3000 and
                pow(object111.yaxis - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(object2.xaxis - player1.plxico, 2) < 3000 and
                pow(object2.yaxis - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(object22.xaxis - player1.plxico, 2) < 3000 and
                pow(object22.yaxis - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(object3.xaxis - player1.plxico, 2) < 3000 and
                pow(object3.yaxis - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(object33.xaxis - player1.plxico, 2) < 3000 and
                pow(object33.yaxis - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(object4.xaxis - player1.plxico, 2) < 3000 and
                pow(object4.yaxis - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(object44.xaxis - player1.plxico, 2) < 3000 and
                pow(object44.yaxis - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(object5.xaxis - player1.plxico, 2) < 3000 and
                pow(object5.yaxis - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(object55.xaxis - player1.plxico, 2) < 3000 and
                pow(object55.yaxis - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if (
                pow(object555.xaxis - player1.plxico, 2) < 3000 and
                pow(object55.yaxis - player1.plyico, 2) < 3000
            ):
                player1.lost = 1
            if player1.plyico < 580:
                player1.l1 = 1
            if player1.plyico < 445:
                player1.l2 = 1
            if player1.plyico < 310:
                player1.l3 = 1
            if player1.plyico < 175:
                player1.l4 = 1
            if player1.plyico < 644:
                player1.l5 = 1
            if player1.plyico < 509:
                player1.l6 = 1
            if player1.plyico < 374:
                player1.l7 = 1
            if player1.plyico < 239:
                player1.l8 = 1
            if player1.plyico < 104:
                player1.l9 = 1

            if player1.lost == 1:
                #    print('LOST')
                player1.plxico = 468
                player1.plyico = 736
                player1.plmovy = 0
                player1.plmovx = 0
                player2.won = 0
                player1.plimg = dead
                player1.cals()
                pygame.time.delay(1000)
                player1.screen_update()
                player2.screen_update()

            if player1.plyico == 40:
                #    print('won')
                player1.l10 = 1
                player1.plxico = 468
                player1.plyico = 736
                player1.plmovy = 0
                player1.plmovx = 0
                player1.won = 1
                player2.won = 0
                turn1 += 1
                player1.cals()
                pygame.time.delay(1000)
                player1.screen_update()
                player2.screen_update()
                player1.resetp(468, 736)

        elif player2.lost == 0 and (player1.lost == 1 or player1.won == 1):
            # player2 movements
            player2.ptime += 1
            gamespeed = turn2
            lvl = gameoverfont.render(
                gamelevel + str(turn2 + 1), True, coloutw)
            screen.blit(lvl, (500, 10))
            object1.changespeed(gamespeed)
            object11.changespeed(gamespeed)
            object111.changespeed(gamespeed)
            object2.changespeed(gamespeed)
            object22.changespeed(gamespeed)
            object3.changespeed(gamespeed)
            object33.changespeed(gamespeed)
            object4.changespeed(gamespeed)
            object44.changespeed(gamespeed)
            object5.changespeed(gamespeed)
            object55.changespeed(gamespeed)
            object555.changespeed(gamespeed)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player2.plmovx = -0.1
                if event.key == pygame.K_d:
                    player2.plmovx = 0.1
                if event.key == pygame.K_w:
                    player2.plmovy = -0.1
                if event.key == pygame.K_s:
                    player2.plmovy = 0.1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player2.plmovx = 0
                if event.key == pygame.K_d:
                    player2.plmovx = 0
                if event.key == pygame.K_w:
                    player2.plmovy = 0
                if event.key == pygame.K_s:
                    player2.plmovy = 0

            if (
                pow(var1 - player2.plxico, 2) < 3000 and
                pow(175 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var2 - player2.plxico, 2) < 3000 and
                pow(310 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var3 - player2.plxico, 2) < 3000 and
                pow(445 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var4 - player2.plxico, 2) < 3000 and
                pow(580 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var5 - player2.plxico, 2) < 3000 and
                pow(175 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var6 - player2.plxico, 2) < 3000 and
                pow(310 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var7 - player2.plxico, 2) < 3000 and
                pow(445 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var8 - player2.plxico, 2) < 3000 and
                pow(580 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var9 - player2.plxico, 2) < 3000 and
                pow(175 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var10 - player2.plxico, 2) < 3000 and
                pow(310 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var11 - player2.plxico, 2) < 3000 and
                pow(445 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var12 - player2.plxico, 2) < 3000 and
                pow(580 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var13 - player2.plxico, 2) < 3000 and
                pow(175 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var14 - player2.plxico, 2) < 3000 and
                pow(310 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var15 - player2.plxico, 2) < 3000 and
                pow(445 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1

            if (
                pow(var16 - player2.plxico, 2) < 3000 and
                pow(580 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var17 - player2.plxico, 2) < 3000 and
                pow(175 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var18 - player2.plxico, 2) < 3000 and
                pow(310 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var19 - player2.plxico, 2) < 3000 and
                pow(445 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var20 - player2.plxico, 2) < 3000 and
                pow(580 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var21 - player2.plxico, 2) < 3000 and
                pow(175 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var22 - player2.plxico, 2) < 3000 and
                pow(310 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var23 - player2.plxico, 2) < 3000 and
                pow(445 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(var24 - player2.plxico, 2) < 3000 and
                pow(580 - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(object1.xaxis - player2.plxico, 2) < 3000 and
                pow(object1.yaxis - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(object11.xaxis - player2.plxico, 2) < 3000 and
                pow(object11.yaxis - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(object111.xaxis - player2.plxico, 2) < 3000 and
                pow(object111.yaxis - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(object2.xaxis - player2.plxico, 2) < 3000 and
                pow(object2.yaxis - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(object22.xaxis - player2.plxico, 2) < 3000 and
                pow(object22.yaxis - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(object3.xaxis - player2.plxico, 2) < 3000 and
                pow(object3.yaxis - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(object33.xaxis - player2.plxico, 2) < 3000 and
                pow(object33.yaxis - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(object4.xaxis - player2.plxico, 2) < 3000 and
                pow(object4.yaxis - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(object44.xaxis - player2.plxico, 2) < 3000 and
                pow(object44.yaxis - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(object5.xaxis - player2.plxico, 2) < 3000 and
                pow(object5.yaxis - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(object55.xaxis - player2.plxico, 2) < 3000 and
                pow(object55.yaxis - player2.plyico, 2) < 3000
            ):
                player2.lost = 1
            if (
                pow(object555.xaxis - player2.plxico, 2) < 3000 and
                pow(object55.yaxis - player2.plyico, 2) < 3000
            ):
                player2.lost = 1

            if player2.plyico > 580:
                player2.l1 = 1
            if player2.plyico > 445:
                player2.l2 = 1
            if player2.plyico > 310:
                player2.l3 = 1
            if player2.plyico > 175:
                player2.l4 = 1
            if player2.plyico > 644:
                player2.l5 = 1
            if player2.plyico > 509:
                player2.l6 = 1
            if player2.plyico > 374:
                player2.l7 = 1
            if player2.plyico > 239:
                player2.l8 = 1
            if player2.plyico > 104:
                player2.l9 = 1

            if player2.lost == 1:
                #            print('LOST')
                player2.plxico = 468
                player2.plyico = 40
                player2.plmovy = 0
                player2.plmovx = 0
                player1.won = 0
                player2.plimg = dead
                pygame.time.delay(1000)
                player1.screen_update()
                player2.screen_update()
                player2.cals()

            if player2.plyico == 736:
                player2.plxico = 468
                player2.plyico = 40
                player2.plmovy = 0
                player2.plmovx = 0
                player2.won = 1
                player1.won = 0
                turn2 += 1
                player2.l10 = 1
                pygame.time.delay(1000)
                player1.screen_update()
                player2.screen_update()
                player2.cals()
                player2.resetp(468, 40)

        if player1.lost == 1 and player2.lost == 1:
            break

        if player2.lost == 1 and player1.won == 1:
            player1.won == 0
            player1.resetp(468, 736)

        if player1.lost == 1 and player2.won == 1:
            player2.won == 0
            player2.resetp(468, 40)

        player1.pos_update()
        player2.pos_update()
        object1.pos_updateo()
        object11.pos_updateo()
        object111.pos_updateo()
        object2.pos_updateo()
        object22.pos_updateo()
        object3.pos_updateo()
        object33.pos_updateo()
        object4.pos_updateo()
        object44.pos_updateo()
        object5.pos_updateo()
        object55.pos_updateo()
        object555.pos_updateo()

    # player movement boundary
        player1.playerbound()
        player2.playerbound()
        object1.objectbound()
        object11.objectbound()
        object111.objectbound()
        object2.objectbound()
        object22.objectbound()
        object3.objectbound()
        object33.objectbound()
        object4.objectbound()
        object44.objectbound()
        object5.objectbound()
        object55.objectbound()
        object555.objectbound()

# player1 position update
        player1.screen_update()
        player2.screen_update()
        object1.screen_updateo()
        object11.screen_updateo()
        object111.screen_updateo()
        object2.screen_updateo()
        object22.screen_updateo()
        object3.screen_updateo()
        object33.screen_updateo()
        object4.screen_updateo()
        object44.screen_updateo()
        object5.screen_updateo()
        object55.screen_updateo()
        object555.screen_updateo()
        pygame.display.update()

    gameoverimage = pygame.image.load('gameover.jpg')
    while gamerun:
        screen.blit(gameoverimage, (0, 40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        player1.score -= player1.ptime/1000
        player2.score -= player2.ptime/1000
        gameover = gameoverfont.render(
            gaovt1 + str(player1.score), True, coloutw)
        screen.blit(gameover, (0, 810))
        gameover2 = gameoverfont.render(
            gaovt2 + str(player2.score), True, coloutw)
        screen.blit(gameover2, (500, 810))
        gameover3 = gameoverfont2.render(gaovt3, True, coloutw)
        screen.blit(gameover3, (200, 300))
        if player1.score > player2.score:
            gameover4 = gameoverfont2.render(gaovt4, True, coloutw)
        elif player1.score == player2.score:
            gameover4 = gameoverfont2.render(gaovt5, True, coloutw)
        else:
            gameover4 = gameoverfont2.render(gaovt6, True, coloutw)
        screen.blit(gameover4, (300, 400))

        pygame.display.update()
        pygame.time.delay(3000)
        breakval = 0
        while gamerun:
            gameover5 = gameoverfont.render(gaovt7, True, coloutw)
            screen.blit(gameover5, (650, 700))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        breakval = 1
                        break
                        gamerun = 0
                    if event.key == pygame.K_n:
                        quit()
            if breakval == 1:
                break
        if breakval == 1:
            break
