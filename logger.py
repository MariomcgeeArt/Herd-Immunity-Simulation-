class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        with open(self.file_name, 'w') as file:
             file.write(f'Population size : {pop_size}, vacc_per: {vacc_percentage}, virus_name: {virus_name}, mortality_rate: {mortality_rate}, repro_num: {basic_repro_num}\n')

          
    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
           with open(self.file_name, "a") as file:
            
            if random_person_sick :
                file.write(f"{person._id} infection failed {random_person._id} person is sick \n")

            elif random_person_vacc :
                file.write(f"{person._id} infection failed  {random_person._id} person is vacinated \n")

            elif did_infect:
                file.write(f"{person._id} infects {random_person._id} \n")


        
    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
            with open(self.file_name, "a") as file:
            if not did_die_from_infection:
                file.write(f"{person._id} died from infection \n")

            else:
                file.write(f"{person._id} survivied infection \n")
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        pass

    def log_time_step(self, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
          with open(self.file_name, "a") as file:
            file.write(f"Time step {time_step_number} ended, beginning {time_step_number + 1}\n")
            file.write(f"Total infected: {total_infected}\n")
            file.write(f"Total dead: {total_dead}\n")
            file.write(f"Total times vaccine saved person: {vaccine_saves}")
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass
