import consts
import pygame
import screen
import random


# train
def draw_train(scrn):
    train = {"x_val": 240, "y_val": 240}
    consts.TRAIN = pygame.transform.scale(consts.TRAIN, (100, 100))
    scrn.blit(consts.TRAIN, (240, 240))
    pygame.display.flip()
    return train


# npc

def add_to_npc_list():
    npc_list = [consts.npc1, consts.npc2, consts.npc3, consts.npc4, consts.npc5, consts.npc6, consts.npc7, consts.npc8, consts.npc9, consts.npc10, consts.npc11,consts.npc12, consts.npc13, consts.npc14]
    return npc_list


def pick_rand_npc():
    npc_list = add_to_npc_list()
    choose_npc = random.choice(npc_list)
    return choose_npc


def draw_npc(scrn, npc):
    npc = pick_rand_npc()
    npc = {"x_val": 240, "y_val": 240}
    for i in range(5):
        consts.npc = pygame.transform.scale(consts.npc, (100, 100))
        scrn.blit(consts.npc, (100, 100))
    pygame.display.flip()
    # return train
