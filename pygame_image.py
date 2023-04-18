import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230418/fig/pg_bg.jpg")
    r_bg_img = pg.transform.flip(bg_img, True, False) 
    kt_img = pg.image.load("ex01-20230418/fig/3.png")
    kt_img = pg.transform.flip(kt_img, True, False)
    kt_imgs = [kt_img, pg.transform.rotozoom(kt_img, 10, 1.0)]
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x = tmr%3200
        
        hane = int((tmr/20)%2)

        screen.blit(bg_img, [-x, 0])
        screen.blit(r_bg_img, [1600 -x, 0])
        screen.blit(bg_img, [3200 -x, 0])
        screen.blit(r_bg_img, [4800 -x, 0])
        
    

        screen.blit(kt_imgs[hane], [300, 200])

        
        
        
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()