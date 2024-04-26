import pygame # type: ignore
import sys
from CookingStation import CookingStation
from HotStove import HotStove
from CuttingBoard import CuttingBoard
from FoodCrate import FoodCrate
from Player import Player
from Item import Item
from Vegetable import Vegetable
from Container import Container
from Cookware import Cookware
from InteractionManager import InteractionManager
from config import BLACK,WHITE,ONION,GRAY
from PlateCrate import PlateCrate
from ServiceStation import ServiceStation
from Map import Map


pygame.init()

# Taille de la fenêtre
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Overcooked')

clock = pygame.time.Clock()

# Positions initiales 
player = Player((50,50))

game_map = Map(player)

# Ajout des objets à la carte
game_map.add_object(HotStove((0, 0)))
game_map.add_object(CuttingBoard((450,450)))
game_map.add_object(FoodCrate((0,450), "onion"))
game_map.add_object(Cookware((0,0), "pot"))
game_map.add_object(PlateCrate((100,200), "plate"))
game_map.add_object(ServiceStation((450,0), "service"))

# Ajouter des obstacles
game_map.add_object(pygame.Rect(0, 0, 50, 50))
game_map.add_object(pygame.Rect(0, 450, 50, 50))
game_map.add_object(pygame.Rect(450, 450, 50, 50))
game_map.add_object(pygame.Rect(100, 200, 50, 50))
game_map.add_object(pygame.Rect(450, 0, 50, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Gestion des touches
    keys = pygame.key.get_pressed()
    player.update_position(keys, game_map.obstacles)

    if keys[pygame.K_SPACE]:
        player.update_item_position()
        if player.held_item:
                # Si le joueur tient un objet et appuie sur espace, relâcher cet objet
                player.drop_item(game_map)
        else:
            # Sinon, interagir avec les objets environnants pour en prendre un
            player.interact(game_map)

    if keys[pygame.K_c]:
        player.cut(game_map)

    # Interface graphique
    screen.fill(BLACK)
    game_map.draw(screen)

    # MàJ
    pygame.display.flip()

    clock.tick(10)

pygame.quit()
sys.exit()