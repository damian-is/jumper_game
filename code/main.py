import pygame, sys
from settings import *
from tiles import *

class Game:
    def __init__(self):

        # General Setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('jumper')
        self.clock = pygame.time.Clock()
        self.test_tile = pygame.sprite.Group(Tile((100, 100), 200))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.test_tile.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
