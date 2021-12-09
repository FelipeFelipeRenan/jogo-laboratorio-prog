import pygame as pg
from random import randint, choice

LARGURA = 650
ALTURA = 500
blau = (0, 0, 255)
weiss = (255, 255, 255)
rot = (255, 0, 0)
scharz = (0, 0, 0)
grun = (0, 0, 0)


tamanho = 10


def jooj():
    try:
        pg.init()
    except:
        print("ERROR")

    pos_x = LARGURA/2
    pos_y = ALTURA-30
    pos_x_car = LARGURA - tamanho
    tamanho_car = tamanho+randint(5, 10)
    velocidade_x = 0
    clock = pg.time.Clock()
    ##pos_y_car = ALTURA - randint(40, ALTURA - tamanho)
    ##pos_x_car = LARGURA - randint(50, LARGURA - tamanho)
    pos_cars = []

    for i in range(0, 5, 1):
        pos_cars.append(randint(40, ALTURA - tamanho))

        #pos_cars[i] = i
    fundo = pg.display.set_mode((LARGURA, ALTURA))
    pg.display.set_caption("jooj")

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
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

        fundo.fill(blau)

        pg.draw.rect(fundo, weiss, [pos_x, pos_y, tamanho, tamanho])

        pg.draw.rect(fundo, rot, [pos_x_car, choice(pos_cars), tamanho_car, tamanho_car])
        pg.draw.rect(fundo, weiss, [pos_x_car, choice(pos_cars), tamanho_car, tamanho_car])
        pg.draw.rect(fundo, scharz, [pos_x_car, choice(pos_cars), tamanho_car, tamanho_car])
        pg.draw.rect(fundo, grun, [pos_x_car, choice(pos_cars), tamanho_car, tamanho_car])
        pg.draw.rect(fundo, rot, [pos_x_car, choice(pos_cars), tamanho_car, tamanho_car])

        velocidade_x += 0.5
        pos_x_car -= velocidade_x

        pg.display.update()
        clock.tick(5)

    pg.quit()


if __name__ == '__main__':
    jooj()



