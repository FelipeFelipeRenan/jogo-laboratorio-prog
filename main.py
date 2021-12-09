import pygame as pg

LARGURA = 650
ALTURA = 500
blau = (0, 0, 255)
weiss = (255, 255, 255)
rot = (255, 0, 0)

pos_x = LARGURA/2
pos_y = ALTURA/2
tamanho = 10


def jooj():
    try:
        pg.init()
    except:
        print("ERROR")

    fundo = pg.display.set_mode((LARGURA, ALTURA))
    pg.display.set_caption("jooj")

    loop = True

    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = False
        fundo.fill(blau)
        pg.draw.rect(fundo, rot, [pos_x, pos_y, tamanho, tamanho])
        pg.display.update()

    pg.quit()


if __name__ == '__main__':
    jooj()



