import pygame
from setting import *
from tile import Tile
from player import *
from info import Info
from button import button
from unit import unit
from random import randint
from overlyofplayer import overlay

def get_tile_num(row,col):
     #this funvtion takes row and col and give a tile no in our list based on row and col of tile
     
    tile_no=(col)+(tiles_col*row)
    return(tile_no)
     

# from tile import Tile

class level:
    def __init__(self):
        self.screen=pygame.display.get_surface()
        self.all_sprites=pygame.sprite.Group()
        
        self.tiles_lst=[]
        self.units_lst=[]
        self.Tile_num_To_unit={}

        
        self.player1=Player(self.tiles_lst,'1',self.all_sprites)
        self.player2=Player(self.tiles_lst,'2',self.all_sprites)

        

        



        self.players_lst=[self.player1,self.player2]
        

        self.player_index=0


        self.Runingplayer=self.player1#first turn
        self.button=button(self.Runingplayer,self.screen)

        
        self.setup()
        overlay1=overlay(self.player1.owner_lst[0],self.all_sprites,self.player1.player_name)
        overlay2=overlay(self.player2.owner_lst[0],self.all_sprites,self.player2.player_name)
        self.overlay_lst=[overlay1,overlay2]


        self.info=Info(self.Runingplayer,self.screen)       
        self.button=button(self.Runingplayer,self.screen)
        


    def setup(self):
    
        for i in range(tiles_row):
            
            for j in range(tiles_col):
                tile=Tile(self.all_sprites,i,j,'no')
                self.tiles_lst.append(tile)

        num=playerpos['1']
        tileNO=get_tile_num(num[0],num[1])
        tile=self.tiles_lst[tileNO]
        self.units_lst.append(unit(self.all_sprites,tile.pos,tile.row,tile.col,len(self.units_lst),self.units_lst))       
        self.Tile_num_To_unit[tileNO]=0#this dict will help us to acces specific unit by specifi tile


        num=playerpos['2']
        tileNO=get_tile_num(num[0],num[1])      
        tile=self.tiles_lst[tileNO]
        self.units_lst.append(unit(self.all_sprites,tile.pos,tile.row,tile.col,len(self.units_lst),self.units_lst))
        self.Tile_num_To_unit[tileNO]=1#this dict will help us to acces specific unit by specifi tile
        
        for i in range(unit_num):
            
            num=randint(0,tiles_row-2),randint(0,tiles_col-2)
            tileNO=get_tile_num(num[0],num[1])      
            tile=self.tiles_lst[tileNO]
            self.units_lst.append(unit(self.all_sprites,tile.pos,tile.row,tile.col,len(self.units_lst),self.units_lst))
            self.Tile_num_To_unit[tileNO]=i+2#this dict will help us to acces specific unit by specifi tile
        # (self.Tile_num_To_unit)
        # (self.Tile_num_To_unit[295])

     
    
    def run(self):
        self.screen.fill(screen_color)





        

        self.all_sprites.draw(self.screen)
        self.all_sprites.update()



        

        




        self.Runingplayer.run()

        

        

        
        

        
        
        
      
            
        
        
        
        
        self.info.blitinfo()

            #chnageturnlogic
        keys=pygame.key.get_pressed()


        self.button.turn()


        if self.Runingplayer.train and self.Runingplayer.selection:
            # ('yes')
            self.button.train()
        if self.Runingplayer.upgrade:
            self.button.upgarde()
    
        if self.button.click :
            
            if self.player_index>0:
                self.player_index=0
                # ('yes')

            else:
                self.player_index=1
                # ('no')
            self.Runingplayer=self.players_lst[self.player_index]
            self.info=Info(self.Runingplayer,self.screen)       
            self.button=button(self.Runingplayer,self.screen)
            self.button.click=False
            # not_clicked=False

            



        else:

            clicked=False
        try:
            self.overlay_lst.append(overlay(self.Runingplayer.owner_lst[len(self.Runingplayer.owner_lst)-1],self.all_sprites,self.Runingplayer.player_name))
        except:
            pass
        self.tiles_lst,self.units_lst,self.Tile_num_To_unit=self.Runingplayer.updated(self.units_lst,self.Tile_num_To_unit)
        pygame.display.update()
