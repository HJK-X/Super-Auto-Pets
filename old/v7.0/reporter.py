import time
import os

import neat

class TeamReplacer(neat.reporting.BaseReporter):
    """Replaces part of the past teams with every generation"""

    def __init__(self, show_species_detail):
        self.show_species_detail = show_species_detail
        self.generation = None
        self.generation_start_time = None
        self.generation_times = []
        self.num_extinctions = 0

    def start_generation(self, generation):
        self.generation = generation
        with open("terminal_output", 'a') as to:
            to.write(
                '\n ****** Running generation {0} ****** \n\n'.format(generation))
        self.generation_start_time = time.time()

        # data.past_teams = [data.past_teams[i][len(data.past_teams[i])//5:]
        #             for i in range(len(data.past_teams))]

        save_logs()
        data.logs = []
        data.preset_teams = []
        
        print("stats: {0} / {1} / {2}".format(data.total_wins,
              data.total_draws, data.total_losses))

        with open("terminal_output", 'a') as to:
            to.write("stats: {0} / {1} / {2}\n".format(data.total_wins,
                    data.total_draws, data.total_losses))


    def end_generation(self, config, population, species_set):
        ng = len(population)
        ns = len(species_set.species)
        with open("terminal_output", 'a') as to:
            if self.show_species_detail:  
                to.write('Population of {0:d} members in {1:d} species:\n'.format(ng, ns))
                to.write("   ID   age  size   fitness   adj fit  stag\n")
                to.write("  ====  ===  ====  =========  =======  ====\n")
                for sid in sorted(species_set.species):
                    s = species_set.species[sid]
                    a = self.generation - s.created
                    n = len(s.members)
                    f = "--" if s.fitness is None else f"{s.fitness:.3f}"
                    af = "--" if s.adjusted_fitness is None else f"{s.adjusted_fitness:.3f}"
                    st = self.generation - s.last_improved
                    to.write(f"  {sid:>4}  {a:>3}  {n:>4}  {f:>9}  {af:>7}  {st:>4}\n")
            else:
                to.write(
                    'Population of {0:d} members in {1:d} species\n'.format(ng, ns))

            elapsed = time.time() - self.generation_start_time
            self.generation_times.append(elapsed)
            self.generation_times = self.generation_times[-10:]
            average = sum(self.generation_times) / len(self.generation_times)
            to.write('Total extinctions: {0:d}\n'.format(self.num_extinctions))
            if len(self.generation_times) > 1:
                to.write("Generation time: {0:.3f} sec ({1:.3f} average)\n".format(
                    elapsed, average))
            else:
                to.write("Generation time: {0:.3f} sec\n".format(elapsed))

    def post_evaluate(self, config, population, species, best_genome):
        # pylint: disable=no-self-use
        fitnesses = [c.fitness for c in population.values()]
        fit_mean = mean(fitnesses)
        fit_std = stdev(fitnesses)
        best_species_id = species.get_species_id(best_genome.key)
        with open("terminal_output", 'a') as to:
            to.write('Population\'s average fitness: {0:3.5f} stdev: {1:3.5f}\n'.format(
                fit_mean, fit_std))
            to.write(
                'Best fitness: {0:3.5f} - size: {1!r} - species {2} - id {3}\n'.format(best_genome.fitness,
                                                                                    best_genome.size(),
                                                                                    best_species_id,
                                                                                    best_genome.key))

    def complete_extinction(self):
        self.num_extinctions += 1
        data.extinctions += 1
        with open("terminal_output", 'a') as to:
            to.write('All species extinct.\n')

    def found_solution(self, config, generation, best):
        with open("terminal_output", 'a') as to:
            to.write('\nBest individual in generation {0} meets fitness threshold - complexity: {1!r}\n'.format(
                self.generation, best.size()))

    def species_stagnant(self, sid, species):
        if self.show_species_detail:
            with open("terminal_output", 'a') as to:
                to.write("\nSpecies {0} with {1} members is stagnated: removing it\n".format(
                    sid, len(species.members)))

    def info(self, msg):
        with open("terminal_output", 'a') as to:
            to.write(msg + "\n")
