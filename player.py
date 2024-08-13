import pygame
from setting import *
import sys
from math import sqrt
import math
from unit import unit


def draw_polygon(pos,screen,color):
    points=[]
    for i in range(6):
        angle = math.pi / 3.0 * i
        x = pos[0] + round(tile_size[0]*0.64) * math.cos(angle)
        y = pos[1] + round(tile_size[1]*0.64) * math.sin(angle)
        points.append((x, y))
    pygame.draw.polygon(screen, color, points, 2)
    


 

def pixel_to_hex(pos):
    #this fucntion takes mouse pos and tell row and col number of tile in eich that pos is


    #this is help ful for click functionality to tile as it will not iterrate to every til to chech which is clicked simply take pos and giv row and col

    mouse_x,mouse_y=pos
    col = round((mouse_x / (tile_size[0] - 24)) * (2/3))
    row = round(((mouse_y + 500) / (tile_size[1] - 20) - (math.sqrt(3)/2 * col)) / math.sqrt(3))    
    return row, col



def get_tile_num(row,col):
     #this funvtion takes row and col and give a tile no in our list based on row and col of tile
     if row>0:
         tile_no=(col)+(tiles_col*row)
         return(tile_no)
     else:
         return(col)


def axial_pixel(row,col):
    #set position of tile based on row and coloum
    #the formula and some numbers are set by run check basis 
    x = (tile_size[0]-24) * (3/2 * col)
    y = (tile_size[1]-20) * (math.sqrt(3)/2 * col  +  math.sqrt(3) * row)-500
    return x,y
    



class Player:
    #this class wil handle player it have function like occupy atile etc
    def __init__(self,tiles_lst,player_name,all_sprites):
        self.all_sprites=all_sprites
        self.player_name=player_name
        self.color=colors.get(self.player_name)#setting color of player based on player name
        self.tiles_lst=tiles_lst
        self.owner_lst=[playerpos[player_name]]
        self.screen=pygame.display.get_surface()


        self.selection=False
        self.selected_tile=None
        self.selected_tile_hex=None


        self.occupying=False
        self.occuping_tiles=[]

        self.settlements_requirement={
            'village':['bushes'],
            'town':['bushes','village'],
            'city':['bushes','village','town']


        }
        self.units_requirement={
            'worker':['bushes'],
            'sword man':['bushes'],
            'archer':['bushes','forest'],
            'knight':['bushes','bushes']




        }


        self.unsatisfied_tiles=[]
        self.satisfying_tile=[]#list of those tiles that satisfy some other tiles

        self.train=False

        self.train_button_option=[]
        self.train_option={
            'village':['worker','sword man'],
            'town':['archer','workers','sword man'],
            'city':['worker','sword man','archer','knight']

        }

        self.units_unsatisfied=[]

        self.upgrade=False
    
    
    def upgraded(self,selected_tile_hex):
        tile_no=get_tile_num(selected_tile_hex[0],selected_tile_hex[1])
        self.tiles_lst[tile_no].settelment_index+=1
    





        
       
        self.occuping_tiles=[]
        
    def can_be_upgrade(self):
        if not(self.selection):
            self.upgrade=False
            return 
        tile_no=get_tile_num(self.selected_tile_hex[0],self.selected_tile_hex[1])
        tile=self.tiles_lst[tile_no]
        try:
            unit_no=self.Tile_num_To_unit[tile_no]
            unit=self.unit_lst[unit_no]
        except:
            self.upgrade=False
        try:

            if unit.unit=='worker':
                self.upgrade=True
            else:
                self.upgrade=False
        except:
            self.upgrade=False
            

    def can_be_train(self):
        tile_no=get_tile_num(self.selected_tile_hex[0],self.selected_tile_hex[1])

        try:
    
            unit_no=self.Tile_num_To_unit[tile_no]
            unit=self.unit_lst[unit_no]
        except:
            unit=None


        tile=self.tiles_lst[tile_no]
        
        if tile.settelment_type in self.settlements_requirement.keys():
            self.train_button_option=self.train_option.get(tile.settelment_type)
            self.train=True
            
    def train_unit(self,change_unit,change_tile_hex):
        tile_no=get_tile_num(change_tile_hex[0],change_tile_hex[1])
        tile=self.tiles_lst[tile_no]

        unit_no=self.Tile_num_To_unit.get(tile_no)
        

        


    


        Unit=unit(self.all_sprites,tile.pos,tile.row,tile.col,len(self.unit_lst),self.unit_lst)
        self.unit_lst[unit_no]=Unit

        self.unit_lst[unit_no].unit=change_unit
        



        
        
             
    def is_unit_satisfied(self):

        for check_tile_hex in self.owner_lst:#checking each tile own by player is the satisfied


            check_tile_no=get_tile_num(check_tile_hex[0],check_tile_hex[1])
            check_tile_unit=self.Tile_num_To_unit[check_tile_no]
            if check_tile_unit.unit in self.settlements_requirement.keys():

                require_index=len(self.settlements_requirement.get(check_tile_unit.settelment_type))


                for checking_tile_hex in self.owner_lst:
                    if not(checking_tile_hex==check_tile_hex) :
                        
                        checking_tile_no=get_tile_num(checking_tile_hex[0],checking_tile_hex[1])
                        checking_tile_unit_no=self.Tile_num_To_unit[checking_tile_no]
                        checking_tile_unit=self.unit_lst[checking_tile_unit_no]
                        if checking_tile_unit.unit in self.units_requirement.get(check_tile_unit.unit):
                            require_index-=1
                    if require_index<0:
                        self.units_unsatisfied.append(checking_tile_unit_no)

        
    def delete_unit(self):
        for unit_no in self.units_unsatisfied:
            unit=self.unit_lst[unit_no]
            unit.kill()
            self.unit_lst.remove(unit)
        self.units_unsatisfied=[]
            

    def is_settelment_satisfied(self):
        
        for check_tile_hex in self.owner_lst:#checking each tile own by player is the satisfied


            check_tile_no=get_tile_num(check_tile_hex[0],check_tile_hex[1])
            check_tile=self.tiles_lst[check_tile_no]


            if check_tile.settelment_type in self.settlements_requirement.keys():

                require_index=len(self.settlements_requirement.get(check_tile.settelment_type))


                for checking_tile_hex in self.owner_lst:
                    if not(checking_tile_hex==check_tile_hex):
                        
                        checking_tile_no=get_tile_num(checking_tile_hex[0],checking_tile_hex[1])
                        checking_tile=self.tiles_lst[checking_tile_no]
                        if (checking_tile.settelment_type in self.settlements_requirement.get(check_tile.settelment_type)): #and (not(checking_tile_hex in self.satisfying_tile))
                            self.satisfying_tile.append(checking_tile_hex)
                            require_index-=1

                if require_index>0:
                    self.unsatisfied_tiles.append(check_tile_hex)

                             

    def delete_unsatisfied_tiles(self):
        for unsatisfied in self.unsatisfied_tiles:
            tile_no=get_tile_num(unsatisfied[0],unsatisfied[1])
            tile=self.tiles_lst[tile_no]
            tile.owner='no'
            
            unit_no=self.Tile_num_To_unit.get(tile_no)
            unit=self.unit_lst[unit_no]
            unit.kill()
            self.unit_lst.remove(unit)

            
                

            self.unsatisfied_tiles.remove(unsatisfied)
            self.owner_lst.remove(unsatisfied)
        self.unsatisfied_tiles=[]

                        

    def updated(self,unit_lst,Tile_num_To_unit):
        self.unit_lst=unit_lst
        self.Tile_num_To_unit= Tile_num_To_unit
        self.is_settelment_satisfied()
        return self.tiles_lst,unit_lst,self.Tile_num_To_unit
        

    def can_be_occupy(self,check_row,check_col):


        selected_tile_no=get_tile_num(self.selected_tile_hex[0],self.selected_tile_hex[1])
        
    
        check_tileNo=get_tile_num(check_row,check_col)
        check_tile=self.tiles_lst[check_tileNo]

        if (check_row,check_col) in self.occuping_tiles:
            return False

        if check_tile.owner=='no' :
            try:

                check_tile_unit=self.unit_lst[self.Tile_num_To_unit.get(check_tileNo)]
                selected_unit=self.unit_lst[self.Tile_num_To_unit.get(selected_tile_no)]
                
            except:
                check_tile_unit=None
                selected_unit=None


            if check_tile_unit==None:#condition where the tile has no unit
                return True
            

    
            
            else:
                if selected_unit==None or selected_unit.unit=='worker':
                    return False
                else:
                    return True

                
            


    def occupy(self):
        click=False

        mouseP=pygame.mouse.get_pressed()
        if mouseP[0]:
            M_pos=pygame.mouse.get_pos()
            click=True
        for row,col in self.occuping_tiles:
            pos=axial_pixel(row,col)
            draw_polygon(pos,self.screen,(0,255,0))

        if click:
            click_tile_hex=pixel_to_hex(M_pos)
            if click_tile_hex in self.occuping_tiles:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==pygame.MOUSEBUTTONUP:

                        occupied_tile_no=get_tile_num(click_tile_hex[0],click_tile_hex[1])
            
                        self.tiles_lst[occupied_tile_no].owner=self.player_name
                        self.owner_lst.append(click_tile_hex)


                        del_unit_no=self.Tile_num_To_unit.get(get_tile_num(self.selected_tile_hex[0],self.selected_tile_hex[1]))
                        try:
                            del_unit=self.unit_lst[del_unit_no]
                        except:
                            pass


                        occuping_unit=unit(self.all_sprites,self.tiles_lst[occupied_tile_no].pos,click_tile_hex[0],click_tile_hex[1],len(self.unit_lst),self.unit_lst)
                        occuping_unit.unit=del_unit.unit
                        del_unit.kill()
                        self.unit_lst.remove(del_unit)
                        self.unit_lst.append(occuping_unit)

                        
                        

                        
                        


                        self.occupying=False
                        self.selection=False
                        self.occuping_tiles=[]
                        self.Tile_num_To_unit[occupied_tile_no]=len(self.unit_lst)-1


                        
    def select(self):
        selected_tile_pos=axial_pixel(self.selected_tile_hex[0],self.selected_tile_hex[1])

        draw_polygon(selected_tile_pos,self.screen,self.color)
        self.check_occuping_tile()
    
    
    
    def check_occuping_tile(self):
        select_row,select_col=self.selected_tile_hex[0],self.selected_tile_hex[1]
        

        
        #list of those tile that can be occupied
        check_tile_lst=[
            (select_row,select_col-1),
            (select_row-1,select_col),
            (select_row-1,select_col+1),
            (select_row,select_col+1),
            (select_row+1,select_col),
            (select_row+1,select_col-1)
]
        check_tile_no=None#this varrible will have a value of tile that need be to check whethe it can be occupied or not
        for check_row,check_col in check_tile_lst:
            if self.can_be_occupy(check_row,check_col):
                self.occuping_tiles.append((check_row,check_col))
                self.occupying=True     



    def run(self):
        
        #this function all event of player

        
            


        if self.occupying==True:
            self.occupy()

        self.is_settelment_satisfied()
        if len(self.unsatisfied_tiles)>0:
            self.delete_unsatisfied_tiles()
       

        
        if self.selected_tile_hex!=None:
            self.can_be_upgrade()  
    

        if self.selection==True:
            # (self.owner_lst)
            self.select()
            self.can_be_train()
            # (self.tiles_lst[get_tile_num(self.selected_tile_hex[0],self.selected_tile_hex[1])].settelment_type)
            # ('down',get_tile_num(self.selected_tile_hex[0],self.selected_tile_hex[1]))
        
            
            # .selected_tile_hex)


        
       
    
       
        mouse_b=pygame.mouse.get_pressed()
        if mouse_b[0]:
            M_pos=pygame.mouse.get_pos()
            
            
            if (M_pos[1]<box_pos[1]):
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==pygame.MOUSEBUTTONUP:
                        
                        selected_tile_hex=pixel_to_hex(M_pos)
                        if selected_tile_hex in self.owner_lst:
                            self.selection=True

                            
                            self.selected_tile_hex=selected_tile_hex
                        else:
                            self.selection=False
                    
                        

            else:
                self.selection=False
                self.occupying=False


    