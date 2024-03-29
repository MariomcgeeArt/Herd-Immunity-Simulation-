import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die as a result
        of the infection.

        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.
        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.logger = None
        self.population = [] # List of Person objects
        self.pop_size = pop_size # Int
        self.next_person_id = 0 # Int
        self.virus = virus # Virus object
        self.initial_infected = initial_infected # Int
        self.total_infected = 0 # Int
        self.current_infected = 0 # Int
        self.vacc_percentage = vacc_percentage # float between 0 and 1
        self.total_dead = 0 # Int
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
        virus_name, population_size, vacc_percentage, initial_infected)
        self.newly_infected = []

    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects.

        '''
        people = []

        for _id in range(self.pop_size):
            person = Person(_id, False)
            people.append(person)

        # percentage of the population left to vaccinate, rounded to the nearest number
        left_to_vaccinate = round((self.pop_size * self.vacc_percentage) + initial_infected)
        print(left_to_vaccinate)
        for person in people:
            if person._id < initial_infected:
                people[person._id].infection = self.virus.name
            elif person._id < left_to_vaccinate:
                people[person._id].is_vaccinated = True
            else:
                break

        return people

    def _simulation_should_continue(self):
        for person in self.population:
            if person.is_alive or person.is_vaccinated == False:
                return True

        return False











    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
     
        time_step_counter = 0
       
           # TODO: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper  # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.

        while self._simulation_should_continue():
            self.time_step()
            time_step_counter += 1


      
        print(f'The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def time_step(self):
    #Hllp from Ben Lafferty https://github.com/tempor1s/herd-immunity/blob/master/simulation.py
        
        interaction = 0

        
        interaction += 1

          living_people = [x for x in self.population if x.is_alive]

        for person in living_people:
            interaction = 0
            if person.infection:
                while interaction <= 100:
                    rand_person = random.choice(living_people)
                    self.interaction(person, rand_person)
                    interaction += 1

        ''' This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a randon person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''
        # TODO: Finish this method.
        pass

    def interaction(self, person, random_person):

        for person in self.population:

        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
      
        assert person.is_alive == True
        assert random_person.is_alive == True
            int1= random.uniform(0.0,1.0)
   
            if random_person.is_vaccinated:
                print("add logger")
          
            elif random_person.is_infected:
                print('add logger')
      
            elif random_person.is_alive and random_person.is_vaccinated == False and random_person.id is not person._id:
                if int1 > self.virus.repo_rate:
                    random_person.id.append(self.newly_infected)

        pass

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infect(self.virus)



        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        pass


if __name__ == "__main__":
    virus = Virus("HIV", 0.8, 0.3)
    initial_infected = 10
    sim = Simulation(100, .6, virus, initial_infected)
    sim._create_population(initial_infected)

    # ORIGINAL
    # params = sys.argv[1:]
    # virus_name = str(params[0])
    # repro_num = float(params[1])
    # mortality_rate = float(params[2])

    # pop_size = int(params[3])
    # vacc_percentage = float(params[4])

    # if len(params) == 6:
    #     initial_infected = int(params[5])
    # else:
    #     initial_infected = 1

    # virus = Virus(name, repro_rate, mortality_rate)
    # sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    # sim.run()
