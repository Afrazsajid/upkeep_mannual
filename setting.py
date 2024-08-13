import pygame


settelment_types=['bushes','forest','village','village','forest','city','town',]

#tilesimages
tiles_images={name:pygame.image.load(f'assets/settelment/{name}/{name}.png') for name in settelment_types}

white=(255,255,255)
font='Roboto'

#screen setting
s_size=(700,700)
screen_color=(28,94,133,1)


#setting for tile
tile_size=(50,50)
tiles_col=22
tiles_row=20

# settelemtnt types


#unit types
units_types=['worker','knight','archer','sword man']
# unit no
unit_num=120
#unit images
units_images={
    unit:pygame.image.load(f'assets/unit/{unit}.png') for unit in units_types
}



#info seeting
box_size=(700,s_size[1]*0.30)
box_pos=(0,s_size[1]*0.70)


#player setting
colors={'1':(53, 162, 159),
        '2':(239, 98, 98)
       
       }
#button setting
button_size=(80,40)
button_color={
    '1':(0,0,255),
    '2':(255,0,0)
}

#fald size
flagsize=(10,10)

#player setting


#player inital pos
playerpos={'1':(13,7),
           '2':(13,6)
           }


#overlays image
overlay_images={
    '1':pygame.image.load('assets/overlay/blue flag.png'),
    '2':pygame.image.load('assets/overlay/Red Flag.png')

}