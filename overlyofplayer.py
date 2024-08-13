import pygame
from setting import *
from math import sqrt


class overlay(pygame.sprite.Sprite):
    def __init__(self,hex,all_sprites,player_name) -> None:
        super().__init__(all_sprites)
        size=(50,50)


        x = (size[0]-24 )* (3/2 * hex[1])-9
        y = ((size[1]-20) * (sqrt(3)/2 * hex[1] +  sqrt(3) * hex[0])-500)-16



        

        self.size=flagsize

        self.image=overlay_images.get(player_name)
        # self.blueflag=pygame.image.load('D:/Afraz/assets/overlay/Red Flag.png').convert_alpha()

        self.image=pygame.transform.scale(self.image,(25,25))
        self.rect=self.image.get_rect(center=(x,y))
        # self.blueflag=pygame.transform.scale(self.image,self.size)



    

            