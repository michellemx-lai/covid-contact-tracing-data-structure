########################################################
# Part 1 - Infected_person Class
########################################################
class Infected_person:
    """
    A class used to represent the id of an infected person, the date on which they were infected,
    and a list of ids of the people they infected.

    Attributes:
    ----------
    id (str): A unique identifier of an infected person
    infected (list): Contains people infected by an infected person
    infected_on (str): Date an infected person was infected

    Methods:
    -------
    infects(person)
        Adds the id of a person to the infected list of
        by whomever infected this person.
    """
    
    def __init__(self, pid, date = "unknown"):
        """
        Constructor, initializes Infected_person class variables. 

        Inputs:
        ------
        - self (Infected_person): an object representing a person's id,
          who they infected, and the date on which they were infected.
        - pid (str): a string representing a person's id
        - date (str): date of infection of the person, has a default value of the string "unknown"
        
        Initializes id to pid, infected to an empty list, and infected_on to date
        """
        self.id = pid
        self.infected = []
        self.infected_on = date
    
    def __str__(self):
        """
        Returns a string representation of the object Infected_person
        in the form "(A,B,C)" where:
        - A is the object’s id
        - B is the infected_on date
        - C is the size of the infected list
        """
        return "(" + str(self.id) + "," + str(self.infected_on) + "," + str(len(self.infected)) + ")"

    def infects(self, person):
        """
        (self, str) -> none
        Given an Infected_person object and a string representing a person's id, adds id to the infected list 
        if id is not already in the list. Returns none.
        """
        if person not in self.infected:
            self.infected.append(person)