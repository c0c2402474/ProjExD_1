import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk3_img = pg.image.load("fig/3.png")#こうかとん2
    kk3_img = pg.transform.flip(kk3_img, True, False)#こうかとん反転2
    bg2_img = pg.transform.flip(bg_img, True, False)#背景反転8
    tmr = 0
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr
        screen.blit(bg_img, [-x, 0])#背景移動6
        screen.blit(bg2_img, [-x+1600, 0])#ｂｇ二枚目7
        screen.blit(kk3_img, [300, 200])#こうかとん反映4
        pg.display.update()
        tmr += 1        
        clock.tick(200)#FPS変更５


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()