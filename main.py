import pygame as pg
from random import randint

LARGURA = 650
ALTURA = 500
blau = (0, 0, 255)
weiss = (255, 255, 255)
rot = (255, 0, 0)


tamanho = 10


def jooj():
    try:
        pg.init()
    except:
        print("ERROR")

    pos_x = LARGURA/2
    pos_y = ALTURA-30
    pos_y_car = ALTURA - randint(40, ALTURA - tamanho)
    pos_x_car = LARGURA - randint(50, LARGURA - tamanho)
    tamanho_car = tamanho+randint(5, 10)
    velocidade_x = 0
    clock = pg.time.Clock()

    fundo = pg.display.set_mode((LARGURA, ALTURA))
    pg.display.set_caption("jooj")

    loop = True
    while loop:
        pos_y_car = ALTURA - randint(40, ALTURA - tamanho)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    pos_x -= 10
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    pos_x += 10
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP or event.key == pg.K_w:
                    pos_y -= 10
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN or event.key == pg.K_s:
                    pos_y += 10

        pg.draw.rect(fundo, rot, [pos_x_car, pos_y_car, tamanho_car, tamanho_car])
        fundo.fill(blau)
        pg.draw.rect(fundo, weiss, [pos_x, pos_y, tamanho, tamanho])
        velocidade_x += 0.5
        pg.display.update()
        clock.tick(15)

    pg.quit()


if __name__ == '__main__':
    jooj()



