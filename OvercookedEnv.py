import gym
from gym import spaces
import numpy as np
from Map import Map
from ScoreBoard import ScoreBoard
from Player import Player
from HotStove import HotStove
from CuttingBoard import CuttingBoard
from FoodCrate import FoodCrate
from Player import Player
from Cookware import Cookware
from config import BLACK
from PlateCrate import PlateCrate
from ServiceStation import ServiceStation
import pygame
from config import REWARDS
from gym import spaces
from Actions import Actions
class OvercookedEnv(gym.Env):
    metadata = {'render.modes': ['human', 'rgb_array', 'none']}

    def __init__(self):
        super(OvercookedEnv, self).__init__()
        self.player = Player((50,50))
        self.map = Map(self.player, ScoreBoard())
        self.setup_map()
        self.game_start_time = pygame.time.get_ticks()
        self.game_duration = 150000
        self.screen = None
        self.action_space = spaces.Discrete(6)
        self.state_dim = 69
        results = ["", "take_item","take vege from crate","take plate from crate","move","toplate","cut","tocookware","serv","nonvaliditem"]
        self.actions_occ = {}
        self.results_occ = {result: 0 for result in results}
        self.n_actions = 0

    def setup_map(self):
        self.map.add_object(HotStove((0, 50)))
        self.map.add_object(CuttingBoard((450,450)))
        self.map.add_object(FoodCrate((0,450), "onion"))
        self.map.add_object(Cookware((0,50), "pot"))
        self.map.add_object(PlateCrate((100,200), "plate"))
        self.map.add_object(ServiceStation((450,50), "service"))
        self.add_obstacles()

    def add_obstacles(self):
        self.map.add_object(pygame.Rect(0, 50, 50, 50))
        self.map.add_object(pygame.Rect(0, 450, 50, 50))
        self.map.add_object(pygame.Rect(450, 450, 50, 50))
        self.map.add_object(pygame.Rect(100, 200, 50, 50))
        self.map.add_object(pygame.Rect(450, 50, 50, 50))


    def step(self, action):
        result = self.player.execute_actions(action, self.map)
        next_state = self._next_observation()
        reward = self.calculate_reward(result)
        done = self.is_done()
        self.n_actions+=1
        
        a = Actions().get_action_name(action)
        if a not in self.actions_occ:
            self.actions_occ[a]=1
        else:
            self.actions_occ[a]+=1

        return next_state, reward ,done

    def calculate_reward(self,result):
        # Implémentez votre logique de récompense ici
        reward = 0
        if result == 'cut':
            reward += REWARDS['cut']
        elif result == 'tocookware':
            reward += REWARDS['tocookware']
        elif result == 'toplate':
            reward += REWARDS['toplate']
        elif result == 'serv':
            reward += REWARDS['serv']
        elif result == 'nonvaliditem' or result =='move' or result == '':
            reward+= -1
        if result not in self.results_occ:
            self.results_occ[result]=1
        else:
            self.results_occ[result]+=1
   
        return reward

    def is_done(self):

        done = False
        if self.n_actions > 2000:
            done = True


        return done

    def reset(self):
        # Réinitialiser la map
        self.map.reset()
        # Réinitialiser le timer
        self.game_start_time = pygame.time.get_ticks()
        # Reconfigurer la map au besoin
        self.setup_map()
        # Retourner l'état initial de l'environnement
        self.n_actions=0
        self.actions_occ = {action: 0 for action in self.actions_occ}
        self.results_occ = {result: 0 for result in self.results_occ}
        return self._next_observation()

    

    def render(self, mode='human'):
        if mode == 'human':
            if self.screen is None:
                pygame.init()
                self.screen = pygame.display.set_mode((500, 500))
            self.map.draw(self.screen)
            pygame.display.flip()
        elif mode == 'rgb_array':
            # Return an image of the screen
            pass
        elif mode == 'none':
            # No rendering
            pass

    def _next_observation(self):
        # Return the current state of the game
        current_state = self.map.getState()
    
        # Si nécessaire, convertissez cette liste en un tableau numpy pour la compatibilité avec des bibliothèques comme NumPy ou PyTorch
        observation = np.array(current_state, dtype=np.float32)
    
        return observation

