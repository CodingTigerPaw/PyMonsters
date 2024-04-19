from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join

from sprites import Sprite
from entities import Player
from groups import AllSprites

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.all_sprites = AllSprites()

        self.clock =pygame.time.Clock()


        self.import_assets()
       # self.setup(self.tmx_maps['world'], 'house')
        self.setup(self.tmx_maps['hospital'], 'world')

        
                    
    def run(self):

         while(True):
            dt = self.clock.tick() / 1000
            #print(self.clock.tick())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.all_sprites.update(dt)
            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)        
            pygame.display.update()


    def import_assets(self):
        self.tmx_maps = {'world': load_pygame(join('..', 'data', 'maps', 'world.tmx')),
                         'hospital': load_pygame(join('..', 'data', 'maps', 'hospital.tmx')), }

    def setup(self, tmx_map, player_start_pos):

        for layer in ['Terrain', "Terrain Top"]:
            for x,y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE,y * TILE_SIZE), surf, self.all_sprites)



        for obj in tmx_map.get_layer_by_name('Objects'):
           Sprite((obj.x, obj.y), obj.image ,self.all_sprites)
           
 

        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player' and obj.properties['pos'] == player_start_pos:
               self.player = Player((obj.x, obj.y), self.all_sprites)
if __name__ == "__main__":
    game = Game()
    game.run()