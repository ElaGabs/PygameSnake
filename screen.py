import random
import pygame
import consts
import ImageEdit

scrn = pygame.display.set_mode((consts.WIDTH, consts.HEIGHT))


def draw_game():
    npc = ImageEdit.pick_rand_npc()
    ImageEdit.draw_npc(scrn, npc)
    ImageEdit.draw_train(scrn)
