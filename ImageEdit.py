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
# def draw_npc(scrn):
#     npc = {"x_val": 240, "y_val": 240}
#     consts.TRAIN = pygame.transform.scale(consts.TRAIN, (100, 100))
#     scrn.blit(consts.TRAIN, (240, 240))
#     pygame.display.flip()
#     return train

def add_to_npc_list(npc1, npc2, npc3, npc4, npc5):
    npc_list = [npc1, npc2, npc3, npc4, npc5]
    return npc_list


def pick_rand_npc(npc_list):
    npc_list = add_to_npc_list(consts.npc1, consts.npc2, consts.npc3, consts.npc4, consts.npc5)
    choose_npc = random.choice(npc_list)
    return choose_npc


def draw_npc(scrn, npc):
    npc = pick_rand_npc(npc_list)
    npc = {"x_val": 240, "y_val": 240}
    for i in range(5):
        consts.npc = pygame.transform.scale(consts.npc, (100, 100))
        scrn.blit(consts.npc, (100, 100))
    pygame.display.flip()
    # return train
