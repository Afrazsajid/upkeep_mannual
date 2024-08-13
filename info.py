import pygame
from setting import *

def blittext(text,size,pos,):
    #this function will blit text
    pass

class Info:

    #this class wil show information like turn of player tiles requiremnets
    def __init__(self,player,screen):
        self.player=player
        self.screen=screen#getting screen to blit inforrmation

        #making a rectangle where it will draw info
        

        


    def blitinfo(self):
        pygame.draw.rect(self.screen,self.player.color,pygame.Rect(box_pos[0],box_pos[1],box_size[0],box_size[1]))
        self.blittext(f'player{self.player.player_name}',40,(20,500),font)
    
    
    
    def blittext(self,text,size,pos,font):
    #this function will blit text 
        font = pygame.font.SysFont(font,size)
        txtsurf = font.render(text, True, white)
        self.screen.blit(txtsurf,pos)
        


        
    
