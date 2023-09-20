import consts
import pygame
import screen

def draw_train(scrn):
    train = {"x_val": 500, "y_val": 500}
    consts.SOLDIER = pygame.transform.scale(consts.SOLDIER, (80, 80))
    scrn.blit(consts.SOLDIER, (0, 0))
    pygame.display.flip()
    return soldier