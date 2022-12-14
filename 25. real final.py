import pygame, sys, math, random
from pygame.locals import *

# pygame set up
pygame.init()
mainClock = pygame.time.Clock()

# window set up
WINDOWWIDTH = 700
WINDOWHEIGHT = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Input')
basicFont1 = pygame.font.SysFont('Agency FB', 80)
basicFont2 = pygame.font.SysFont('Agency FB', 60)
basicFont3 = pygame.font.SysFont('Arial', 30)

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)
SKYBLUE = (0, 255, 255)
SHIELD = (128, 128, 255)
COLOR0 = (138, 231, 168)
COLOR1 = (0, 255, 255)
COLOR2 = (233, 106, 192)
COLOR3 = (127, 16, 181)
COLOR4 = (245, 104, 37)
COLOR5 = (0, 255, 0)
COLOR6 = (80, 80, 80)
COLOR7 = (28, 61, 98)
ORANGE = (238, 180, 73)

# set up the player and bullet data structure
SPEED = 75
SIZE1 = 50
SIZE2 = 50
ITEMSIZE = 40
ITEMCOUNTER = 0
ITEMTIME = SPEED*5
SELECTITEM = 0
BULLETSIZE = 30
player1 = pygame.Rect(int(WINDOWWIDTH/4)-25, int(WINDOWHEIGHT/2)-25, SIZE1, SIZE1)
player2 = pygame.Rect(int(WINDOWWIDTH/4*3)-25, int(WINDOWHEIGHT/2)-25, SIZE2, SIZE2)
showitem = pygame.Rect(240, 190, 220, 220)
goback = pygame.Rect(600, 50, 50, 50)
itemselect = pygame.Rect(65, 100, 560, 500)
iteminfo = pygame.Rect(327.5, 505, 45, 45)

playerImage1ou = pygame.image.load('icon1_open(u).png')
playerImage1od = pygame.image.load('icon1_open(d).png')
playerImage1or = pygame.image.load('icon1_open(r).png')
playerImage1ol = pygame.image.load('icon1_open(l).png')

playerImage1cu = pygame.image.load('icon1_close(u).png')
playerImage1cd = pygame.image.load('icon1_close(d).png')
playerImage1cr = pygame.image.load('icon1_close(r).png')
playerImage1cl = pygame.image.load('icon1_close(l).png')

playerImage2ou = pygame.image.load('icon2_open(u).png')
playerImage2od = pygame.image.load('icon2_open(d).png')
playerImage2or = pygame.image.load('icon2_open(r).png')
playerImage2ol = pygame.image.load('icon2_open(l).png')

playerImage2cu = pygame.image.load('icon2_close(u).png')
playerImage2cd = pygame.image.load('icon2_close(d).png')
playerImage2cr = pygame.image.load('icon2_close(r).png')
playerImage2cl = pygame.image.load('icon2_close(l).png')

bulletImagei = pygame.image.load('ice_magic.png')
bulletStretchedImagei = pygame.transform.scale(bulletImagei, (BULLETSIZE, BULLETSIZE))

bulletImage11 = pygame.image.load('bulletup3.png')
bulletStretchedImage11 = pygame.transform.scale(bulletImage11, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImage12 = pygame.image.load('bulletdown3.png')
bulletStretchedImage12 = pygame.transform.scale(bulletImage12, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImage13 = pygame.image.load('bulletleft3.png')
bulletStretchedImage13 = pygame.transform.scale(bulletImage13, (BULLETSIZE,int(BULLETSIZE*2/3)))
bulletImage14 = pygame.image.load('bulletright3.png')
bulletStretchedImage14 = pygame.transform.scale(bulletImage14, (BULLETSIZE,int(BULLETSIZE*2/3)))

bulletImage21 = pygame.image.load('bulletup2.png')
bulletStretchedImage21 = pygame.transform.scale(bulletImage21, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImage22 = pygame.image.load('bulletdown2.png')
bulletStretchedImage22 = pygame.transform.scale(bulletImage22, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImage23 = pygame.image.load('bulletleft2.png')
bulletStretchedImage23 = pygame.transform.scale(bulletImage23, (BULLETSIZE,int(BULLETSIZE*2/3)))
bulletImage24 = pygame.image.load('bulletright2.png')
bulletStretchedImage24 = pygame.transform.scale(bulletImage24, (BULLETSIZE,int(BULLETSIZE*2/3)))

bulletImagec11 = pygame.image.load('firecrashup1.png')
bulletStretchedImagec11 = pygame.transform.scale(bulletImagec11, (BULLETSIZE, BULLETSIZE))
bulletImagec12 = pygame.image.load('firecrashdown1.png')
bulletStretchedImagec12 = pygame.transform.scale(bulletImagec12, (BULLETSIZE, BULLETSIZE))
bulletImagec13 = pygame.image.load('firecrashleft1.png')
bulletStretchedImagec13 = pygame.transform.scale(bulletImagec13, (BULLETSIZE, BULLETSIZE))
bulletImagec14 = pygame.image.load('firecrashright1.png')
bulletStretchedImagec14 = pygame.transform.scale(bulletImagec14, (BULLETSIZE, BULLETSIZE))

bulletImagec21 = pygame.image.load('firecrashup2.png')
bulletStretchedImagec21 = pygame.transform.scale(bulletImagec21, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImagec22 = pygame.image.load('firecrashdown2.png')
bulletStretchedImagec22 = pygame.transform.scale(bulletImagec22, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImagec23 = pygame.image.load('firecrashleft2.png')
bulletStretchedImagec23 = pygame.transform.scale(bulletImagec23, (BULLETSIZE,int(BULLETSIZE*2/3)))
bulletImagec24 = pygame.image.load('firecrashright2.png')
bulletStretchedImagec24 = pygame.transform.scale(bulletImagec24, (BULLETSIZE,int(BULLETSIZE*2/3)))

laserImage1 = pygame.image.load('Laser.png')
laserImage2 = pygame.image.load('Laser.png')
laserImage3 = pygame.image.load('Laser2.png')
laserImage4 = pygame.image.load('Laser2.png')

itemImage0 = pygame.image.load('item0.png')
itemImage1 = pygame.image.load('item1.png')
itemImage2 = pygame.image.load('item2.png')
itemImage3 = pygame.image.load('item3.png')
itemImage4 = pygame.image.load('item4.png')
itemImage5 = pygame.image.load('item5.png')
itemImage6 = pygame.image.load('item6.png')
itemImage7 = pygame.image.load('item7.png')
itemStretchedImage0 = pygame.transform.scale(itemImage0, (ITEMSIZE, ITEMSIZE))
itemStretchedImage1 = pygame.transform.scale(itemImage1, (ITEMSIZE, ITEMSIZE))
itemStretchedImage2 = pygame.transform.scale(itemImage2, (ITEMSIZE, ITEMSIZE))
itemStretchedImage3 = pygame.transform.scale(itemImage3, (ITEMSIZE, ITEMSIZE))
itemStretchedImage4 = pygame.transform.scale(itemImage4, (ITEMSIZE, ITEMSIZE))
itemStretchedImage5 = pygame.transform.scale(itemImage5, (ITEMSIZE, ITEMSIZE))
itemStretchedImage6 = pygame.transform.scale(itemImage6, (ITEMSIZE, ITEMSIZE))
itemStretchedImage7 = pygame.transform.scale(itemImage7, (ITEMSIZE, ITEMSIZE))

itemStretchedImage0p = pygame.transform.scale(itemImage0, (220, 220))
itemStretchedImage1p = pygame.transform.scale(itemImage1, (220, 220))
itemStretchedImage2p = pygame.transform.scale(itemImage2, (220, 220))
itemStretchedImage3p = pygame.transform.scale(itemImage3, (220, 220))
itemStretchedImage4p = pygame.transform.scale(itemImage4, (220, 220))
itemStretchedImage5p = pygame.transform.scale(itemImage5, (220, 220))
itemStretchedImage6p = pygame.transform.scale(itemImage6, (220, 220))
itemStretchedImage7p = pygame.transform.scale(itemImage7, (220, 220))

turretImage11 = pygame.image.load('tankup1.png')
turretStretchedImage11 = pygame.transform.scale(turretImage11, (ITEMSIZE, ITEMSIZE))
turretImage12 = pygame.image.load('tankdown1.png')
turretStretchedImage12 = pygame.transform.scale(turretImage12, (ITEMSIZE, ITEMSIZE))
turretImage13 = pygame.image.load('tankleft1.png')
turretStretchedImage13 = pygame.transform.scale(turretImage13, (ITEMSIZE, ITEMSIZE))
turretImage14 = pygame.image.load('tankright1.png')
turretStretchedImage14 = pygame.transform.scale(turretImage14, (ITEMSIZE, ITEMSIZE))

turretImage21 = pygame.image.load('tankup1.png')
turretStretchedImage21 = pygame.transform.scale(turretImage21, (ITEMSIZE, ITEMSIZE))
turretImage22 = pygame.image.load('tankdown1.png')
turretStretchedImage22 = pygame.transform.scale(turretImage22, (ITEMSIZE, ITEMSIZE))
turretImage23 = pygame.image.load('tankleft1.png')
turretStretchedImage23 = pygame.transform.scale(turretImage23, (ITEMSIZE, ITEMSIZE))
turretImage24 = pygame.image.load('tankright1.png')
turretStretchedImage24 = pygame.transform.scale(turretImage24, (ITEMSIZE, ITEMSIZE))

skullImage = pygame.image.load('skull.png')
mineImage = pygame.image.load('mine.png')
mineStretchedImage = pygame.transform.scale(mineImage, (ITEMSIZE, ITEMSIZE))

itemselectImage = pygame.image.load('itemselect.png')
itemselectStretchedImage = pygame.transform.scale(itemselectImage, (560, 500))
gobackImage = pygame.image.load('goback.png')
gobackStretchedImage = pygame.transform.scale(gobackImage, (50, 50))

mainImage = pygame.image.load('background21.jpg')
mainStretchedImage = pygame.transform.scale(mainImage, (WINDOWWIDTH, WINDOWHEIGHT))
backgroundImage = pygame.image.load('brickTile.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
textname = basicFont1.render('FIRST BLOOD', True, WHITE)
textnameRect = textname.get_rect()
textnameRect.centerx = windowSurface.get_rect().centerx
textnameRect.centery = 150
textstart1 = basicFont2.render('PRACTICE', True, WHITE)
textstart1Rect = textstart1.get_rect()
textstart1Rect.right = 0
textstart1Rect.centery = 290
textstart2 = basicFont2.render('2 PLAYER', True, WHITE)
textstart2Rect = textstart2.get_rect()
textstart2Rect.left = WINDOWWIDTH
textstart2Rect.centery = 380
textsetting = basicFont2.render('SETTING', True, WHITE)
textsettingRect = textsetting.get_rect()
textsettingRect.right = 0
textsettingRect.centery = 470
textmade = basicFont3.render('made by OKJ, JWY', True, WHITE)
textmadeRect = textmade.get_rect()
textmadeRect.centerx = windowSurface.get_rect().centerx
textmadeRect.centery = 600
musictext = basicFont3.render('press ''m'' for music on and off', True, RED)
musictextRect = musictext.get_rect()
musictextRect.right = WINDOWWIDTH-10
musictextRect.top = 0
itemon = basicFont3.render(' ON ', True, WHITE)
itemonbutton = itemon.get_rect()
itemonbutton.centerx = 315
itemonbutton.centery = 465
onbutton = pygame.Rect(290, 445, 60, 40)
itemoff = basicFont3.render(' OFF ', True, WHITE)
itemoffbutton = itemoff.get_rect()
itemoffbutton.centerx = 375
itemoffbutton.centery = 465
offbutton = pygame.Rect(345, 445, 60, 40)
onoffcontrol = [pygame.Rect(285, 445, 60, 40), pygame.Rect(285, 445, 60, 40), pygame.Rect(285, 445, 60, 40), pygame.Rect(285, 445, 60, 40), pygame.Rect(285, 445, 60, 40), pygame.Rect(285, 445, 60, 40), pygame.Rect(285, 445, 60, 40), pygame.Rect(285, 445, 60, 40)]
robotstart1 = basicFont2.render('DEFENCE MODE', True, WHITE)
robotstart1Rect = robotstart1.get_rect()
robotstart1Rect.left = WINDOWWIDTH
robotstart1Rect.centery = WINDOWHEIGHT/3
robotstart2 = basicFont2.render('ATTACK MODE', True, WHITE)
robotstart2Rect = robotstart2.get_rect()
robotstart2Rect.centerx = robotstart1Rect.centerx
robotstart2Rect.centery = WINDOWHEIGHT/3*2
textmade = basicFont3.render('made by OKJ, JWY', True, WHITE)
text1 = basicFont3.render('Player1 WIN!', True, WHITE)
text2 = basicFont3.render('Player2 WIN!', True, WHITE)
slow = basicFont3.render('  slow  ', True, WHITE)
slowRect = slow.get_rect()
slowRect.right = WINDOWWIDTH
slowRect.top = 0
medium = basicFont3.render(' medium ', True, WHITE)
mediumRect = medium.get_rect()
mediumRect.right = WINDOWWIDTH
mediumRect.top = 0
fast = basicFont3.render('  fast  ', True, WHITE)
fastRect = fast.get_rect()
fastRect.right = WINDOWWIDTH
fastRect.top = 0
veryfast = basicFont3.render(' veryfast ', True, WHITE)
veryfastRect = veryfast.get_rect()
veryfastRect.right = WINDOWWIDTH
veryfastRect.top = 0
speedis = basicFont3.render('SPEED: ', True, WHITE)
speedisRect = speedis.get_rect()
speedisRect.right = veryfastRect.left
speedisRect.top = 0
information = [0,0,0,0,0,0,0,0,0]
informationRect = [0,0,0,0,0,0,0,0,0]
information[0] = basicFont3.render('make other player bigger', True, WHITE)
informationRect[0] = information[0].get_rect()
informationRect[0].centerx = windowSurface.get_rect().centerx
informationRect[0].centery = windowSurface.get_rect().centery
information[1] = basicFont3.render('make other player slower', True, WHITE)
informationRect[1] = information[1].get_rect()
informationRect[1].centerx = windowSurface.get_rect().centerx
informationRect[1].centery = windowSurface.get_rect().centery
information[2] = basicFont3.render('shooting laser', True, WHITE)
informationRect[2] = information[2].get_rect()
informationRect[2].centerx = windowSurface.get_rect().centerx
informationRect[2].centery = windowSurface.get_rect().centery
information[3] = basicFont3.render('become invincible and teleport', True, WHITE)
informationRect[3] = information[3].get_rect()
informationRect[3].centerx = windowSurface.get_rect().centerx
informationRect[3].centery = windowSurface.get_rect().centery
information[4] = basicFont3.render('making turret', True, WHITE)
informationRect[4] = information[4].get_rect()
informationRect[4].centerx = windowSurface.get_rect().centerx
informationRect[4].centery = windowSurface.get_rect().centery
information[5] = basicFont3.render('heal', True, WHITE)
informationRect[5] = information[5].get_rect()
informationRect[5].centerx = windowSurface.get_rect().centerx
informationRect[5].centery = windowSurface.get_rect().centery
information[6] = basicFont3.render('make other player keyboard opposite', True, WHITE)
informationRect[6] = information[6].get_rect()
informationRect[6].centerx = windowSurface.get_rect().centerx
informationRect[6].centery = windowSurface.get_rect().centery
information[7] = basicFont3.render('make mine and cannot move', True, WHITE)
informationRect[7] = information[7].get_rect()
informationRect[7].centerx = windowSurface.get_rect().centerx
informationRect[7].centery = windowSurface.get_rect().centery

GAMESTART = 1
SETTING = 0
WINNER = 0
GAMEEND = 0
WHO = 0
mousex = 0
mousey = 0
BULLETSPEED = 4
BULLETGAP = 15
BULLETINTERVAL1 = BULLETGAP-1
BULLETINTERVAL2 = BULLETGAP-1
FIREBUGINTERVAL = BULLETGAP
FIREBUG1 = FIREBUGINTERVAL
FIREBUG2 = FIREBUGINTERVAL
FIREBUGTRUE1 = False
FIREBUGTRUE2 = False
HP1 = player1.width
HP2 = player2.width
ascore = 0
bscore = 0
DESIGN11 = 1
DESIGN12 = 0
wt1 = 0
DESIGN21 = 0
DESIGN22 = 0
wt2 = 0
DESIGN31 = 0
DESIGN32 = 0
wt3 = 0
wt = 0
k = 0
itemlist = []
attackmode = 0
defencemode = 0

while True:
    player1 = pygame.Rect(int(WINDOWWIDTH/4)-25, int(WINDOWHEIGHT/2)-25, SIZE1, SIZE1)
    player2 = pygame.Rect(int(WINDOWWIDTH/4*3)-25, int(WINDOWHEIGHT/2)-25, SIZE2, SIZE2)
    turret1 = pygame.Rect(0, 0, ITEMSIZE, ITEMSIZE)
    turret2 = pygame.Rect(0, 0, ITEMSIZE, ITEMSIZE)
    HP1 = player1.width
    HP2 = player2.width
    up1 = []
    down1 = []
    left1 = []
    right1 = []
    up1c = []
    down1c = []
    left1c = []
    right1c = []
    up1crash = []
    down1crash = []
    left1crash = []
    right1crash = []
    direction1 = 'right'
    up2 = []
    down2 = []
    left2 = []
    right2 = []
    up2c = []
    down2c = []
    left2c = []
    right2c = []
    up2crash = []
    down2crash = []
    left2crash = []
    right2crash = []
    direction2 = 'left'
    FIREBUGTRUE1 = False
    FIREBUGTRUE2 = False
    moveUp1 = False
    moveDown1 = False
    moveLeft1 = False
    moveRight1 = False
    moveUp2 = False
    moveDown2 = False
    moveLeft2 = False
    moveRight2 = False
    fireGun1 = False
    fireGun2 = False
    ITEM0 = []
    ITEM1 = []
    ITEM2 = []
    ITEM3 = []
    ITEM4 = []
    ITEM5 = []
    ITEM6 = []
    ITEM7 = []
    SISE1 = 0
    SISE2 = 0
    SISE1_COUNTER = 0
    SISE2_COUNTER = 0
    SISETIME = SPEED*5
    ICE1 = 0
    ICE2 = 0
    ICE1_COUNTER = 0
    ICE2_COUNTER = 0
    ICETIME = SPEED*5
    LASER1 = 0
    LASER2 = 0
    LASER1_COUNTER = 0
    LASER2_COUNTER = 0
    LASERTIME = SPEED*2
    SHIELD1 = 0
    SHIELD2 = 0
    SHIELD1_COUNTER = 0
    SHIELD2_COUNTER = 0
    SHIELDTIME = SPEED*3
    TURRET1 = 0
    TURRET2 = 0
    TURRET_direction1 = "right"
    TURRET_direction2 = "right"
    TURRET1_COUNTER = 0
    TURRET2_COUNTER = 0
    TURRETTIME = SPEED*10
    SKULL1 = 0
    SKULL2 = 0
    SKULL_COUNTER = 0
    SKULLTIME = SPEED*3
    MINE1 = []
    MINE2 = []
    TRAPPED1 = 0
    TRAPPED2 = 0
    MINE1_COUNTER = 0
    MINE2_COUNTER = 0
    MINETIME = SPEED*2
    MOVESPEED1 = 3
    MOVESPEED2 = 3
    rightcounter = 0
    Rightcount = 0
    leftcounter = 0
    Leftcount = 0
    upcounter = 0
    Upcount = 0
    downcounter = 0
    Downcount = 0
    ROBOT = 0
    MOVING = 1
    selectrobot = 1
    MOVING2 = 1
    defencemodenum = 0
    speedy = 3
    no = 1
    itemdot = [0,0,0,0,0,0,0,0]
    timetoturnright = 0
    timetoturnleft = 0
    turnrighttime = 0
    turnlefttime = 0
    buttonmove = 0
    itemselected = 0
    showing = 0
    sign = [-1, -1, -1, -1, -1, -1, -1, -1]
    musicplaying = True
    pickUpsound = pygame.mixer.Sound('click.WAV')
    firesound = pygame.mixer.Sound('shotgun2.WAV')
    heal = pygame.mixer.Sound('heal.wav')
    hit = pygame.mixer.Sound('hit.wav')
    mine = pygame.mixer.Sound('mine.wav')
    bigger = pygame.mixer.Sound('bigger.wav')
    install = pygame.mixer.Sound('install.WAV')
    flip = pygame.mixer.Sound('flip.wav')
    game = 0
    pygame.mixer.music.load('interstella.mp3')
    pygame.mixer.music.play(-1,3.0)

    while GAMESTART:
        SIZE1 = 50
        SIZE2 = 50
        ceta = 0
        ascore = 0
        bscore = 0
        pplayer1 = pygame.Rect(player1.left, player1.top, SIZE1, SIZE1)
        pplayer2 = pygame.Rect(player2.left, player2.top, SIZE2, SIZE2)
        if DESIGN11:
            textstart1Rect.right += 10
        if DESIGN11 and textstart1Rect.centerx > 350:
            DESIGN11 = 0
            DESIGN12 = 1
        if DESIGN12:
            textstart1Rect.right += 10*(2.718**(-wt1/SPEED))*math.cos(wt1*math.pi*2/SPEED)
            wt1 += 1
        if DESIGN12 and wt1 > 80:
            DESIGN12 = 0
            textstart1Rect.centerx = 350

        if DESIGN21:
            textstart2Rect.right -= 10
        if DESIGN21 and textstart2Rect.centerx < 440:
            DESIGN21 = 0
            DESIGN22 = 1
        if DESIGN22:
            textstart2Rect.right -= 10*(2.718**(-wt2/SPEED))*math.cos(wt2*math.pi*2/SPEED)
            wt2 += 1
        if DESIGN22 and wt2 > 80:
            DESIGN22 = 0
            textstart2Rect.centerx = 350

        if DESIGN31:
            textsettingRect.right += 10
        if DESIGN31 and textsettingRect.centerx > 350:
            DESIGN31 = 0
            DESIGN32 = 1
        if DESIGN32:
            textsettingRect.right += 10*(2.718**(-wt3/SPEED))*math.cos(wt3*math.pi*2/SPEED)
            wt3 += 1
        if wt3 > 80:
            DESIGN32 = 0
            textsettingRect.centerx = 350

        if wt >= 0:
            wt += 1
        if wt >= 10:
            DESIGN21 = 1
        if wt >= 20:
            DESIGN31 = 1
            wt = -1
        windowSurface.blit(mainStretchedImage, (0,0))
        windowSurface.blit(textname, textnameRect)
        windowSurface.blit(textstart1, textstart1Rect)
        windowSurface.blit(textstart2, textstart2Rect)
        windowSurface.blit(textsetting, textsettingRect)
        windowSurface.blit(textmade, textmadeRect)
        windowSurface.blit(musictext,musictextRect)
        mousex = 0
        mousey = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if musicplaying:
                    pickUpsound.play()
            if event.type == KEYDOWN:
                if event.key == ord('m'):
                    if musicplaying == True:
                        pygame.mixer.music.stop()
                    if musicplaying == False :
                        pygame.mixer.music.play(-1,0.0)
                    musicplaying = not musicplaying
        if mousey > textstart1Rect.top and mousey < textstart1Rect.bottom and mousex > textstart1Rect.left and mousex < textstart1Rect.right:
            GAMESTART = 0
            WINNER = 1
            ROBOT = 1
            selectrobot = 1
            MOVING2 = 1
            robotstart1Rect.left = WINDOWWIDTH
            robotstart1Rect.centery = WINDOWHEIGHT/3
            robotstart2Rect.centerx = robotstart1Rect.centerx
            robotstart2Rect.centery = WINDOWHEIGHT/3*2
        if mousey > textstart2Rect.top and mousey < textstart2Rect.bottom and mousex > textstart2Rect.left and mousex < textstart2Rect.right:
            GAMESTART = 0
            WINNER = 1
            defencemode = 0
            attackmode = 0
            if musicplaying:
                pygame.mixer.music.load('mylength.mp3')
                pygame.mixer.music.play(1,0.0)
        if mousey > textsettingRect.top and mousey < textsettingRect.bottom and mousex > textsettingRect.left and mousex < textsettingRect.right:
            GAMESTART = 0
            SETTING = 1
        # draw the window onto the screen
        pygame.display.update()
        mainClock.tick(SPEED)

    while SETTING:
        mousex = 0
        mousey = 0
        no = 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    timetoturnright = 1
                if event.key == K_LEFT:
                    timetoturnleft = 1
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if musicplaying:
                    pickUpsound.play()
        windowSurface.blit(mainStretchedImage, (0, 0))
        if mousex >= goback.left and mousex <= goback.right and mousey >= goback.top and mousey <= goback.bottom:
            SETTING = 0
            GAMESTART = 1
        if MOVING:
            k += 1
            if textnameRect.right >= 0:
                textnameRect.right -= 10
            if textstart1Rect.right >= 0:
                textstart1Rect.right -= 10
            if textstart2Rect.right >= 0:
                textstart2Rect.right -= 10
            if textsettingRect.right >= 0:
                textsettingRect.right -= 10
            if textmadeRect.right >=0:
                textmadeRect.right -= 10
            windowSurface.blit(textname, textnameRect)
            windowSurface.blit(textstart1, textstart1Rect)
            windowSurface.blit(textstart2, textstart2Rect)
            windowSurface.blit(textsetting, textsettingRect)
            windowSurface.blit(textmade, textmadeRect)
        if textnameRect.right < 0 and textstart1Rect.right < 0 and textstart2Rect.right < 0 and textsettingRect.right < 0:
            MOVING = 0
            textnameRect.centerx = windowSurface.get_rect().centerx
            textnameRect.centery = 150
            textstart1Rect.centerx = windowSurface.get_rect().centerx
            textstart1Rect.centery = 290
            textstart2Rect.centerx = windowSurface.get_rect().centerx
            textstart2Rect.centery = 380
            textsettingRect.centerx = windowSurface.get_rect().centerx
            textsettingRect.centery = 470
            textmadeRect.centerx = windowSurface.get_rect().centerx
            textmadeRect.centery = 600
        if not MOVING:
            if timetoturnright:
                turnrighttime += 1
                ceta += math.pi/100
            if timetoturnleft:
                turnlefttime += 1
                ceta -= math.pi/100
            if turnrighttime >= 25 or turnlefttime >= 25:
                if musicplaying:
                    flip.play()
                if turnrighttime >= 25:
                    itemselected -= 1
                if turnlefttime >= 25:
                    itemselected += 1
                if itemselected == -1:
                    itemselected = 7
                if itemselected == 8:
                    itemselected = 0
                showing = 0
                turnrighttime = 0
                timetoturnright = 0
                turnlefttime = 0
                timetoturnleft = 0
                if ceta < 0:
                    ceta += 2*math.pi
                if ceta >= math.pi/4 - 0.1 and ceta <= math.pi/4 + 0.1:
                    ceta = math.pi/4
                if ceta >= math.pi/2 - 0.1 and ceta <= math.pi/2 + 0.1:
                    ceta = math.pi/2
                if ceta >= math.pi*3/4 - 0.1 and ceta <= math.pi*3/4 + 0.1:
                    ceta = math.pi*3/4
                if ceta >= math.pi - 0.1 and ceta <= math.pi + 0.1:
                    ceta = math.pi
                if ceta >= math.pi*5/4 - 0.1 and ceta <= math.pi*5/4 + 0.1:
                    ceta = math.pi*5/4
                if ceta >= math.pi*3/2 - 0.1 and ceta <= math.pi*3/2 + 0.1:
                    ceta = math.pi*3/2
                if ceta >= math.pi*7/4 - 0.1 and ceta <= math.pi*7/4 + 0.1:
                    ceta = math.pi*7/4
                if ceta >= 2*math.pi - 0.1 and ceta <= 2*math.pi + 0.1:
                    ceta = 0
            windowSurface.blit(gobackStretchedImage, goback)
            pygame.draw.rect(windowSurface, COLOR2, (340+300*math.cos(ceta),340+300*math.sin(ceta), 20, 20))
            pygame.draw.rect(windowSurface, COLOR3, (340+300*math.cos(ceta+math.pi/4),340+300*math.sin(ceta+math.pi/4), 20, 20))
            pygame.draw.rect(windowSurface, COLOR4, (340+300*math.cos(ceta+math.pi/2),340+300*math.sin(ceta+math.pi/2), 20, 20))
            pygame.draw.rect(windowSurface, COLOR5, (340+300*math.cos(ceta+math.pi*3/4),340+300*math.sin(ceta+math.pi*3/4), 20, 20))
            pygame.draw.rect(windowSurface, COLOR6, (340+300*math.cos(ceta+math.pi),340+300*math.sin(ceta+math.pi), 20, 20))
            pygame.draw.rect(windowSurface, COLOR7, (340+300*math.cos(ceta+math.pi*5/4), 340+300*math.sin(ceta+math.pi*5/4), 20, 20))
            pygame.draw.rect(windowSurface, COLOR0, (340+300*math.cos(ceta+math.pi*3/2), 340+300*math.sin(ceta+math.pi*3/2), 20, 20))
            pygame.draw.rect(windowSurface, COLOR1, (340+300*math.cos(ceta+math.pi*7/4), 340+300*math.sin(ceta+math.pi*7/4), 20, 20))
            if timetoturnright == 0 and timetoturnleft == 0:
                windowSurface.blit(itemselectStretchedImage, itemselect)
                pygame.draw.circle(windowSurface, ORANGE, (350, 528), 26, 0)
                if ceta == 0:
                    windowSurface.blit(itemStretchedImage0p, showitem)
                if ceta >= math.pi/4 - 0.1 and ceta <= math.pi/4 + 0.1:
                    windowSurface.blit(itemStretchedImage7p, showitem)
                if ceta >= math.pi/2 - 0.1 and ceta <= math.pi/2 + 0.1:
                    windowSurface.blit(itemStretchedImage6p, showitem)
                if ceta >= math.pi*3/4 - 0.1 and ceta <= math.pi*3/4 + 0.1:
                    windowSurface.blit(itemStretchedImage5p, showitem)
                if ceta >= math.pi - 0.1 and ceta <= math.pi + 0.1:
                    windowSurface.blit(itemStretchedImage4p, showitem)
                if ceta >= math.pi*5/4 - 0.1 and ceta <= math.pi*5/4 + 0.1:
                    windowSurface.blit(itemStretchedImage3p, showitem)
                if ceta >= math.pi*3/2 - 0.1 and ceta <= math.pi*3/2 + 0.1:
                    windowSurface.blit(itemStretchedImage2p, showitem)
                if ceta >= math.pi*7/4 - 0.1 and ceta <= math.pi*7/4 + 0.1:
                    windowSurface.blit(itemStretchedImage1p, showitem)
                if mousex >= itemonbutton.left and mousex <= itemoffbutton.right and mousey >= itemonbutton.top and mousey <= itemonbutton.bottom:
                    sign[itemselected] *= -1
                    buttonmove = 1
                if buttonmove and sign[itemselected] == 1 and onoffcontrol[itemselected].right < itemoffbutton.right:
                    onoffcontrol[itemselected].right += 3
                if buttonmove and sign[itemselected] == -1 and onoffcontrol[itemselected].left > itemonbutton.left:
                    onoffcontrol[itemselected].left -= 3
                if buttonmove and sign[itemselected] == 1 and onoffcontrol[itemselected].right >= itemoffbutton.right:
                    onoffcontrol[itemselected].right = itemoffbutton.right
                    buttonmove = 0
                    itemlist.append(itemselected)
                if buttonmove and sign[itemselected] == -1 and onoffcontrol[itemselected].left <= itemonbutton.left:
                    onoffcontrol[itemselected].left = itemonbutton.left
                    buttonmove = 0
                    if itemselected in itemlist:
                        itemlist.remove(itemselected)
                if showing and no and mousex >= iteminfo.left and mousex <= iteminfo.right and mousey >= iteminfo.top and mousey <= iteminfo.bottom:
                    showing = 0
                    no = 0
                if not showing and no and mousex >= iteminfo.left and mousex <= iteminfo.right and mousey >= iteminfo.top and mousey <= iteminfo.bottom:
                    showing = 1
                    no = 0
                if showing:
                    pygame.draw.rect(windowSurface, GRAY, informationRect[itemselected])
                    windowSurface.blit(information[itemselected], informationRect[itemselected])
                pygame.draw.rect(windowSurface, GRAY, offbutton)
                windowSurface.blit(itemoff, itemoffbutton)
                if onoffcontrol[itemselected].right == itemoffbutton.right:
                    pygame.draw.rect(windowSurface, RED, onbutton)
                else:
                    pygame.draw.rect(windowSurface, GRAY, onbutton)
                windowSurface.blit(itemon, itemonbutton)
                pygame.draw.rect(windowSurface, WHITE, onoffcontrol[itemselected])
        pygame.display.update()
        mainClock.tick(SPEED)
        
    while ROBOT:
        while selectrobot:
            windowSurface.blit(mainStretchedImage, (0,0))
            if MOVING:
                if textnameRect.right >= 0:
                    textnameRect.right -= 10
                if textstart1Rect.right >= 0:
                    textstart1Rect.right -= 10
                if textstart2Rect.right >= 0:
                    textstart2Rect.right -= 10
                if textsettingRect.right >= 0:
                    textsettingRect.right -= 10
            if textnameRect.right < 0 and textstart1Rect.right < 0 and textstart2Rect.right < 0 and textsettingRect.right < 0:
                MOVING = 0
            windowSurface.blit(textname, textnameRect)
            windowSurface.blit(textstart1, textstart1Rect)
            windowSurface.blit(textstart2, textstart2Rect)
            windowSurface.blit(textsetting, textsettingRect)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
            if MOVING2:
                if robotstart1Rect.centerx >= WINDOWWIDTH/2:
                    robotstart1Rect.right -= 10
                if robotstart2Rect.centerx >= WINDOWWIDTH/2:
                    robotstart2Rect.right -= 10
            if robotstart1Rect.centerx < WINDOWWIDTH/2 and robotstart2Rect.centerx < WINDOWWIDTH/2:
                MOVING2 = 0
            windowSurface.blit(gobackStretchedImage, goback)
            windowSurface.blit(robotstart1, robotstart1Rect)
            windowSurface.blit(robotstart2, robotstart2Rect)
            if mousex >= goback.left and mousex <= goback.right and mousey >= goback.top and mousey <= goback.bottom:
                ROBOT = 0
                selectrobot = 0
                GAMESTART = 1
                WINNER = 0
                textnameRect.centerx = windowSurface.get_rect().centerx
                textnameRect.centery = 150
                textstart1Rect.centerx = windowSurface.get_rect().centerx
                textstart1Rect.centery = 290
                textstart2Rect.centerx = windowSurface.get_rect().centerx
                textstart2Rect.centery = 380
                textsettingRect.centerx = windowSurface.get_rect().centerx
                textsettingRect.centery = 470
                textmadeRect.centerx = windowSurface.get_rect().centerx
                textmadeRect.centery = 600
            if mousey > robotstart1Rect.top and mousey < robotstart1Rect.bottom and mousex > robotstart1Rect.left and mousex < robotstart1Rect.right:
                selectrobot = 0
                defencemode = 1
                attackmode = 0
                if musicplaying:
                    pygame.mixer.music.load('lisin.mp3')
                    pygame.mixer.music.play(1, 0.0)
            if mousey > robotstart2Rect.top and mousey < robotstart2Rect.bottom and mousex > robotstart2Rect.left and mousex < robotstart2Rect.right:
                selectrobot = 0
                attackmode = 1
                defencemode = 0
            pygame.display.update()
            mainClock.tick(SPEED)
        break
    if attackmode:
            pplayer2 = pygame.Rect(WINDOWWIDTH/2 - SIZE2/2, WINDOWHEIGHT/2 - SIZE2/2 + SIZE2/10, SIZE2, SIZE2)
            if musicplaying:
                pygame.mixer.music.load('kill.mp3')
                pygame.mixer.music.play(1,0.0)
    if defencemode:
            pplayer1 = pygame.Rect(WINDOWWIDTH/2 - SIZE2/2, WINDOWHEIGHT/2 - SIZE2/2 + SIZE2/10, SIZE2, SIZE2)
    winner = 0
    inner = 0
    
    # run the game loop
    while WINNER:
        winner += 1
        if winner == int(SPEED*2.5):
            if musicplaying:
                pygame.mixer.music.load('undertale.mp3')
                pygame.mixer.music.play(-1,0.0)
        # draw the background onto the surface
        windowSurface.blit(backgroundStretchedImage, (0,0))
        pplayer1 = pygame.Rect(pplayer1.left, pplayer1.top, SIZE1, SIZE1)
        pplayer2 = pygame.Rect(pplayer2.left, pplayer2.top, SIZE2, SIZE2)
        playerStretchedImage1ou = pygame.transform.scale(playerImage1ou, (SIZE1, SIZE1))
        playerStretchedImage1od = pygame.transform.scale(playerImage1od, (SIZE1, SIZE1))
        playerStretchedImage1ol = pygame.transform.scale(playerImage1ol, (SIZE1, SIZE1))
        playerStretchedImage1or = pygame.transform.scale(playerImage1or, (SIZE1, SIZE1))
        playerStretchedImage1cu = pygame.transform.scale(playerImage1cu, (SIZE1, SIZE1))
        playerStretchedImage1cd = pygame.transform.scale(playerImage1cd, (SIZE1, SIZE1))
        playerStretchedImage1cl = pygame.transform.scale(playerImage1cl, (SIZE1, SIZE1))
        playerStretchedImage1cr = pygame.transform.scale(playerImage1cr, (SIZE1, SIZE1))
        playerStretchedImage2ou = pygame.transform.scale(playerImage2ou, (SIZE2, SIZE2))
        playerStretchedImage2od = pygame.transform.scale(playerImage2od, (SIZE2, SIZE2))
        playerStretchedImage2ol = pygame.transform.scale(playerImage2ol, (SIZE2, SIZE2))
        playerStretchedImage2or = pygame.transform.scale(playerImage2or, (SIZE2, SIZE2))
        playerStretchedImage2cu = pygame.transform.scale(playerImage2cu, (SIZE2, SIZE2))
        playerStretchedImage2cd = pygame.transform.scale(playerImage2cd, (SIZE2, SIZE2))
        playerStretchedImage2cl = pygame.transform.scale(playerImage2cl, (SIZE2, SIZE2))
        playerStretchedImage2cr = pygame.transform.scale(playerImage2cr, (SIZE2, SIZE2))

        laserStretchedImage1 = pygame.transform.scale(laserImage2, (int(WINDOWWIDTH/3), BULLETSIZE))
        laserStretchedImage2 = pygame.transform.scale(laserImage3, (BULLETSIZE,int(WINDOWHEIGHT/3)))
        laserStretchedImage3 = pygame.transform.scale(laserImage2, (int(WINDOWWIDTH/3), BULLETSIZE))
        laserStretchedImage4 = pygame.transform.scale(laserImage3, (BULLETSIZE, int(WINDOWHEIGHT/3)))
        
        laserStretchedImage11 = pygame.transform.scale(laserImage1, (pplayer1.left+5, BULLETSIZE))
        laserStretchedImage12 = pygame.transform.scale(laserImage2, (WINDOWHEIGHT-pplayer1.right+5, BULLETSIZE))
        laserStretchedImage13 = pygame.transform.scale(laserImage3, (BULLETSIZE, pplayer1.top+5))
        laserStretchedImage14 = pygame.transform.scale(laserImage4, (BULLETSIZE, WINDOWWIDTH-pplayer1.bottom+5))
        laserStretchedImage21 = pygame.transform.scale(laserImage1, (pplayer2.left+5, BULLETSIZE))
        laserStretchedImage22 = pygame.transform.scale(laserImage2, (WINDOWHEIGHT-pplayer2.right+5, BULLETSIZE))
        laserStretchedImage23 = pygame.transform.scale(laserImage3, (BULLETSIZE, pplayer2.top+5))
        laserStretchedImage24 = pygame.transform.scale(laserImage4, (BULLETSIZE, WINDOWWIDTH-pplayer2.bottom+5))

        robotlaser1 = pygame.Rect((WINDOWWIDTH/3, WINDOWHEIGHT/3, WINDOWWIDTH/3, BULLETSIZE))
        robotlaser2 = pygame.Rect((WINDOWWIDTH/3*2-BULLETSIZE/2, WINDOWHEIGHT/3+BULLETSIZE/2, BULLETSIZE, WINDOWHEIGHT/3))
        robotlaser3 = pygame.Rect((WINDOWWIDTH/3, WINDOWHEIGHT/3*2, WINDOWWIDTH/3, BULLETSIZE))
        robotlaser4 = pygame.Rect((WINDOWWIDTH/3-BULLETSIZE/2, WINDOWHEIGHT/3+BULLETSIZE/2, BULLETSIZE, WINDOWHEIGHT/3))
        
        uplayer1 = pygame.Rect(pplayer1.centerx-(BULLETSIZE/2), 0, BULLETSIZE, pplayer1.top)
        dplayer1 = pygame.Rect(pplayer1.centerx-(BULLETSIZE/2), pplayer1.bottom, BULLETSIZE, WINDOWHEIGHT-pplayer1.bottom)
        lplayer1 = pygame.Rect(0, pplayer1.centery-(BULLETSIZE/2), pplayer1.left, BULLETSIZE)
        rplayer1 = pygame.Rect(pplayer1.right, pplayer1.centery-(BULLETSIZE/2), WINDOWWIDTH-pplayer1.right, BULLETSIZE)

        uplayer2 = pygame.Rect(pplayer2.centerx-(BULLETSIZE/2), 0, BULLETSIZE, pplayer2.top)
        dplayer2 = pygame.Rect(pplayer2.centerx-(BULLETSIZE/2), pplayer2.bottom, BULLETSIZE, WINDOWHEIGHT-pplayer2.bottom)
        lplayer2 = pygame.Rect(0, pplayer2.centery-(BULLETSIZE/2), pplayer2.left, BULLETSIZE)
        rplayer2 = pygame.Rect(pplayer2.right, pplayer2.centery-(BULLETSIZE/2), WINDOWWIDTH-pplayer2.right, BULLETSIZE)
        
        skullStretchedImage1 = pygame.transform.scale(skullImage, (SIZE1, SIZE1))
        skullStretchedImage2 = pygame.transform.scale(skullImage, (SIZE2, SIZE2))
        
        # check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # change the keyboard variables
                if event.key == ord('w'):
                    if not SKULL1:
                        direction1 = 'up'
                        moveUp1 = True
                        moveDown1 = False
                    if SKULL1:
                        direction1 = 'down'
                        moveDown1 = True
                        moveUp1 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == K_UP :
                    if not SKULL2:
                        direction2 = 'up'
                        moveUp2 = True
                        moveDown2 = False
                    if SKULL2:
                        direction2 = 'down'
                        moveDown2 = True
                        moveUp2 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == ord('s'):
                    if not SKULL1:
                        direction1 = 'down'
                        moveDown1 = True
                        moveUp1 = False
                    if SKULL1:
                        direction1 = 'up'
                        moveUp1 = True
                        mvoeDown1 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == K_DOWN :
                    if not SKULL2:
                        direction2 = 'down'
                        moveDown2 = True
                        moveUp2 = False
                    if SKULL2:
                        direction2 = 'up'
                        moveUp2 = True
                        moveDown2 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == ord('a'):
                    if not SKULL1:
                        direction1 = 'left'
                        moveLeft1 = True
                        moveRight1 = False
                    if SKULL1:
                        direction1 = 'right'
                        moveRight1 = True
                        moveLeft1 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == K_LEFT:
                    if not SKULL2:
                        direction2 = 'left'
                        moveLeft2 = True
                        moveRight2 = False
                    if SKULL2:
                        direction2 = 'right'
                        moveRight2 = True
                        moveLeft2 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == ord('d'):
                    if not SKULL1:
                        direction1 = 'right'
                        moveRight1 = True
                        moveLeft1 = False
                    if SKULL1:
                        direction1 = 'left'
                        moveLeft1 = True
                        moveRight1 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == K_RIGHT:
                    if not SKULL2:
                        direction2 = 'right'
                        moveRight2 = True
                        moveLeft2 = False
                    if SKULL2:
                        direction2 = 'left'
                        moveLeft2 = True
                        moveRight2 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == ord(' ') and FIREBUG1 >= FIREBUGINTERVAL:
                    fireGun1 = True
                    FIREBUG1 = 0
                    FIREBUGTRUE1 = True
                    FIREBUGTRUE2 = False
                if event.key == ord('/') and FIREBUG2 >= FIREBUGINTERVAL:
                    fireGun2 = True
                    FIREBUG2 = 0
                    FIREBUGTRUE2 = True
                    FIREBUGTRUE1 = False
                
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == ord('w'):
                    if not SKULL1:
                        moveUp1 = False
                    if SKULL1:
                        moveDown1 = False
                if event.key == K_UP :
                    if not SKULL2:
                        moveUp2 = False
                    if SKULL2:
                        moveDown2 = False
                if event.key == ord('s'):
                    if not SKULL1:
                        moveDown1 = False
                    if SKULL1:
                        moveUp1 = False
                if event.key == K_DOWN:
                    if not SKULL2:
                        moveDown2 = False
                    if SKULL2:
                        moveUp2 = False
                if event.key == ord('a'):
                    if not SKULL1:
                        moveLeft1 = False
                    if SKULL1:
                        moveRight1 = False
                if event.key == K_LEFT :
                    if not SKULL2:
                        moveLeft2 = False
                    if SKULL2:
                        moveRight2 = False
                if event.key == ord('d'):
                    if not SKULL1:
                        moveRight1 = False
                    if SKULL1:
                        moveLeft1 = False
                if event.key == K_RIGHT:
                    if not SKULL2:
                        moveRight2 = False
                    if SKULL2:
                        moveLeft2 = False
                if event.key == ord(' '):
                    fireGun1 = False
                    BULLETINTERVAL1 = BULLETGAP-1
                    if LASER1 == 1:
                        LASER1 = 0
                if event.key == ord('/'):
                    fireGun2 = False
                    BULLETINTERVAL2 = BULLETGAP-1
                    if LASER2 == 1:
                        LASER2 = 0
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if musicplaying:
                    pickUpsound.play()
        if defencemode:
            if defencemodenum == int(SPEED*2.5):
                if musicplaying:
                    pygame.mixer.music.load('Resolver.mp3')
                    pygame.mixer.music.play(-1,0.0)
            windowSurface.blit(speedis, speedisRect)
            no = 1
            if mousey > fastRect.top and mousey < fastRect.bottom and mousex > fastRect.left and mousex < fastRect.right and speedy == 2 and no:
                speedy = 1
                no = 0
            if mousey > mediumRect.top and mousey < mediumRect.bottom and mousex > mediumRect.left and mousex < mediumRect.right and speedy == 3 and no:
                speedy = 2
                no = 0
            if mousey > slowRect.top and mousey < slowRect.bottom and mousex > slowRect.left and mousex < slowRect.right and speedy == 4 and no:
                speedy = 3
                no = 0
            if mousey > veryfastRect.top and mousey < veryfastRect.bottom and mousex > veryfastRect.left and mousex < veryfastRect.right and speedy == 1 and no:
                speedy = 4
                no = 0
            if speedy == 1:
                windowSurface.blit(veryfast, veryfastRect)
            if speedy == 2:
                windowSurface.blit(fast, fastRect)
            if speedy == 3:
                windowSurface.blit(medium, mediumRect)
            if speedy == 4:
                windowSurface.blit(slow, slowRect)
            defencemodenum += 1
            if defencemodenum > SPEED*3:
                if defencemodenum % (SPEED*speedy) == 0:
                    up2.append(pygame.Rect(random.randint(pplayer1.centerx - SIZE2, pplayer1.centerx + SIZE2), WINDOWHEIGHT, BULLETSIZE, BULLETSIZE))
                if defencemodenum % (SPEED*speedy) == int(SPEED/4*speedy):
                    down2.append(pygame.Rect(random.randint(pplayer1.centerx - SIZE2, pplayer1.centerx + SIZE2), 0, BULLETSIZE, BULLETSIZE))
                if defencemodenum % (SPEED*speedy) == int(SPEED/4*speedy*2):
                    right2.append(pygame.Rect(0, random.randint(pplayer1.centery - SIZE2, pplayer1.centery + SIZE2), BULLETSIZE, BULLETSIZE))
                if defencemodenum % (SPEED*speedy) == int(SPEED/4*speedy*3):
                    left2.append(pygame.Rect(WINDOWWIDTH, random.randint(pplayer1.centery - SIZE2, pplayer1.centery + SIZE2), BULLETSIZE, BULLETSIZE))
        mousex = 0
        mousey = 0
        if attackmode:
            inner += 1
            if inner == int(SPEED*2.5):
                if musicplaying:
                    pygame.mixer.music.load('Resolver.mp3')
                    pygame.mixer.music.play(-1,0.0)
            windowSurface.blit(laserStretchedImage1, robotlaser1)
            windowSurface.blit(laserStretchedImage2, robotlaser2)
            windowSurface.blit(laserStretchedImage3, robotlaser3)
            windowSurface.blit(laserStretchedImage4, robotlaser4)
            if len(down1) > 0:
                for i in range(len(down1)):
                    if ((pplayer2.top - down1[i].bottom)/BULLETSPEED)//MOVESPEED2 <= (down1[i].right - pplayer2.left +MOVESPEED2)/MOVESPEED2//MOVESPEED2 and (pplayer2.top - down1[i].bottom) > -(SIZE2 + BULLETSIZE) and pplayer2.right - down1[i].left >= (SIZE2+BULLETSIZE)/2 and pplayer2.right - down1[i].left < (SIZE2+BULLETSIZE): 
                        rightcounter = 0
                        Rightcount = ((down1[i].right - pplayer2.left) + MOVESPEED2)//MOVESPEED2
                    if ((pplayer2.top - down1[i].bottom)/BULLETSPEED)//MOVESPEED2 <= (pplayer2.right - down1[i].left+MOVESPEED2)/MOVESPEED2//MOVESPEED2 and (pplayer2.top - down1[i].bottom) > -(SIZE2 + BULLETSIZE) and pplayer2.right - down1[i].left < (SIZE2+BULLETSIZE)/2 and pplayer2.right - down1[i].left > 0:
                        leftcounter = 0
                        Leftcount = ((pplayer2.right - down1[i].left) + MOVESPEED2)//MOVESPEED2
            if len(up1) > 0:
                for i in range(len(up1)):
                    if ((pplayer2.bottom - up1[i].top)/BULLETSPEED)//MOVESPEED2 == -(up1[i].right - pplayer2.left +MOVESPEED2)/MOVESPEED2//MOVESPEED2 and pplayer2.right - up1[i].left >= (SIZE2+BULLETSIZE)/2 and pplayer2.right - up1[i].left < (SIZE2+BULLETSIZE) : 
                        rightcounter = 0
                        Rightcount = ((up1[i].right - pplayer2.left) + MOVESPEED2)//MOVESPEED2
                    if ((pplayer2.bottom - up1[i].top)/BULLETSPEED)//MOVESPEED2 == -(pplayer2.right - up1[i].left+MOVESPEED2)/MOVESPEED2//MOVESPEED2 and pplayer2.right - up1[i].left < (SIZE2+BULLETSIZE)/2 and pplayer2.right - up1[i].left > 0:
                        leftcounter = 0
                        Leftcount = ((pplayer2.right - up1[i].left) + MOVESPEED2)//MOVESPEED2
            if len(right1) > 0:
                for i in range(len(right1)):
                    if ((pplayer2.left - right1[i].right)/BULLETSPEED)//MOVESPEED2 == (right1[i].bottom - pplayer2.top +MOVESPEED2)/MOVESPEED2//MOVESPEED2 and pplayer2.bottom - right1[i].top >= (SIZE2+BULLETSIZE)/2 and pplayer2.bottom - right1[i].top < (SIZE2+BULLETSIZE) : 
                        downcounter = 0
                        Downcount = ((right1[i].bottom - pplayer2.top) + MOVESPEED2-1)//MOVESPEED2
                    if ((pplayer2.left - right1[i].right)/BULLETSPEED)//MOVESPEED2 == (pplayer2.bottom - right1[i].top+MOVESPEED2)/MOVESPEED2//MOVESPEED2 and pplayer2.bottom - right1[i].top < (SIZE2+BULLETSIZE)/2 and pplayer2.bottom - right1[i].top > 0:
                        upcounter = 0
                        Upcount = ((pplayer2.bottom - right1[i].top) + MOVESPEED2)//MOVESPEED2
            if len(left1) > 0:
                for i in range(len(left1)):
                    if ((pplayer2.right - left1[i].left)/BULLETSPEED)//MOVESPEED2 == -(left1[i].bottom - pplayer2.top +MOVESPEED2)/MOVESPEED2//MOVESPEED2 and pplayer2.bottom - left1[i].top >= (SIZE2+BULLETSIZE)/2 and pplayer2.bottom - left1[i].top < (SIZE2+BULLETSIZE) : 
                        downcounter = 0
                        Downcount = ((left1[i].bottom - pplayer2.top) +MOVESPEED2)//MOVESPEED2
                    if ((pplayer2.right - left1[i].left)/BULLETSPEED)//MOVESPEED2 == -(pplayer2.bottom - left1[i].top+MOVESPEED2)/MOVESPEED2//MOVESPEED2 and pplayer2.bottom - left1[i].top < (SIZE2+BULLETSIZE)/2 and pplayer2.bottom - left1[i].top > 0:
                        upcounter = 0
                        Upcount = ((pplayer2.bottom - left1[i].top) + MOVESPEED2-1)//MOVESPEED2
            if rightcounter == Rightcount:
                moveRight2 = False
                rightcounter += 1
            if leftcounter == Leftcount:
                moveLeft2 = False
                leftcounter += 1
            if upcounter == Upcount:
                moveUp2 = False
                upcounter += 1
            if downcounter == Downcount:
                moveDown2 = False
                downcounter += 1
            if rightcounter < Rightcount:
                moveRight2 = True
                direction2 = 'right'
                rightcounter += 1
            if upcounter < Upcount:
                moveUp2 = True
                direction2 = 'up'
                upcounter += 1
            if downcounter < Downcount:
                moveDown2 = True
                direction2 = 'down'
                downcounter += 1
            if leftcounter < Leftcount:
                moveLeft2 = True
                direction2 = 'left'
                leftcounter += 1
        
        # don't fire the gun 1
        if FIREBUGTRUE1 and FIREBUG1 < FIREBUGINTERVAL+10:
            FIREBUG1 +=1
        if FIREBUGTRUE2 and FIREBUG2 < FIREBUGINTERVAL+10:
            FIREBUG2 +=1

        # remove the bullet
        if len(up1) > 0:
            if up1[0].top < 0:
                up1crash.append(pygame.Rect(up1[0].left, up1[0].top, BULLETSIZE, BULLETSIZE))              
                up1.remove(up1[0])
                up1c.append(0)
        for i in range(len(up1)):
            up1[i].top -= BULLETSPEED
        if len(down1) > 0:
            if down1[0].bottom > WINDOWHEIGHT:
                down1crash.append(pygame.Rect(down1[0].left, down1[0].top, BULLETSIZE, BULLETSIZE))              
                down1.remove(down1[0])
                down1c.append(0)
        for i in range(len(down1)):
            down1[i].bottom += BULLETSPEED    
        if len(left1) > 0:
            if left1[0].left < 0:
                left1crash.append(pygame.Rect(left1[0].left, left1[0].top, BULLETSIZE, BULLETSIZE))              
                left1.remove(left1[0])
                left1c.append(0)
        for i in range(len(left1)):
            left1[i].left -= BULLETSPEED
        if len(right1) > 0:
            if right1[0].right > WINDOWWIDTH:
                right1crash.append(pygame.Rect(right1[0].left, right1[0].top, BULLETSIZE, BULLETSIZE))              
                right1.remove(right1[0])
                right1c.append(0)
        for i in range(len(right1)):
            right1[i].right += BULLETSPEED
        if len(up2) > 0:
            if up2[0].top < 0:
                up2crash.append(pygame.Rect(up2[0].left, up2[0].top, BULLETSIZE, BULLETSIZE))              
                up2.remove(up2[0])
                up2c.append(0)
        for i in range(len(up2)):
            up2[i].top -= BULLETSPEED
        if len(down2) > 0:
            if down2[0].bottom > WINDOWHEIGHT:
                down2crash.append(pygame.Rect(down2[0].left, down2[0].top, BULLETSIZE, BULLETSIZE))              
                down2.remove(down2[0])
                down2c.append(0)
        for i in range(len(down2)):
            down2[i].bottom += BULLETSPEED
        if len(left2) > 0:
            if left2[0].left < 0:
                left2crash.append(pygame.Rect(left2[0].left, left2[0].top, BULLETSIZE, BULLETSIZE))              
                left2.remove(left2[0])
                left2c.append(0)
        for i in range(len(left2)):
            left2[i].left -= BULLETSPEED 
        if len(right2) > 0:
            if right2[0].right > WINDOWWIDTH:
                right2crash.append(pygame.Rect(right2[0].left, right2[0].top, BULLETSIZE, BULLETSIZE))              
                right2.remove(right2[0])
                right2c.append(0)
        for i in range(len(right2)):
            right2[i].right += BULLETSPEED

        # don't fire the gun 2
        if(fireGun1):
            BULLETINTERVAL1 += 1
        if(fireGun2):
            BULLETINTERVAL2 += 1

        # fire gun
        if fireGun1 and BULLETINTERVAL1 == BULLETGAP and LASER1 == 0:
            if direction1 == 'up':
                up1.append(pygame.Rect(pplayer1.centerx+(SIZE2/10)-(BULLETSIZE/2)-(ICE1*5), pplayer1.top+(SIZE1/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if musicplaying:
                    firesound.play()
            if direction1 == 'down':
                down1.append(pygame.Rect(pplayer1.centerx+(SIZE1/10)-(BULLETSIZE/2)-(ICE1*5), pplayer1.bottom-(SIZE1/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if musicplaying:
                    firesound.play()
            if direction1 == 'left':
                left1.append(pygame.Rect(pplayer1.left+(SIZE1/6)-(BULLETSIZE/2), pplayer1.centery+(SIZE1/10)-(BULLETSIZE/2)-(ICE1*5), BULLETSIZE, BULLETSIZE))
                if musicplaying:
                    firesound.play()
            if direction1 == 'right':
                right1.append(pygame.Rect(pplayer1.right-(SIZE1/6)-(BULLETSIZE/2), pplayer1.centery+(SIZE2/10)-(BULLETSIZE/2)-(ICE1*5), BULLETSIZE, BULLETSIZE))
                if musicplaying:
                    firesound.play()
            BULLETINTERVAL1 = 0
        if fireGun2 and BULLETINTERVAL2 == BULLETGAP and LASER2 == 0:
            if direction2 == 'up':
                up2.append(pygame.Rect(pplayer2.centerx+(SIZE2/10)-(BULLETSIZE/2)-(ICE2*5), pplayer2.top+(SIZE1/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if musicplaying:
                    firesound.play()
            if direction2 == 'down':
                down2.append(pygame.Rect(pplayer2.centerx+(SIZE2/10)-(BULLETSIZE/2)-(ICE2*5), pplayer2.bottom-(SIZE1/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if musicplaying:
                    firesound.play()
            if direction2 == 'left':
                left2.append(pygame.Rect(pplayer2.left+(SIZE2/6)-(BULLETSIZE/2), pplayer2.centery+(SIZE2/10)-(BULLETSIZE/2)-(ICE2*5), BULLETSIZE, BULLETSIZE))
                if musicplaying:
                    firesound.play()
            if direction2 == 'right':
                right2.append(pygame.Rect(pplayer2.right-(SIZE2/6)-(BULLETSIZE/2), pplayer2.centery+(SIZE2/10)-(BULLETSIZE/2)-(ICE2*5), BULLETSIZE, BULLETSIZE))
                if musicplaying:
                    firesound.play()
            BULLETINTERVAL2 = 0

        if LASER1 and fireGun1:
            if direction1 == 'up':
                windowSurface.blit(laserStretchedImage13, uplayer1)
            if direction1 == 'down':
                windowSurface.blit(laserStretchedImage14, dplayer1)
            if direction1 == 'left':
                windowSurface.blit(laserStretchedImage11, lplayer1)
            if direction1 == 'right':
                windowSurface.blit(laserStretchedImage12, rplayer1)
        if LASER2 and fireGun2:
            if direction2 == 'up':
                windowSurface.blit(laserStretchedImage23, uplayer2)
            if direction2 == 'down':
                windowSurface.blit(laserStretchedImage24, dplayer2)
            if direction2 == 'left':
                windowSurface.blit(laserStretchedImage21, lplayer2)
            if direction2 == 'right':
                windowSurface.blit(laserStretchedImage22, rplayer2)
        
        # Ouch!!!
        for i in up1[:]:
            if pplayer2.colliderect(i):
                up1crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))              
                up1c.append(0)
                up1.remove(i)
                if not SHIELD2:
                    if not ICE1:
                        HP2 -= 10
                        if musicplaying:
                            hit.play()
                    if ICE1:
                        HP2 -= 8
                        if musicplaying:
                            hit.play()
                        MOVESPEED2 = 1
        for i in down1[:]:
            if pplayer2.colliderect(i):
                down1crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))
                down1c.append(0)
                down1.remove(i)
                if not SHIELD2:
                    if not ICE1:
                        HP2 -= 10
                        if musicplaying:
                            hit.play()
                    if ICE1:
                        HP2 -= 8
                        if musicplaying:
                            hit.play()
                        MOVESPEED2 = 1
        for i in left1[:]:
            if pplayer2.colliderect(i):
                left1crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))
                left1c.append(0)
                left1.remove(i)
                if not SHIELD2:
                    if not ICE1:
                        HP2 -= 10
                        if musicplaying:
                            hit.play()
                    if ICE1:
                        HP2 -= 8
                        if musicplaying:
                            hit.play()
                        MOVESPEED2 = 1
        for i in right1[:]:
            if pplayer2.colliderect(i):
                right1crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))                          
                right1c.append(0)
                right1.remove(i)
                if not SHIELD2:
                    if not ICE1:
                        HP2 -= 10
                        if musicplaying:
                            hit.play()
                    if ICE1:
                        HP2 -= 8
                        if musicplaying:
                            hit.play()
                        MOVESPEED2 = 1
        for i in up2[:]:
            if pplayer1.colliderect(i):
                up2crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))              
                up2c.append(0)
                up2.remove(i)
                if not SHIELD1:
                    if not ICE2:
                        HP1 -= 10
                        if musicplaying:
                            hit.play()
                    if ICE2:
                        HP1 -= 8
                        if musicplaying:
                            hit.play()
                        MOVESPEED1 = 1
        for i in down2[:]:
            if pplayer1.colliderect(i):
                down2crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))                
                down2c.append(0)
                down2.remove(i)
                if not SHIELD1:
                    if not ICE2:
                        HP1 -= 10
                        if musicplaying:
                            hit.play()
                    if ICE2:
                        HP1 -= 8
                        if musicplaying:
                            hit.play()
                        MOVESPEED1 = 1
        for i in left2[:]:
            if pplayer1.colliderect(i):
                left2crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))
                left2c.append(0)
                left2.remove(i)
                if not SHIELD1:
                    if not ICE2:
                        HP1 -= 10
                        if musicplaying:
                            hit.play()
                    if ICE2:
                        HP1 -= 8
                        if musicplaying:
                            hit.play()
                        MOVESPEED1 = 1
        for i in right2[:]:
            if pplayer1.colliderect(i):
                right2crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))              
                right2c.append(0)
                right2.remove(i)
                if not SHIELD1:
                    if not ICE2:
                        HP1 -= 10
                        if musicplaying:
                            hit.play()
                    if ICE2:
                        HP1 -= 8
                        if musicplaying:
                            hit.play()
                        MOVESPEED1 = 1

        if direction1 == 'up' and LASER1 and fireGun1 and pplayer2.colliderect(uplayer1) and not SHIELD2:
            HP2 -= 1
            if musicplaying:
                hit.play()
        if direction1 == 'down' and LASER1 and fireGun1 and pplayer2.colliderect(dplayer1) and not SHIELD2:
            HP2 -= 1
            if musicplaying:
                hit.play()
        if direction1 == 'left' and LASER1 and fireGun1 and pplayer2.colliderect(lplayer1) and not SHIELD2:
            HP2 -= 1
            if musicplaying:
                hit.play()
        if direction1 == 'right' and LASER1 and fireGun1 and pplayer2.colliderect(rplayer1) and not SHIELD2:
            HP2 -= 1
            if musicplaying:
                hit.play()
        if direction2 == 'up' and LASER2 and fireGun2 and pplayer1.colliderect(uplayer2) and not SHIELD1:
            HP1 -= 1
            if musicplaying:
                hit.play()
        if direction2 == 'down' and LASER2 and fireGun2 and pplayer1.colliderect(dplayer2) and not SHIELD1:
            HP1 -= 1
            if musicplaying:
                hit.play()
        if direction2 == 'left' and LASER2 and fireGun2 and pplayer1.colliderect(lplayer2) and not SHIELD1:
            HP1 -= 1
            if musicplaying:
                hit.play()
        if direction2 == 'right' and LASER2 and fireGun2 and pplayer1.colliderect(rplayer2) and not SHIELD1:
            HP1 -= 1
            if musicplaying:
                hit.play()
            
        if HP1 < 0:
            HP1 += 10
            WINNER = 0
            GAMEEND = 1
            WHO = 1
            bscore += 1
            textnameRect.centerx = windowSurface.get_rect().centerx
            textnameRect.centery = 150
            textstart1Rect.centerx = windowSurface.get_rect().centerx
            textstart1Rect.centery = 290
            textstart2Rect.centerx = windowSurface.get_rect().centerx
            textstart2Rect.centery = 380
            textsettingRect.centerx = windowSurface.get_rect().centerx
            textsettingRect.centery = 470
            textmadeRect.centerx = windowSurface.get_rect().centerx
            textmadeRect.centery = 600
        if HP2 < 0:
            HP2 += 10
            WINNER = 0
            GAMEEND = 1
            WHO = 2
            ascore +=1
            textnameRect.centerx = windowSurface.get_rect().centerx
            textnameRect.centery = 150
            textstart1Rect.centerx = windowSurface.get_rect().centerx
            textstart1Rect.centery = 290
            textstart2Rect.centerx = windowSurface.get_rect().centerx
            textstart2Rect.centery = 380
            textsettingRect.centerx = windowSurface.get_rect().centerx
            textsettingRect.centery = 470
            textmadeRect.centerx = windowSurface.get_rect().centerx
            textmadeRect.centery = 600

        #draw item
        ITEMCOUNTER += 1
        if ITEMCOUNTER >= ITEMTIME and ROBOT == 0:
            ITEMCOUNTER = 0
            if len(itemlist) == 0:
                randem = -1
            else:
                randem = random.randint(0,len(itemlist)-1)
                randem = itemlist[randem]
            if randem == 4:
                while True:
                    randem1 = random.randint(80, WINDOWWIDTH-80-ITEMSIZE)
                    randem2 = random.randint(80, WINDOWHEIGHT-80-ITEMSIZE)
                    ITEM0.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
                    if ITEM0[len(ITEM0)-1].colliderect(pplayer1) or ITEM0[len(ITEM0)-1].colliderect(pplayer2):
                        ITEM0.remove(ITEM0[len(ITEM0)-1])
                    else:
                        ITEM0.remove(ITEM0[len(ITEM0)-1])
                        break
            else:
                while True:
                    randem1= random.randint(0, WINDOWWIDTH - ITEMSIZE)
                    randem2 = random.randint(0, WINDOWHEIGHT - ITEMSIZE)
                    ITEM0.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
                    if ITEM0[len(ITEM0)-1].colliderect(pplayer1) or ITEM0[len(ITEM0)-1].colliderect(pplayer2):
                        ITEM0.remove(ITEM0[len(ITEM0)-1])
                    else:
                        ITEM0.remove(ITEM0[len(ITEM0)-1])
                        break
            if randem == 0:
                ITEM0.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 1:
                ITEM1.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 2:
                ITEM2.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 3:
                ITEM3.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 4:
                ITEM4.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 5:
                ITEM5.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 6:
                ITEM6.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 7:
                ITEM7.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            
        for i in range(len(ITEM0)):
            windowSurface.blit(itemStretchedImage0, ITEM0[i])
        for i in range(len(ITEM1)):
            windowSurface.blit(itemStretchedImage1, ITEM1[i])
        for i in range(len(ITEM2)):
            windowSurface.blit(itemStretchedImage2, ITEM2[i])
        for i in range(len(ITEM3)):
            windowSurface.blit(itemStretchedImage3, ITEM3[i])
        for i in range(len(ITEM4)):
            windowSurface.blit(itemStretchedImage4, ITEM4[i])
        for i in range(len(ITEM5)):
            windowSurface.blit(itemStretchedImage5, ITEM5[i])
        for i in range(len(ITEM6)):
            windowSurface.blit(itemStretchedImage6, ITEM6[i])
        for i in range(len(ITEM7)):
            windowSurface.blit(itemStretchedImage7, ITEM7[i])

        for i in range(len(MINE1)):
            if pplayer2.colliderect(MINE1[i]):
                TRAPPED2 = 1
                moveUp2 = False
                moveDown2 = False
                moveLeft2 = False
                moveRight2 = False
                windowSurface.blit(mineStretchedImage, MINE1[i])
                if MINE1_COUNTER == MINETIME:
                    TRAPPED2 = 0
                    MINE1_COUNTER = 0
                    MINE1.remove(MINE1[i])
                    break
                
        for i in range(len(MINE2)):
            if pplayer1.colliderect(MINE2[i]):
                TRAPPED1 = 1
                moveUp1 = False
                moveDown1 = False
                moveLeft1 = False
                moveRight1 = False
                windowSurface.blit(mineStretchedImage, MINE2[i])
                if MINE2_COUNTER == MINETIME:
                    TRAPPED1 = 0
                    MINE2_COUNTER = 0
                    MINE2.remove(MINE2[i])
                    break

        if TRAPPED1:
            MINE2_COUNTER += 1
        if TRAPPED2:
            MINE1_COUNTER += 1

        if moveUp1 and pplayer1.top > 0:
            pplayer1.top -= MOVESPEED1
        if moveDown1 and pplayer1.bottom < WINDOWHEIGHT:
            pplayer1.top += MOVESPEED1
        if moveLeft1 and pplayer1.left > 0:
            pplayer1.left -= MOVESPEED1
        if moveRight1 and pplayer1.right < WINDOWWIDTH:
            pplayer1.right += MOVESPEED1
        if moveUp2 and pplayer2.top > 0:
            pplayer2.top -= MOVESPEED2
        if moveDown2 and pplayer2.bottom < WINDOWHEIGHT:
            pplayer2.top += MOVESPEED2
        if moveLeft2 and pplayer2.left > 0:
            pplayer2.left -= MOVESPEED2
        if moveRight2 and pplayer2.right < WINDOWWIDTH:
            pplayer2.right += MOVESPEED2

        skull1 = pygame.Rect(pplayer1.left, pplayer1.top, SIZE1, SIZE1)
        skull2 = pygame.Rect(pplayer2.left, pplayer2.top, SIZE2, SIZE2)

        if direction1 == 'up' and not fireGun1:
            windowSurface.blit(playerStretchedImage1cu, pplayer1)
        if direction1 == 'down' and not fireGun1:
            windowSurface.blit(playerStretchedImage1cd, pplayer1)
        if direction1 == 'left' and not fireGun1:
            windowSurface.blit(playerStretchedImage1cl, pplayer1)
        if direction1 == 'right' and not fireGun1:
            windowSurface.blit(playerStretchedImage1cr, pplayer1)
        if direction1 == 'up' and fireGun1:
            windowSurface.blit(playerStretchedImage1ou, pplayer1)
        if direction1 == 'down' and fireGun1:
            windowSurface.blit(playerStretchedImage1od, pplayer1)
        if direction1 == 'left' and fireGun1:
            windowSurface.blit(playerStretchedImage1ol, pplayer1)
        if direction1 == 'right' and fireGun1:
            windowSurface.blit(playerStretchedImage1or, pplayer1)
        pygame.draw.rect(windowSurface, WHITE, (pplayer1.left, pplayer1.top - 10, pplayer1.width, 5))
        pygame.draw.rect(windowSurface, RED, (pplayer1.left, pplayer1.top - 10, HP1*pplayer1.width/player1.width, 5))

        if not defencemode:
            if direction2 == 'up' and not fireGun2:
                windowSurface.blit(playerStretchedImage2cu, pplayer2)
            if direction2 == 'down' and not fireGun2:
                windowSurface.blit(playerStretchedImage2cd, pplayer2)
            if direction2 == 'left' and not fireGun2:
                windowSurface.blit(playerStretchedImage2cl, pplayer2)
            if direction2 == 'right' and not fireGun2:
                windowSurface.blit(playerStretchedImage2cr, pplayer2)
            if direction2 == 'up' and fireGun2:
                windowSurface.blit(playerStretchedImage2ou, pplayer2)
            if direction2 == 'down' and fireGun2:
                windowSurface.blit(playerStretchedImage2od, pplayer2)
            if direction2 == 'left' and fireGun2:
                windowSurface.blit(playerStretchedImage2ol, pplayer2)
            if direction2 == 'right' and fireGun2:
                windowSurface.blit(playerStretchedImage2or, pplayer2)
            pygame.draw.rect(windowSurface, WHITE, (pplayer2.left, pplayer2.top - 10, pplayer2.width, 5))
            pygame.draw.rect(windowSurface, RED, (pplayer2.left, pplayer2.top - 10, HP2*pplayer2.width/player2.width, 5))

        if SKULL1:
            windowSurface.blit(skullStretchedImage1, skull1)
        if SKULL2:
            windowSurface.blit(skullStretchedImage2, skull2)

        if SISE1:
            SISE1_COUNTER += 1
        if SISE1_COUNTER >= SISETIME:
            SISE1 = 0
            SISE1_COUNTER = 0
            SIZE2 -= 30
            pplayer2.left += 15
            pplayer2.top += 15
        if SISE2:
            SISE2_COUNTER += 1
        if SISE2_COUNTER >= SISETIME:
            SISE2 = 0
            SISE2_COUNTER = 0
            SIZE1 -= 30
            pplayer1.left += 15
            pplayer1.top += 15

        if ICE1:
            ICE1_COUNTER += 1
        if ICE1_COUNTER >= ICETIME:
            ICE1 = 0
            ICE1_COUNTER = 0
            MOVESPEED2 = 3
        if ICE2:
            ICE2_COUNTER += 1
        if ICE2_COUNTER >= ICETIME:
            ICE2 = 0
            ICE2_COUNTER = 0
            MOVESPEED1 = 3

        if LASER1:
            LASER1_COUNTER += 1
        if LASER1_COUNTER >= LASERTIME:
            LASER1 = 0
            LASER1_COUNTER = 0
        if LASER2:
            LASER2_COUNTER += 1
        if LASER2_COUNTER >= LASERTIME:
            LASER2 = 0
            LASER2_COUNTER = 0

        if SHIELD1:
            pygame.draw.circle(windowSurface, SHIELD, (pplayer1.centerx, pplayer1.centery), 35, 2)
            SHIELD1_COUNTER += 1
        if SHIELD1_COUNTER >= SHIELDTIME:
            SHIELD1 = 0
            SHIELD1_COUNTER = 0
        if SHIELD2:
            pygame.draw.circle(windowSurface, SHIELD, (pplayer2.centerx, pplayer2.centery), 35, 2)
            SHIELD2_COUNTER += 1
        if SHIELD2_COUNTER >= SHIELDTIME:
            SHIELD2 = 0
            SHIELD2_COUNTER = 0

        if TURRET1:
            TURRET1_COUNTER += 1
        if TURRET1_COUNTER >= TURRETTIME:
            TURRET1 = 0
            TURRET1_COUNTER = 0
        if TURRET2:
            TURRET2_COUNTER += 1
        if TURRET2_COUNTER >= TURRETTIME:
            TURRET2 = 0
            TURRET2_COUNTER = 0

        if SKULL1 or SKULL2:
            SKULL_COUNTER += 1
        if SKULL_COUNTER >= SKULLTIME:
            SKULL1 = 0
            SKULL2 = 0
            SKULL_COUNTER = 0
                
        if TURRET1:
            if TURRET_direction1 == 'up':
                windowSurface.blit(turretStretchedImage11, turret1)
            if TURRET_direction1 == 'down':
                windowSurface.blit(turretStretchedImage12, turret1)
            if TURRET_direction1 == 'left':
                windowSurface.blit(turretStretchedImage13, turret1)
            if TURRET_direction1 == 'right':
                windowSurface.blit(turretStretchedImage14, turret1)
            if TURRET1_COUNTER % 15 == 1:
                if TURRET_direction1 == 'up':
                    up1.append(pygame.Rect(turret1.centerx+(50/10)-(BULLETSIZE/2), turret1.top+(50/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if TURRET_direction1 == 'down':
                    down1.append(pygame.Rect(turret1.centerx+(50/10)-(BULLETSIZE/2), turret1.bottom-(50/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if TURRET_direction1 == 'left':
                    left1.append(pygame.Rect(turret1.left+(50/6)-(BULLETSIZE/2), turret1.centery+(50/10)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if TURRET_direction1 == 'right':
                    right1.append(pygame.Rect(turret1.right-(50/6)-(BULLETSIZE/2), turret1.centery+(50/10)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
        if TURRET2:
            if TURRET_direction2 == 'up':
                windowSurface.blit(turretStretchedImage21, turret2)
            if TURRET_direction2 == 'down':
                windowSurface.blit(turretStretchedImage22, turret2)
            if TURRET_direction2 == 'left':
                windowSurface.blit(turretStretchedImage23, turret2)
            if TURRET_direction2 == 'right':
                windowSurface.blit(turretStretchedImage24, turret2)
            if TURRET2_COUNTER % 15 == 1:
                if TURRET_direction2 == 'up':
                    up2.append(pygame.Rect(turret2.centerx+(50/10)-(BULLETSIZE/2), turret2.top+(50/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if TURRET_direction2 == 'down':
                    down2.append(pygame.Rect(turret2.centerx+(50/10)-(BULLETSIZE/2), turret2.bottom-(50/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if TURRET_direction2 == 'left':
                    left2.append(pygame.Rect(turret2.left+(50/6)-(BULLETSIZE/2), turret2.centery+(50/10)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if TURRET_direction2 == 'right':
                    right2.append(pygame.Rect(turret2.right-(50/6)-(BULLETSIZE/2), turret2.centery+(50/10)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
        
        # draw the bullet
        for i in range(len(up1)):
            if not ICE1:
                windowSurface.blit(bulletStretchedImage11, up1[i])
            if ICE1:
                windowSurface.blit(bulletStretchedImagei, up1[i])
        for i in range(len(down1)):
            if not ICE1:
                windowSurface.blit(bulletStretchedImage12, down1[i])
            if ICE1:
                windowSurface.blit(bulletStretchedImagei, down1[i])
        for i in range(len(left1)):
            if not ICE1:
                windowSurface.blit(bulletStretchedImage13, left1[i])
            if ICE1:
                windowSurface.blit(bulletStretchedImagei, left1[i])
        for i in range(len(right1)):
            if not ICE1:
                windowSurface.blit(bulletStretchedImage14, right1[i])
            if ICE1:
                windowSurface.blit(bulletStretchedImagei, right1[i])
        for i in range(len(up2)):
            if not ICE2:
                windowSurface.blit(bulletStretchedImage21, up2[i])
            if ICE2:
                windowSurface.blit(bulletStretchedImagei, up2[i])
        for i in range(len(down2)):
            if not ICE2:
                windowSurface.blit(bulletStretchedImage22, down2[i])
            if ICE2:
                windowSurface.blit(bulletStretchedImagei, down2[i])
        for i in range(len(left2)):
            if not ICE2:
                windowSurface.blit(bulletStretchedImage23, left2[i])
            if ICE2:
                windowSurface.blit(bulletStretchedImagei, left2[i])
        for i in range(len(right2)):
            if not ICE2:
                windowSurface.blit(bulletStretchedImage24, right2[i])
            if ICE2:
                windowSurface.blit(bulletStretchedImagei, right2[i])

        for i in range(len(up1crash)):
            if up1c[i] < 10:
                windowSurface.blit(bulletStretchedImagec21, up1crash[i])
                up1c[i] += 1
            if up1c[i] == 0:
                up1c.remove(i)
                up1crash.remove(i)
        for i in range(len(down1crash)):
            if down1c[i] < 10:
                windowSurface.blit(bulletStretchedImagec22, down1crash[i])
                down1c[i] += 1
            if down1c[i] == 0:
                down1c.remove(i)
                down1crash.remove(i)
        for i in range(len(left1crash)):
            if left1c[i] < 10:
                windowSurface.blit(bulletStretchedImagec23, left1crash[i])
                left1c[i] += 1
            if left1c[i] == 0:
                left1c.remove(i)
                left1crash.remove(i)
        for i in range(len(right1crash)):
            if right1c[i] < 10:
                windowSurface.blit(bulletStretchedImagec24, right1crash[i])
                right1c[i] += 1
            if right1c[i] == 0:
                right1c.remove(i)
                right1crash.remove(i)

        for i in range(len(up2crash)):
            if up2c[i] < 10:
                windowSurface.blit(bulletStretchedImagec21, up2crash[i])
                up2c[i] += 1
            if up2c[i] == 0:
                up2c.remove(i)
                up2crash.remove(i)
        for i in range(len(down2crash)):
            if down2c[i] < 10:
                windowSurface.blit(bulletStretchedImagec22, down2crash[i])
                down2c[i] += 1
            if down2c[i] == 0:
                down2c.remove(i)
                down2crash.remove(i)
        for i in range(len(left2crash)):
            if left2c[i] < 10:
                windowSurface.blit(bulletStretchedImagec23, left2crash[i])
                left2c[i] += 1
            if left2c[i] == 0:
                left2c.remove(i)
                left2crash.remove(i)
        for i in range(len(right2crash)):
            if right2c[i] < 10:
                windowSurface.blit(bulletStretchedImagec24, right2crash[i])
                right2c[i] += 1
            if right2c[i] == 0:
                right2c.remove(i)
                right2crash.remove(i)

        if not defencemode and not attackmode:
            textScore = basicFont2.render('%d : %d'%(ascore,bscore), True, WHITE)    
            textScoreRect = textScore.get_rect()
            textScoreRect.centery = 30
            textScoreRect.centerx = int(WINDOWWIDTH/2)
            windowSurface.blit(textScore, textScoreRect)
        
        for i in ITEM0[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                SIZE2 += 30
                if pplayer2.top>15 and pplayer2.bottom<WINDOWHEIGHT-15:
                    pplayer2.top -= 15
                if pplayer2.bottom>WINDOWHEIGHT-15:
                    pplayer2.bottom -= 30
                if pplayer2.left>15 and pplayer2.right<WINDOWWIDTH-15:
                    pplayer2.left -= 15
                if pplayer2.right>WINDOWWIDTH-15:
                    pplayer2.left -= 30
                ITEM0.remove(i)
                if musicplaying:
                    bigger.play()
                SISE1 = 1
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                SIZE1 += 30
                if pplayer1.top>15 and pplayer1.bottom<WINDOWHEIGHT-15:
                    pplayer1.top -= 15
                if pplayer1.bottom>WINDOWHEIGHT-15:
                    pplayer1.bottom -= 30
                if pplayer1.left>15 and pplayer1.right<WINDOWWIDTH-15:
                    pplayer1.left -= 15
                if pplayer1.right>WINDOWWIDTH-15:
                    pplayer1.left -= 30
                ITEM0.remove(i)
                if musicplaying:
                    bigger.play()
                SISE2 = 1
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                SIZE1 += 30
                SIZE2 += 30
                if pplayer2.top>15 and pplayer2.bottom<WINDOWHEIGHT-15:
                    pplayer2.top -= 15
                if pplayer2.bottom>WINDOWHEIGHT-15:
                    pplayer2.bottom -= 30
                if pplayer2.left>15 and pplayer2.right<WINDOWWIDTH-15:
                    pplayer2.left -= 15
                if pplayer2.right>WINDOWWIDTH-15:
                    pplayer2.left -= 30
                if pplayer1.top>15 and pplayer1.bottom<WINDOWHEIGHT-15:
                    pplayer1.top -= 15
                if pplayer1.bottom>WINDOWHEIGHT-15:
                    pplayer1.bottom -= 30
                if pplayer1.left>15 and pplayer1.right<WINDOWWIDTH-15:
                    pplayer1.left -= 15
                if pplayer1.right>WINDOWWIDTH-15:
                    pplayer1.left -= 30
                ITEM0.remove(i)
                if musicplaying:
                    bigger.play()
                SISE1 = 1
                SISE2 = 1
        for i in ITEM1[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                ICE1 = 1
                ITEM1.remove(i)
                if musicplaying:
                    install.play()
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                ICE2 = 1
                ITEM1.remove(i)
                if musicplaying:
                    install.play()
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                ICE1 = 1
                ICE2 = 1
                ITEM1.remove(i)
                if musicplaying:
                    install.play()
        for i in ITEM2[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                LASER1 = 1
                ITEM2.remove(i)
                if musicplaying:
                    install.play()
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                LASER2 = 1
                ITEM2.remove(i)
                if musicplaying:
                    install.play()
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                LASER1 = 1
                LASER2 = 1
                ITEM2.remove(i)
                if musicplaying:
                    install.play()
        for i in ITEM3[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                SHIELD1 = 1
                pplayer1.top = random.randint(pplayer2.top-100, pplayer2.bottom+50)
                pplayer1.left = random.randint(pplayer2.left-100, pplayer2.right+50)
                ITEM3.remove(i)
                if musicplaying:
                    install.play()
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                SHIELD2 = 1
                pplayer2.top = random.randint(pplayer1.top-100, pplayer1.bottom+50)
                pplayer2.left = random.randint(pplayer1.left-100, pplayer1.right+50)
                ITEM3.remove(i)
                if musicplaying:
                    install.play()
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                SHIELD1 = 1
                SHIELD2 = 1
                pplayer1.top = random.randint(0, WINDOWHEIGHT - pplayer1.height)
                pplayer1.left = random.randint(0, WINDOWWIDTH - pplayer1.width)
                pplayer2.top = random.randint(0, WINDOWHEIGHT - pplayer1.height)
                pplayer2.left = random.randint(0, WINDOWWIDTH - pplayer1.width)
                ITEM3.remove(i)
                if musicplaying:
                    install.play()
        for i in ITEM4[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                TURRET1 = 1
                TURRET1_COUNTER = 0
                TURRET_direction1 = direction1
                turret1.left = i.left
                turret1.top = i.top
                ITEM4.remove(i)
                if musicplaying:
                    mine.play()
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                TURRET2 = 1
                TURRET2_COUNTER = 0
                TURRET_direction2= direction2
                turret2.left = i.left
                turret2.top = i.top
                ITEM4.remove(i)
                if musicplaying:
                    mine.play()
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                TURRET1 = 1
                TURRET2 = 1
                TURRET1_COUNTER = 0
                TURRET2_COUNTER = 0
                TURRET_direction1 = direction1
                TURRET_direction2 = direction2
                turret1.left = i.left
                turret1.top = i.top
                turret2.left = i.left
                turret2.top = i.top
                ITEM4.remove(i)
                if musicplaying:
                    mine.play()
        for i in ITEM5[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                if HP1 < player1.width:
                    HP1 += 10
                ITEM5.remove(i)
                if musicplaying:
                    heal.play()
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                if HP2 < player2.width:
                    HP2 += 10
                ITEM5.remove(i)
                if musicplaying:
                    heal.play()
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                if HP1 < player1.width:
                    HP1 += 10
                if HP2 < player2.width:
                    HP2 += 10
                ITEM5.remove(i)
                if musicplaying:
                    heal.play()
        for i in ITEM6[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                SKULL2 = 1
                ITEM6.remove(i)
                if musicplaying:
                    install.play()
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                SKULL1 = 1
                ITEM6.remove(i)
                if musicplaying:
                    install.play()
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                SKULL1 = 1
                SKULL2 = 1
                ITEM6.remove(i)
                if musicplaying:
                    install.play()
        for i in ITEM7[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                MINE1.append(pygame.Rect(i.left, i.top, ITEMSIZE, ITEMSIZE))
                ITEM7.remove(i)
                if musicplaying:
                    install.play()
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                MINE2.append(pygame.Rect(i.left, i.top, ITEMSIZE, ITEMSIZE))
                ITEM7.remove(i)
                if musicplaying:
                    install.play()
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                MINE1.append(pygame.Rect(i.left, i.top, ITEMSIZE, ITEMSIZE))
                MINE2.append(pygame.Rect(i.left, i.top, ITEMSIZE, ITEMSIZE))
                ITEM7.remove(i)
                if musicplaying:
                    install.play()
        if attackmode:
            if moveUp1 and pplayer1.top < WINDOWHEIGHT/3*2 + BULLETSIZE/2 and pplayer1.bottom > WINDOWHEIGHT/3*2 + BULLETSIZE/2  and pplayer1.right > WINDOWWIDTH/3 and pplayer1.left < WINDOWWIDTH/3*2:
                pplayer1.top += MOVESPEED1
            if moveDown1 and pplayer1.bottom > WINDOWHEIGHT/3 + BULLETSIZE/2 and pplayer1.top < WINDOWHEIGHT/3 + BULLETSIZE/2 and pplayer1.right > WINDOWWIDTH/3 and pplayer1.left < WINDOWWIDTH/3*2:
                pplayer1.top -= MOVESPEED1
            if moveRight1 and pplayer1.right > WINDOWWIDTH/3 and pplayer1.left < WINDOWWIDTH/3 and pplayer1.bottom > WINDOWHEIGHT/3 and pplayer1.top < WINDOWHEIGHT/3*2:
                pplayer1.left -= MOVESPEED1
            if moveLeft1 and pplayer1.left < WINDOWWIDTH/3*2 and pplayer1.right > WINDOWWIDTH/3*2 and pplayer1.bottom > WINDOWHEIGHT/3 and pplayer1.top < WINDOWHEIGHT/3*2:
                pplayer1.right += MOVESPEED1
                
            if pplayer2.top < WINDOWHEIGHT/3*2 + BULLETSIZE/2 and pplayer2.bottom > WINDOWHEIGHT/3*2 + BULLETSIZE/2:
                pplayer2.centerx = WINDOWWIDTH/2
                pplayer2.centery = WINDOWHEIGHT/2 + SIZE2/2
            if pplayer2.bottom > WINDOWHEIGHT/3 + BULLETSIZE/2 and pplayer2.top < WINDOWHEIGHT/3 + BULLETSIZE/2:
                pplayer2.centerx = WINDOWWIDTH/2
                pplayer2.centery = WINDOWHEIGHT/2 + SIZE2/2
            if pplayer2.right > WINDOWWIDTH/3 and pplayer2.left < WINDOWWIDTH/3:
                pplayer2.centerx = WINDOWWIDTH/2
                pplayer2.centery = WINDOWHEIGHT/2 
            if pplayer2.left < WINDOWWIDTH/3*2 and pplayer2.right > WINDOWWIDTH/3*2:
                pplayer2.centerx = WINDOWWIDTH/2
                pplayer2.centery = WINDOWHEIGHT/2
        # draw the window onto the screen
        pygame.display.update()
        mainClock.tick(SPEED)
    if musicplaying:
        pygame.mixer.music.stop()
    r = random.randint(0,3)
    if defencemode:
        r =2
    if r == 0:
        if musicplaying:
            pygame.mixer.music.load('death.mp3')
            pygame.mixer.music.play(1,0.0)
    if r == 1:
        if musicplaying:
            pygame.mixer.music.load('twisted.mp3')
            pygame.mixer.music.play(1,0.0)
    if r == 2:
        if musicplaying:
            pygame.mixer.music.load('laugh.mp3')
            pygame.mixer.music.play(1,0.0)
    if r == 3:
        if musicplaying:
            pygame.mixer.music.load('fool.mp3')
            pygame.mixer.music.play(1,0.0)
    while GAMEEND:
        windowSurface.blit(mainStretchedImage, (0,0))
        mousex = 0
        text = basicFont2.render('GO TO MAIN SCREEN', True, WHITE)
        text1Rect = text1.get_rect()
        text2Rect = text2.get_rect()
        textRect = text.get_rect()
        text1Rect.centerx = windowSurface.get_rect().centerx
        text1Rect.centery = int(WINDOWHEIGHT/3)
        text2Rect.centerx = windowSurface.get_rect().centerx
        text2Rect.centery = int(WINDOWHEIGHT/3)
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = windowSurface.get_rect().centery
        wantrestart = basicFont2.render('RESTART', True, WHITE)
        wantrestartRect = wantrestart.get_rect()
        wantrestartRect.centerx = windowSurface.get_rect().centerx
        wantrestartRect.centery = int(WINDOWHEIGHT*2/3)
        if not defencemode and not attackmode:
            if WHO == 1:
                windowSurface.blit(text2, text2Rect)
            if WHO == 2 :
                windowSurface.blit(text1, text1Rect)
        windowSurface.blit(text,textRect)
        windowSurface.blit(wantrestart, wantrestartRect)
        mousey = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
        if mousey > textRect.top and mousey < textRect.bottom and mousex > textRect.left and mousex < textRect.right:
            GAMEEND = 0
            GAMESTART = 1
        if mousex >= wantrestartRect.left and mousex <= wantrestartRect.right and mousey >= wantrestartRect.top and mousey <= wantrestartRect.bottom:
            GAMEEND = 0
            WINNER = 1

        # draw the window onto the screen
        pygame.display.update()
        mainClock.tick(SPEED)

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(SPEED)
# ITEM: 0:?????? ??????, 1:????????? ??????, 2:?????????, 3:????????????, 4:??????, 5:??????, 6:??????, 7:??????
