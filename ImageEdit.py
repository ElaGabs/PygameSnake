import consts
import pygame
import screen


def draw_train(scrn):
    train = {"x_val": 500, "y_val": 500}
    consts.TRAIN = pygame.transform.scale(consts.TRAIN, (100, 100))
    scrn.blit(consts.TRAIN, (240, 240))
    pygame.display.flip()
    return train
