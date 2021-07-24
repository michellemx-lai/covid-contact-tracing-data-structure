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

########################################################
# Part 2 - Parse Contact Tracing Data
########################################################
import csv 

def parse_contacts(filename):
    """ (str) -> dict
    
    Reads the contents of the given CSV file. Each row in the data file lists an infected person,
    who they were infected by, and the date on which they were infected. 

    Returns a dictionary of the following format {id : Infected_person-object, ...}, where:
    - each key, id, is a string representing a person’s id
    - each value is an object of type Infected_person

    If the data file is empty (i.e., has no rows), returns an empty dictionary.
    """

    parsed_data = {}

    #open the file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        #skip headers
        header = next(reader) 

        #create a key for each person in the first (id) column by looping through each row
        for row in reader: 
            
            infected_id = row[0]
            date = row[2]

            infected_person_object = Infected_person(infected_id, date)
            
            parsed_data.update({infected_person_object.id: infected_person_object})
        
    #open the file again\
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        #skip headers
        header = next(reader) 

        #create a key for each person in the second (infected_by) column if they are not already in parsed_data 
        for row in reader:

            spreader_id = row[1]

            if spreader_id not in parsed_data:
                infected_person_object = Infected_person(spreader_id)
            
                parsed_data.update({infected_person_object.id: infected_person_object})
                
    #open the file again
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        #skip headers
        header = next(reader) 
    
        for row in reader:
            infected_id = row[0]
            spreader_id = row[1]
            date = row[2]
            
            #loop through all the keys in parsed_data, call infects() method 
            for id in parsed_data:
                if id == spreader_id:
                    parsed_data[id].infects(infected_id)
    
    #delete keys-value pairs that have any empty keys or values from parsed_data
    parsed_data_copy = dict(parsed_data) 
    for id in parsed_data_copy:
        if id == None or id == '' or parsed_data[id] == None or parsed_data[id] == '':
            del parsed_data[id]

    return parsed_data

########################################################
# Part 3 - Identify Top Direct Superspreaders
########################################################

def find_top_direct_superspreader(parsed_data):
    """ (dict) -> list

    Takes in a dictionary with format {id : Infected_person-object, ...}, identifies the id corresponding
    to the person who has infected the most people in the dictionary.
    Returns a list of ids corresponding to the top direct superspreader(s), in the format [id1, id2, ...]

    If the input is an empty dictionary, returns an empty list.
    """
    #initialize variables
    highest_num = 0
    top_direct_superspreader = []
    
    #loop over keys in parsed_data dictionary
    for id in parsed_data:

        #access the corresponding value of id, and call infected() to find length of infected list 
        num_infected = len(parsed_data[id].infected)
        
        #check if num_infected is greater than highest_num. If so, they are a superspreader
        if num_infected > highest_num:
            top_direct_superspreader.clear()
            top_direct_superspreader.append(id) 
            highest_num = num_infected
        
        #check if num_infected is equal to highest_num. If so, they are a tied superspreader 
        elif num_infected == highest_num:
            top_direct_superspreader.append(id)

    return top_direct_superspreader

########################################################
# Part 4 - Find Superspreading Dates
########################################################
def find_superspreading_date(parsed_data):
    """ (dict) -> (list, int) 

    Takes in a dictionary and identifies the superspreading date(s) for direct infections, 
    and how many infections occured on the superspreading date(s).
    
    Returns a tuple of the form ([date1,...], max-infected) where:

    - [date1,...] is a list of strings representing all superspreading dates, with no duplicates.

    - max_infected is the number of direct infections on any of the superspreading dates

    If the input dictionary is empty, returns the tuple ([], 0)
    """
    #initialize variables
    superspreading_date = []
    all_infection_dates = []
    max_infected = 0
    
    #loop over the keys in parsed_data 
    for id in parsed_data:
        
        #access the corresponding value and call infected_on method to find the date
        infection_date = parsed_data[id].infected_on
        
        #append all infection dates to our list except the unknowns
        if infection_date != "unknown":
            all_infection_dates.append(infection_date)
        
    for date in all_infection_dates:
        if date not in superspreading_date: 

            #the number of times the date appears in an Infected_person object is the number of people infected on that date
            num_infected = all_infection_dates.count(date)
            
            #check if the number of infections is higher or equal to the current highest 
            if num_infected > max_infected: 
                superspreading_date.clear()
                superspreading_date.append(date)
                max_infected = num_infected
            
            elif num_infected == max_infected:
                superspreading_date.append(date)
        
    return (superspreading_date, max_infected)

########################################################
# Part 5 - Identify Top Direct + Indirect Superspreaders
########################################################

####
# 5a
####
def get_all_infected(parsed_data, person_id):
    """ (dict, str) -> list
    
    Takes in a dictionary with format {id : Infected_person-object, ...} and a string that represents a person's id, 
    finds all persons within the dictionary who was directly or indirectly infected by the person of interest.

    Returns a list of the ids of all persons (directly + indirectly) infected by the person of interest. 

    If dictionary is empty or person_id is not in dictionary, returns none.
    """
    #check if person_id is in parsed_data dictionary. If so, access its corresponding value
    #in the dictionary, call the infected method, and copy the infected list
    if person_id in parsed_data:
        all_infected = list(parsed_data[person_id].infected) #all_infected now contains all directly infected people

        for id in all_infected:
            all_infected.extend(parsed_data[id].infected) #extend all_infected list to include all indirectly infected people

        return all_infected

    #only return an empty list if person_id is not in parsed_data
    else:
        return []
    
####
# 5b
####
def find_top_direct_plus_indirect_superspreader(parsed_data):
    """
    (dict) --> (list, int)

    Takes in a dictionary with format {id : Infected_person-object, ...}
    Returns a tuple of the form ([id1, id2, ...], max_infection_count) where:
    - ([id1, id2, ...] is a list of person id’s corresponding to the top (direct + indirect) superspreader(s), with no duplicates.
    
    If called with an empty dictionary as argument, returns the tuple ([], 0).

    """

    #initialize variables
    max_infection_count = 0
    top_overall_superspreader = []
    
    #loop over keys in parsed_data dictionary
    for id in parsed_data:
        #call get_all_infected function to get list of all directly and indirectly infected people
        all_infected = get_all_infected(parsed_data, id) 
        
        #find the number of directly and indirectly infected people using len() method
        num_infected = len(all_infected)
        
        #check if number of total infections due to this person is higher than current highest
        if num_infected > max_infection_count:
            top_overall_superspreader.clear() #clear list since this is a new top superspreader
            top_overall_superspreader.append(id)
            max_infection_count = num_infected 
        
        elif num_infected == max_infection_count: #there is a tie between the superspreaders
            top_overall_superspreader.append(id) 
    
    return (top_overall_superspreader, max_infection_count)

