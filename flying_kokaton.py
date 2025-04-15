import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img, True, False)#背景反転8
    kk3_img = pg.image.load("fig/3.png")#こうかとん2
    kk3_img = pg.transform.flip(kk3_img, True, False)#こうかとん反転2
    kk3_rct = kk3_img.get_rect()#rect抽出１０
    kk3_rct.center = 300,200#初期座標１０
    tate = 0
    yoko = 0
    tmr = 0
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = pg.key.get_pressed()#キー検知１０－３
        if key_lst[pg.K_UP]:#こうかとん移動10-4
            yoko = -1
            tate = -1

            # kk3_rct.move_ip((0, -1))
        elif key_lst[pg.K_DOWN]:
            yoko = -1
            tate = 1
            # kk3_rct.move_ip((0, 1))
        elif key_lst[pg.K_RIGHT]:
            yoko = 2
            tate = 0
            # kk3_rct.move_ip((2, 0))
        elif key_lst[pg.K_LEFT]:
            yoko = -2
            tate = 0
            # kk3_rct.move_ip((-2, 0))
        else:#押してないとき左に動く
            yoko = -1
            tate = 0
            # kk3_rct.move_ip((-1, 0))
        kk3_rct.move_ip((yoko,tate))
        x = tmr % 3200#ループ９
        # y = 200
        screen.blit(bg_img, [-x, 0])#背景移動6
        screen.blit(bg2_img, [-x+1600, 0])#ｂｇ二枚目7
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(kk3_img, kk3_rct)#こうかとん反映4
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)#FPS変更５


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()