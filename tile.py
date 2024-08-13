import pygame,random
from setting import *
import math
from unit import unit


def draw_polygon(pos):
    pass


def axialTonum(row,col):
     if row>0:
         tile_no=(col+1)+(tiles_row*row)
         return(tile_no)
    


class Tile(pygame.sprite.Sprite):
    def __init__(self,all_sprites,row,col,owner):
        super().__init__(all_sprites)
        self.owner=owner
        self.row=row
        self.col=col
    
    
    #this logic decide image of player 1 and 2 inital tile
    #  because when the game start the both player shpuld have a tile of forest
        if self.row==playerpos['1'][0]  and self.col==playerpos['1'][1] :
            self.settelment_index=0
            self.settelment_type=settelment_types[self.settelment_index]
            self.owner='1'
        elif row==playerpos['2'][0] and col==playerpos['2'][1]:
            self.settelment_index=0
            self.settelment_type=settelment_types[self.settelment_index]
            self.owner='2'
            
        else:
            self.settelment_index=random.randint(0,len(settelment_types)-1)
            self.settelment_type=settelment_types[self.settelment_index]

        self.image=tiles_images.get(self.settelment_type)

    

        #settelment image scale
        self.size=tile_size
        self.image=pygame.transform.scale(self.image,self.size)
 

        self.tile_size=tile_size

        self.pos=self.axial_pixel()
        self.rect=self.image.get_rect(center=self.pos)


 


    def axial_pixel(self):
        #set position of tile based on row and coloum

        #the formula and some numbers are set by run check basis 


        x = (tile_size[0]-24) * (3/2 * self.col)
        y = (tile_size[1]-20) * (math.sqrt(3)/2 * self.col  +  math.sqrt(3) * self.row)-500
        return x,y
    
    def update(self):
        self.settelment_type=settelment_types[self.settelment_index]
        self.image=tiles_images.get(self.settelment_type)
        self.image=pygame.transform.scale(self.image,self.size)

        
    

            
            
        


        
    