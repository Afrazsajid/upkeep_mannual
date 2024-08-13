import pygame,sys
from level import level #importing main module
from setting import * #importin some seeting varriables
from level import level


class game:
    def __init__(self,screen_size):
        pygame.init()
        self.screen=pygame.display.set_mode(screen_size)# setting our screen
        pygame.display.set_caption('Upkeep Mannual')# setting caption of screen
        self.clock=pygame.time.Clock()
        
        
        
        
        self.level=level()



    def run(self):
        while True:

            dt=self.clock.tick(16)/1000
            self.level.run()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()



if __name__=='__main__':
    game=game(s_size)
    game.run()

