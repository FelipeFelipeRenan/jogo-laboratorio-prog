import pygame as pg

LARGURA = 650
ALTURA = 500


def jooj():
    try:
        pg.init()
    except:
        print("ERROR")

    pg.display.set_mode((LARGURA, ALTURA))
    pg.display.set_caption("jooj")

    loop = True

    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = False
        pg.display.update()

    pg.quit()


if __name__ == '__main__':
    jooj()



