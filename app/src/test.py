import multiprocessing as mp
import os
import pickle
import csv
import sys
import time

import neat
from neat.math_util import mean, stdev
import sapai

import sap
import visualize
import reporter

local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config-feedforward')
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                        neat.DefaultSpeciesSet, neat.DefaultStagnation,
                        config_path)

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 1


class TeamReplacer(neat.reporting.BaseReporter):
    """Replaces part of the past teams with every generation"""

    def __init__(self, show_species_detail):
        self.show_species_detail = show_species_detail
        self.generation = None
        self.generation_start_time = None
        self.generation_times = []
        self.num_extinctions = 0

p = neat.Checkpointer.restore_checkpoint('ckpt-19979')
winner = p.run(eval_genomes, 1)
# Display the winning genome.
print('\nBest genome:\n{!s}'.format(winner))

node_names = {-1: 'Pet 1, ID', -2: 'Pet 1, exp', -3: 'Pet 1, atk', -4: 'Pet 1, def', -5: 'Pet 1, perk',
              -6: 'Pet 2, ID', -7: 'Pet 2, exp', -8: 'Pet 2, atk', -9: 'Pet 2, def', -10: 'Pet 2, perk',
              -11: 'Pet 3, ID', -12: 'Pet 3, exp', -13: 'Pet 3, atk', -14: 'Pet 3, def', -15: 'Pet 3, perk',
              -16: 'Pet 4, ID', -17: 'Pet 4, exp', -18: 'Pet 4, atk', -19: 'Pet 4, def', -20: 'Pet 4, perk',
              -21: 'Pet 5, ID', -22: 'Pet 5, exp', -23: 'Pet 5, atk', -24: 'Pet 5, def', -25: 'Pet 5, perk', 
              -26: 'Shop 1, ID', -27: 'Shop 1, atk', -28: 'Shop 1, def', -29: 'Shop 1, frozen', 
              -30: 'Shop 2, ID', -31: 'Shop 2, atk', -32: 'Shop 2, def', -33: 'Shop 2, frozen', 
              -34: 'Shop 3, ID', -35: 'Shop 3, atk', -36: 'Shop 3, def', -37: 'Shop 3, frozen', 
              -38: 'Shop 4, ID', -39: 'Shop 4, atk', -40: 'Shop 4, def', -41: 'Shop 4, frozen', 
              -42: 'Shop 5, ID', -43: 'Shop 5, atk', -44: 'Shop 5, def', -45: 'Shop 5, frozen', 
              -46: 'Shop 6, ID', -47: 'Shop 6, atk', -48: 'Shop 6, def', -49: 'Shop 6, frozen', 
              -50: 'Shop 7, ID', -51: 'Shop 7, atk', -52: 'Shop 7, def', -53: 'Shop 7, frozen', 
              -54: 'Money', -55: 'Turn', -56: "Lives", -57: "Wins",
              0: 'Buy 1 to 1', 1: 'Buy 1 to 2', 2: 'Buy 1 to 3', 3: 'Buy 1 to 4', 4: 'Buy 1 to 5',
              5: 'Buy 2 to 1', 6: 'Buy 2 to 2', 7: 'Buy 2 to 3', 8: 'Buy 2 to 4', 9: 'Buy 2 to 5',
              10: 'Buy 3 to 1', 11: 'Buy 3 to 2', 12: 'Buy 3 to 3', 13: 'Buy 3 to 4', 14: 'Buy 3 to 5',
              15: 'Buy 4 to 1', 16: 'Buy 4 to 2', 17: 'Buy 4 to 3', 18: 'Buy 4 to 4', 19: 'Buy 4 to 5',
              20: 'Buy 5 to 1', 21: 'Buy 5 to 2', 22: 'Buy 5 to 3', 23: 'Buy 5 to 4', 24: 'Buy 5 to 5',
              25: 'Buy 6 to 1', 26: 'Buy 6 to 2', 27: 'Buy 6 to 3', 28: 'Buy 6 to 4', 29: 'Buy 6 to 5',
              30: 'Buy 7 to 1', 31: 'Buy 7 to 2', 32: 'Buy 7 to 3', 33: 'Buy 7 to 4', 34: 'Buy 7 to 5',
              35: 'Move 1 to 2', 36: 'Move 1 to 3', 37: 'Move 1 to 4', 38: 'Move 1 to 5',
              39: 'Move 2 to 1', 40: 'Move 2 to 3', 41: 'Move 2 to 4', 42: 'Move 2 to 5',
              43: 'Move 3 to 1', 44: 'Move 3 to 2', 45: 'Move 3 to 4', 46: 'Move 3 to 5',
              47: 'Move 4 to 1', 48: 'Move 4 to 2', 49: 'Move 4 to 3', 50: 'Move 4 to 5',
              51: 'Move 5 to 1', 52: 'Move 5 to 2', 53: 'Move 5 to 3', 54: 'Move 5 to 4',
              55: 'Sell 1', 56: 'Sell 2', 57: 'Sell 3', 58: 'Sell 4', 59: 'Sell 5',
              60: 'Freeze 1', 61: 'Freeze 2', 62: 'Freeze 3', 63: 'Freeze 4', 64: 'Freeze 5', 65: 'Freeze 6', 66: 'Freeze 7',
              67: "Roll", 68: "End Turn"}

visualize.draw_net(config, winner, True, node_names=node_names)
visualize.draw_net(config, winner, True, node_names=node_names, prune_unused=True)

