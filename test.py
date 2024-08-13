# Hexagon Map Tutorial - Part One
import pygame ,sys
w, h = 500, 500
pygame.init()
scrn=pygame.display.set_mode((w,h))

hex_size = 20


img=pygame.image.load('D:/Afraz/assets/Bushes001.png')
img=pygame.transform.scale(img,(50,50))

grid_x_pixels = .9 * w
grid_y_pixels = .9 * h

sep_x = 3* hex_size
sep_y = .86 * hex_size

grid_x = int(grid_x_pixels / sep_x) + 1
grid_y = int(grid_y_pixels / sep_y) + 1

def draw_hexagons():


    
    
    # Draw the Grid
    current_x = 1
    current_y = 1
    for i in range(100):
        if (i % 2 == 0):
            current_x += 1.5 * hex_size
        for j in range(100):

            scrn.blit(img,(current_x-30, current_y-30))
            
            current_x += sep_x
        current_x = w/2.0 - grid_x_pixels/2.0
        current_y += sep_y
while True:
    pygame.display.update()
    draw_hexagons()
    # self.screen.fill(screen_color)
    # pygame.display.update()
    # dt=self.clock.tick(16)/1000
    # self.level.run()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()