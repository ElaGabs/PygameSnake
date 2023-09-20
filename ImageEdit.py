import consts
import pygame
import screen


def draw_train(scrn):
    train = {"x_val": 240, "y_val": 240}
    consts.TRAIN = pygame.transform.scale(consts.TRAIN, (100, 100))
    scrn.blit(consts.TRAIN, (240, 240))
    pygame.display.flip()
    return train
