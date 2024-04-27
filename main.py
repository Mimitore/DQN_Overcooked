import pygame
import sys
from HotStove import HotStove
from CuttingBoard import CuttingBoard
from FoodCrate import FoodCrate
from Player import Player
from Cookware import Cookware
from config import BLACK
from PlateCrate import PlateCrate
from ServiceStation import ServiceStation
from Map import Map
from ScoreBoard import ScoreBoard

pygame.init()

# Taille de la fenêtre
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Overcooked')

clock = pygame.time.Clock()

# Positions initiales 
player = Player((50,50))
score = ScoreBoard()
game_map = Map(player,score)

# Ajout des objets à la carte
game_map.add_object(HotStove((0, 50)))
game_map.add_object(CuttingBoard((450,450)))
game_map.add_object(FoodCrate((0,450), "onion"))
game_map.add_object(Cookware((0,50), "pot"))
game_map.add_object(PlateCrate((100,200), "plate"))
game_map.add_object(ServiceStation((450,50), "service"))

# Ajouter des obstacles
game_map.add_object(pygame.Rect(0, 50, 50, 50))
game_map.add_object(pygame.Rect(0, 450, 50, 50))
game_map.add_object(pygame.Rect(450, 450, 50, 50))
game_map.add_object(pygame.Rect(100, 200, 50, 50))
game_map.add_object(pygame.Rect(450, 50, 50, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Gestion des touches
    keys = pygame.key.get_pressed()
    player.execute_actions(keys, game_map)


    # Interface graphique
    screen.fill(BLACK)
    game_map.draw(screen)

    # MàJ
    pygame.display.flip()

    clock.tick(10)

pygame.quit()
sys.exit()