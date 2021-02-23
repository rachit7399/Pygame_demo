import pygame
import random
from blob_class import *
from logging import *

# old Version
# log_format = '%(asctime)s -- %(message)s -- %(lineno)d'
# basicConfig(filename='logging_file.log', level=DEBUG, format=log_format)

# New Version 
log_format = '{asctime} -- {message} -- {lineno}'
basicConfig(filename='logging_file.log', level=DEBUG, style = '{', format = log_format)

warning("This is demo Warning")

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BLOB")

clock = pygame.time.Clock()


def draw_environment(blob):
    game_display.fill(WHITE) 
    pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
    pygame.display.update()
    blob.move()

def main():
    red_blob = Blob(color = RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment(red_blob)
        clock.tick(60)        


if __name__ == '__main__':
    main()           
