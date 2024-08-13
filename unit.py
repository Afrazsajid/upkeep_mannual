import pygame
from setting import *
from random import randint



class unit(pygame.sprite.Sprite):
    def __init__(self, groups,pos,row,col,unit_no,unit_lst):
        self.unit_no=unit_no
        self.unit_lst=unit_lst
        super().__init__(groups)
        self.row=row
        self.col=col

        
        
        self.size=(round(tile_size[0]*0.76),round(tile_size[0]*0.76))
        
        self.image=self.random_unit(row,col)
        self.image=pygame.transform.scale(self.image,self.size)
        
        
        self.rect=self.image.get_rect(center=pos)
        # (self.unit_images

    def random_unit(self,row,col):
        if row==playerpos['1'][0]  and col==playerpos['1'][1] :
            self.unit='worker'
            
        elif row==playerpos['2'][0]  and col==playerpos['2'][1] :
            self.unit='worker'



        else:
            self.unit=units_types[randint(0,len(units_types)-1)]
        image=units_images[self.unit]
            
        return(image)
    def update(self):
    
        self.image=units_images[self.unit]
        self.image=pygame.transform.scale(self.image,self.size)







