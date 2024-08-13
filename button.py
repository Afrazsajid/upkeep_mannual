import pygame
from info import blittext
from setting import *
import sys
from unit import unit

class button:
    #this class handles all buttons logic
    #such as dissapera,appear logic
    #rember this class not represent single button this handle all buttons
    def __init__(self,player,screen):
        self.screen=screen
        self.player=player
        self.color=button_color.get(self.player.player_name)
        self.click=False

        self.train_button_lst=[]
        self.upgarde_button=None

    def blittext(self,text,size,pos,font):
    #this function will blit text 
        font = pygame.font.SysFont(font,size)
        txtsurf = font.render(text, True, white)
        self.screen.blit(txtsurf,pos)


    def drawbutton(self,pos,text,butto_size):
        rect=pygame.draw.rect(self.screen,self.color,pygame.Rect(pos[0],pos[1],butto_size[0],butto_size[1]))
        self.blittext(text,40,(pos[0]+8,pos[1]+7),'Roboto')
        return rect
    
    def turn(self):
    #this function handle turn button
        pos=(600,500)
        self.turn_buton=self.drawbutton(pos,'Turn',button_size)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_r:
                    self.click=True
            elif event.type==pygame.MOUSEBUTTONUP:
                M_pos=pygame.mouse.get_pos()
                if self.turn_buton.collidepoint(M_pos):
                    self.click=True


                
                if self.upgarde_button:
                    if self.upgarde_button.collidepoint(M_pos):
                        
                        
                        self.player.upgraded(self.player.selected_tile_hex)
                        
                
           

            
                point=len(self.player.train_option)-1
                        
                if self.player.train:
                    if point<2:
                        

                        if self.train_button_lst[0].collidepoint(M_pos):
            
                            change_unit=self.player.train_button_option[0]

                            self.player.train_unit(change_unit,self.player.selected_tile_hex)


                        elif self.train_button_lst[1].collidepoint(M_pos):
                            change_unit=self.player.train_button_option[1]

                            self.player.train_unit(change_unit,self.player.selected_tile_hex)
                    else:
                        if self.train_button_lst[0].collidepoint(M_pos):
            
                            change_unit=self.player.train_button_option[0]

                            self.player.train_unit(change_unit,self.player.selected_tile_hex)


                        elif self.train_button_lst[1].collidepoint(M_pos):
                            change_unit=self.player.train_button_option[1]

                            self.player.train_unit(change_unit,self.player.selected_tile_hex)
                            # ('yes')


                        elif self.train_button_lst[2].collidepoint(M_pos):
            
                            change_unit=self.player.train_button_option[2]
                               # (change_unit)

                            self.player.train_unit(change_unit,self.player.selected_tile_hex)
                            # ('yes')


                        elif self.train_button_lst[3].collidepoint(M_pos):
                            change_unit=self.player.train_button_option[3]
                            # (change_unit)

                            self.player.train_unit(change_unit,self.player.selected_tile_hex)
                            

                        

            
            
            
                
                

    def train(self):
    
        pos=(300,500)
        gap=25

        # if len(self.train_button_lst)>len(self.player.train_button_option):
        #     return 
    
        
        for i,button_text in enumerate(self.player.train_button_option):
            pos=pos[0],pos[1]+(gap*(i+1))
            buon=self.drawbutton(pos,f"train {button_text}",(220,40))
            self.train_button_lst.append(buon)
            # (self.train_button_lst)

    def upgarde(self):
        
        
        pos=(150,500)
        self.upgarde_button=self.drawbutton(pos,"upgrade",(button_size[0]+35,button_size[1]))
        



                
                        
                    
                    
        
            



           
            

    
        


        
